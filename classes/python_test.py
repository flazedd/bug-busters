from classes.abstract_test import HandleTestImplementation
from config import constant
from utility import utils


class PythonTestImplementation(HandleTestImplementation):
    def __init__(self, folder, class_name, oracle, test_name):
        self.oracle = oracle
        self.folder = folder
        self.test_name = test_name  #class_name + 'Test_LLM'
        # self.package = "package " + folder + ";\n"
        # self.begin_class = "public class " + self.test_name + " {\n"
        # self.end_class = "}"
        self.classname = class_name
        # self.benchmark_tests = self.get_benchmark_tests()
        self.tests = []
        # classes = utils.get_class_names_from_file(f'./PythonPUT/{folder}/{class_name}.py')
        # classes_str = ''
        # for index, item in enumerate(classes):
        #     if index == len(classes)-1:
        #         classes_str += classes[index]
        #     else:
        #         classes_str += f'{classes[index]}, '
        self.imports = {
            "import pytest\n",
            f"import {class_name} as {constant.DEFAULT_IMPORT}\n",
        }
        self.add_imports(oracle.get_imports(folder, class_name))

    def get_contents(self):
        result = ''
        imp = ''
        for line in self.imports:
            imp += line
        result += imp
        # result += self.begin_class
        # result += self.benchmark_tests
        # print(self.tests)
        for test in self.tests:
            result += test
            result += "\n\n\n"
        # result += self.end_class
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
        imps = self.oracle.get_imports_from_string(response)
        res = set()
        for line in imps.split('\n'):
            res.add(line + '\n')
        self.imports.update(res)
