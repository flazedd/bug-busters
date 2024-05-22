from classes.abstract_test_reader import ReaderTestImplementation
from config import constant


class JavaReaderTestImplementation(ReaderTestImplementation):
    def __init__(self, folder, oracle, test_name):
        self.filepath = f'./JavaProgramUnderTest/lib/src/test/java/{folder}/{test_name}.java'
        with open(self.filepath, 'r') as file:
            content = file.read()
        end_import = content.find('@Test')
        self.imports = content[:end_import]
        self.tests = []
        self.test_name = test_name
        self.oracle = oracle
        self.folder = folder
        self.end_file = ''
        index_tracker = end_import
        while True:
            begin = content.find('@Test', index_tracker)
            if begin == -1:
                # print('[+] @Test annotation not found')
                self.end_file = content[index_tracker:]
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
        print(f'[+] Found {len(self.tests)} when reading file')

    def partial_write(self, amount: int) -> None:
        code = self.imports
        for i in range(0, amount):
            code += self.tests[i] + '\n\n'
        code += self.end_file
        self.oracle.write_code(self.folder, self.test_name, code)

    def amount_of_tests(self) -> int:
        return len(self.tests)