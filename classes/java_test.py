from classes.abstract_test import HandleTestImplementation
from config import constant

class JavaTestImplementation(HandleTestImplementation):
    def __init__(self, folder, class_name, oracle, test_name):
        self.oracle = oracle
        self.folder = folder
        self.test_name = test_name #class_name + 'Test_LLM'
        self.package = "package " + folder + ";\n"
        self.begin_class = "public class " + self.test_name + " {\n"
        self.end_class = "}"
        self.classname = class_name
        # self.benchmark_tests = self.get_benchmark_tests()
        self.tests = []
        self.imports = {
            "import org.junit.jupiter.api.Test;\n",
            "import static org.junit.jupiter.api.Assertions.*;\n",
            "import java.util.Arrays;\n"
        }
        self.add_imports(oracle.get_imports(folder, class_name))
        self.fill_tests()

    def fill_tests(self):
        filepath = f'./JavaProgramUnderTest/lib/src/test/java/{self.folder}/{self.test_name}.java'
        with open(filepath, 'r') as file:
            content = file.read()
        end_import = content.find('@Test')
        index_tracker = end_import
        while True:
            begin = content.find('@Test', index_tracker)
            if begin == -1:
                # print('[+] @Test annotation not found')
                # self.end_file = content[index_tracker:]
                break
            counter = 0
            end = begin
            brace_seen = False
            for char in content[begin:]:
                if char == "{":
                    counter += 1
                    brace_seen = True
                elif char == "}":
                    counter -= 1

                if counter == 0 and brace_seen:
                    self.tests.append(content[begin:end+1])
                    index_tracker = end+1
                    break

                end += 1
        if len(self.tests) > 0:
            result = self.oracle.exec_test(self.folder, self.test_name, self.tests[-1])
            if self.oracle.did_test_fail(result):
                self.remove_last_test()
        print(f'[+] Already found {len(self.tests)} working tests from previous iteration!')

    def get_required_tests(self):
        return constant.RETRIES - len(self.tests)

    def get_contents(self):
        result = self.package
        imp = ''
        for line in self.imports:
            imp += line
        result += imp
        result += self.begin_class
        # result += self.benchmark_tests
        # print(self.tests)
        for test in self.tests:
            result += test
            result += "\n"
        result += self.end_class
        return result

    def write(self):
        code = self.get_contents()
        # improved_test = self.classname + "_LLM"
        self.oracle.write_code(self.folder, self.test_name, code)

    def empty_file(self):
        self.oracle.write_code(self.folder, self.test_name, '')

    def add_test(self, test):
        self.tests.append(test)

    def remove_last_test(self):
        try:
            self.tests.pop()
        except IndexError:
            pass
            # print("")
            # Handle the error as needed, e.g., log it, raise a different exception, etc.

    def add_imports(self, response):
        res = []
        end = 0
        while True:
            start = response.find('import', end)
            end = response.find(';\n', start)
            if start == -1 or end == -1:
                break
            res.append(response[start:end + 2])
        for element in res:
            if 'junit' in element:
                continue
            self.imports.add(element)