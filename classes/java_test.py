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
        }
        self.add_imports(oracle.get_imports(folder, class_name))

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
        self.tests.pop()

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
            self.imports.add(element)