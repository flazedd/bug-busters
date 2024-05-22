import os
import subprocess
import time

from classes.abstract_language import LanguageImplementation
from classes.java_test import JavaTestImplementation
from config import constant
from classes.prompt import Prompt
from classes.python_test import PythonTestImplementation


class PythonImplementation(LanguageImplementation):
    def get_test_instance(self, folder, class_name, test_name):
        return PythonTestImplementation(folder, class_name, self, test_name)

    def get_code(self, ai_output):
        start = ai_output.rfind('def test')
        if start == -1:
            print('[+] def test not found')
        semi_end = ai_output.rfind('\n    ')
        if semi_end == -1:
            print('[+] semi end not found')
        end = ai_output.find('\n', semi_end)
        if end == -1:
            print('[+] end not found')
        res = ai_output[start:end]
        print(f'[+] returning:\n {res}')
        return res

    def get_args(self):
        directory = 'PythonPUT/'
        args = []
        for folder in os.listdir(directory):
            if folder.startswith('.') or folder.startswith('__'):
                continue
            folder_path = os.path.join(directory, folder)
            if os.path.isdir(folder_path):
                for file in os.listdir(folder_path):
                    if file.startswith('__') or file.startswith('test_'):
                        continue
                    file_name = file.split('.py')[0]
                    arg = (folder, file_name, constant.MODEL)
                    args.append(arg)
        return args

    @staticmethod
    def find_numbers_before_percent(string):
        i = -1
        while True:
            if string[i] == '%':
                i -= 1
                break
            i -= 1
        dot_seen = False
        numbers = ''
        while True:
            if string[i].isdigit():
                numbers = string[i] + numbers
            elif string[i] == '.' and not dot_seen:
                dot_seen = True
                numbers = string[i] + numbers
            else:
                break
            i -= 1
        return float(numbers) if numbers else None

    def get_statistics(self, terminal_output):
        start = terminal_output.find("[*] Mutation score [")
        end = terminal_output.find("- all:", start)
        target = terminal_output[start:end]
        return self.find_numbers_before_percent(target)

    @staticmethod
    def exec_mutpy(folder, file_name, test_name):
        target = f'PythonPUT/{folder}/{file_name}.py'
        unit_test = f'PythonPUT/{folder}/{test_name}.py'
        mut_script_path = os.path.join('.', 'venv', 'Scripts', 'mut.py')
        # print(mut_script_path)
        # # Run the script using subprocess
        result = subprocess.run(['python', mut_script_path,
                                 '--target', target,
                                 '--unit-test', unit_test,
                                 '--runner', 'pytest'],
                                capture_output=True, text=True, shell=True)
        # Print the output
        # print("Standard Output:")
        # print(result.stdout)
        result = result.stdout
        return result

    def get_mutation_score(self, folder, file_name, test_name):
        result = self.exec_mutpy(folder, file_name, test_name)
        return self.get_statistics(result)

    def get_dict(self, data: dict) -> dict:
        directory = 'PythonPUT/'
        args = self.get_args()
        for arg in args:
            folder = arg[0]
            class_name = arg[1]
            ai_number = arg[2]
            cpath = f'{directory}/{folder}'
            for file in os.listdir(cpath):
                if file.startswith(f"Test__{class_name}"):
                    # print(file)
                    test_name = file.split('.')[0]
                    ai_model = test_name.split("__")[2]
                    print(f'[+] ai model abbrev is {ai_model}')
                    print(f'[+] Getting mutation score for {test_name}')
                    score = self.get_mutation_score(folder, class_name, test_name)
                    print(f'[+] Mutation score for {test_name} is: {score}%')
                    result.setdefault(ai_model, {})
                    result[ai_model][class_name] = score
                    # print(test_name)
        return result

    def write_code(self, package, test_name, code):
        path = 'PythonPUT/' + package + '/' + test_name + '.py'
        with constant.PRINT_LOCK:
            print(f'[+] {package}/{test_name} is writing code')
        while True:
            try:
                with (open(path, 'w') as py_test_file):
                    # Read the contents of the file
                    py_test_file.write(code)
                    break
            except FileNotFoundError as f:
                with constant.PRINT_LOCK:
                    print(f'{package}/{test_name} has encountered FileNotFoundError. Retrying...')
                    time.sleep(constant.SLEEP)

    @staticmethod
    def get_signature(test_string):
        # Find the index of the first occurrence of "()"
        index = test_string.find("()")

        # Find the start index of the function name by searching backward from the index of "()"
        start_index = index
        while start_index > 0 and test_string[start_index - 1] != ' ':
            start_index -= 1

        # Extract the function name
        function_name = test_string[start_index:index].strip()

        return function_name

    def exec_test(self, package, test_name, test_string):
        newly_added_test = self.get_signature(test_string)
        path = f'PythonPUT/{package}/{test_name}.py::{newly_added_test}'
        result = subprocess.run(["pytest", path], shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True)
        result = f'{result.stdout} {result.stderr}'
        return result

    def did_test_fail(self, output):
        s1 = output.find('FAILURES')
        s2 = output.find('AssertionError')
        s3 = output.find('ERRORS')
        s4 = output.find('invalid syntax')
        return any(n >= 0 for n in [s1, s2, s3, s4])

    def get_test_errors(self, output, test_name_improved):
        #pytest output is pretty concise
        return output

    @staticmethod
    def get_imports_from_string(contents):
        result = set()
        s2 = 0
        while True:
            s1 = contents.find('import ', s2)
            s3 = contents.find('from ', s2)
            if s1 == -1 and s3 == -1:
                break
            elif s1 != -1 and s3 != -1:
                start = min(s1, s3)
                end = contents.find('\n', start)
                result.add(contents[start:end] + '\n')
                s2 = end
                continue
            elif s1 != -1:
                end = contents.find('\n', s1)
                if end == -1:
                    print('[+] Could not find newline after import was found')
                else:
                    result.add(contents[s1:end] + '\n')
                s2 = end
            elif s3 != -1:
                end = contents.find('\n', s3)
                if end == -1:
                    print('[+] Could not find newline after import was found')
                else:
                    result.add(contents[s3:end] + '\n')
                s2 = end
        return result

    def get_imports(self, package, class_name):
        with open(f'PythonPUT/{package}/{class_name}.py') as py_file:
            contents = py_file.read()
            imports = self.get_imports_from_string(contents)
            result = ''
            for imp in imports:
                result += imp
            return result

    @staticmethod
    def get_program_under_test(package, class_name):
        put = ''
        file_path = f'PythonPUT/{package}/{class_name}.py'
        while True:
            try:
                with open(file_path, 'r') as py_file:
                    # Read the contents of the file
                    put += py_file.read()
                    break
            except FileNotFoundError as f:
                with constant.PRINT_LOCK:
                    print(f'{package}/{class_name} has encountered FileNotFoundError. Retrying...')
                    time.sleep(constant.SLEEP)
        return put

    def get_prompt(self, package, class_name):
        class_code = self.get_program_under_test(package, class_name)
        imports = self.get_imports(package, class_name)
        extra = 'example response: \ndef test_example():\n    assert 1 == 1\n'
        return Prompt.get_input(class_code, imports, extra)

    def create_file(self, folder, class_name, ai_model):
        path = f'./PythonPUT/{folder}'
        # Check if the directory exists
        if not os.path.exists(path):
            # If it doesn't exist, create it
            os.makedirs(path)
        file = f'test__{class_name}__{ai_model}'
        file_name = f'{file}.py'
        file_path = os.path.join(path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w'):
                pass
            print(f"[+] File '{file_name}' created in '{path}'")
        else:
            print(f"[+] File '{file_name}' already exists in '{path}'")
        # Return file without .java extension
        # init = '__init__.py'
        # init_path = os.path.join(path, init)
        # if not os.path.exists(init_path):
        #     with open(init_path, 'w'):
        #         pass
        #     print(f"[+] File '{init}' created in '{path}'")
        # else:
        #     print(f"[+] File '{init}' already exists in '{path}'")
        return file

    def __str__(self):
        return 'Python'

    def work_already_satisfied(self, folder, class_name, ai_model):
        path = f'PythonPUT/{folder}/test__{class_name}__{ai_model}.py'
        if not os.path.exists(path):
            # If it doesn't exist, create it
            return False
        count = self.count_tests(path)
        return count == constant.RETRIES

    @staticmethod
    def count_tests(path):
        with open(path, 'r') as py_file:
            count = 0
            for line in py_file:
                # Check if the line contains the @Test annotation
                if "def " in line:
                    count += 1
            return count

    def generate_sbst_tool(self, folder, class_name):
        # Set the environment variable in the current process
        path = f'./PythonPUT/{folder}/test_{class_name}.py'
        # Check if the directory exists
        if os.path.exists(path) and os.path.getsize(path) > 0:
            print(f'[+] Pynguin {path} is non-empty. Skipping.')
            return
        os.environ['PYNGUIN_DANGER_AWARE'] = 'true'
        print(f"[+] PYNGUIN_DANGER_AWARE: {os.environ['PYNGUIN_DANGER_AWARE']}")
        command = [
            '.\\venv\\Scripts\\pynguin.exe',
            '--project-path', f'PythonPUT/{folder}',
            '--module-name', class_name,
            '--output-path', f'PythonPUT/{folder}',
            '--assertion-generation', 'SIMPLE',
            '--algorithm', 'DYNAMOSA',
            '--maximum-search-time', constant.PYNGUIN_MAX_SEARCH
        ]

        # Run the command
        result = subprocess.run(command, capture_output=True, text=True)
        print(f'[+] stdout: {result.stdout}')
        print(f'[+] stderror: {result.stderr}')
        print(f'[+] Generated Pynguin tests for {folder}/{class_name}.py')




