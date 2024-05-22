from classes.abstract_test_reader import ReaderTestImplementation
from config import constant


class PythonReaderTestImplementation(ReaderTestImplementation):
    def __init__(self, folder, class_name, oracle, test_name):
        filepath = f'./PythonPUT/{folder}/{test_name}.py'
        with open(filepath, 'r') as file:
            content = file.read()
        end_import = content.find('def ')
        self.imports = content[:end_import]
        self.tests = []
        self.test_name = test_name
        self.oracle = oracle
        self.folder = folder
        index_tracker = end_import
        while True:
            start = content.find('def ', index_tracker)
            end = content.find('def ', start + 4)
            if end == -1:
                self.tests.append(content[start:])
                break
            else:
                self.tests.append(content[start:end])
            index_tracker = end

    def partial_write(self, amount: int) -> None:
        code = self.imports
        for i in range(0, amount):
            code += self.tests[i]
        self.oracle.write_code(self.folder, self.test_name, code)

    def amount_of_tests(self) -> int:
        pass
