from classes.abstract_test import HandleTestImplementation
from config import constant


class JavaTestImplementation(HandleTestImplementation):
    def __init__(self, folder, class_name, oracle):
        self.oracle = oracle
        self.folder = folder
        self.target = class_name + 'Test_LLM'
        self.begin_template = (
                "package " + folder + ";\n" +
                "import org.junit.jupiter.api.Test;\n" +
                "import static org.junit.jupiter.api.Assertions.*;\n" +
                oracle.get_imports(folder, class_name) +
                "public class " + self.target + " {\n"
        )
        self.end_template = "}"
        self.classname = class_name
        # self.benchmark_tests = self.get_benchmark_tests()
        self.tests = []

    def get_contents(self):
        result = self.begin_template
        # result += self.benchmark_tests
        # print(self.tests)
        for test in self.tests:
            result += test
            result += "\n"
        result += self.end_template
        return result

    def write(self):
        code = self.get_contents()
        # improved_test = self.classname + "_LLM"
        self.oracle.write_code(self.folder, self.target, code)

    def add_test(self, t):
        self.tests.append(t)

    def remove_last_test(self):
        self.tests.pop()