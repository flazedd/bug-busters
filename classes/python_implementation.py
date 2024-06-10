import ast
import concurrent
import math
import os
import random
import string
import subprocess
import time

from classes.abstract_language import LanguageImplementation
from classes.java_test import JavaTestImplementation
from config import constant
from classes.prompt import Prompt
from classes.python_test import PythonTestImplementation
from classes.python_test_reader import PythonReaderTestImplementation


class PythonImplementation(LanguageImplementation):
    def get_test_instance(self, folder, class_name, test_name):
        return PythonTestImplementation(folder, class_name, self, test_name)

    @staticmethod
    def generate_random_string(length=8):
        # Define the character set to include lowercase letters and digits
        characters = string.ascii_lowercase + string.digits
        # Generate a random string of the specified length
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    def extract_first_function_code(self, code):
        # Parse the code into an Abstract Syntax Tree (AST)
        tree = ast.parse(code)

        # Iterate through the nodes in the tree
        for node in ast.walk(tree):
            # Check if the node is a function definition
            if isinstance(node, ast.FunctionDef):
                # Get the source code of the function
                random_suffix = self.generate_random_string()
                node.name = f"{node.name}_{random_suffix}"
                function_code = ast.unparse(node)
                return function_code.strip()

        # If no function definition is found, return None
        return None

    def get_code(self, ai_output):
        # print(f'[+] ai_output:\n\n {ai_output}')
        start = ai_output.find('def')
        end = ai_output.find('```', start)
        code = ai_output[start:end]
        res = self.extract_first_function_code(code)

        # start = ai_output.rfind('def test')
        # if start == -1:
        #     print('[+] def test not found')
        # semi_end = ai_output.rfind('\n    ')
        # if semi_end == -1:
        #     print('[+] semi end not found')
        # end = ai_output.find('\n', semi_end)
        # if end == -1:
        #     print('[+] end not found')
        # res = ai_output[start:end] + '\n'
        # print(f'[+] returning:\n {res}')
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
                    file_path = os.path.join(folder_path, file)
                    if file.startswith('__') or file.startswith('test_') or os.path.isdir(file_path):
                        continue
                    file_name = file.split('.py')[0]
                    arg = (folder, file_name, constant.MODEL)
                    args.append(arg)
        return args

    @staticmethod
    def find_numbers_before_percent(string):
        try:
            i = -1
            if len(string) < 2:
                return None
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
        except IndexError:
            return None

    def get_statistics(self, terminal_output):
        start = terminal_output.find("[*] Mutation score [")
        end = terminal_output.find("- all:", start)
        target = terminal_output[start:end]
        return self.find_numbers_before_percent(target)

    @staticmethod
    def exec_mutpy(folder, class_name, test_name):
        target = f'PythonPUT/{folder}/{class_name}.py'
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
        result = result.stdout + result.stderr
        return result

    def get_mutation_score(self, folder, file_name, test_name):
        result = self.exec_mutpy(folder, file_name, test_name)
        stats = self.get_statistics(result)
        if stats is not None:
            return stats
        print('[+] Could not find stats in mutpy, returning NaN...')
        time.sleep(2)
        return math.nan
        # return self.get_mutation_score(folder, file_name, test_name)

    def get_dict(self, run) -> dict:
        directory = 'PythonPUT/'
        args = self.get_args()
        result = {}
        for arg in args:
            folder = arg[0]
            class_name = arg[1]
            ai_number = arg[2]
            cpath = f'{directory}/{folder}'
            for file in os.listdir(cpath):
                mixed_name = f'{folder}.{class_name}'
                if file.startswith(f"test__{class_name}") and file.endswith(f'__{run}.py'):
                    # print(file)
                    # pass
                    test_name = file.split('.')[0]
                    ai_model = test_name.split("__")[2]
                    # print(f'[+] AI: {ai_model}')
                    print(f'[+] Getting mutation score for {test_name}')
                    result.setdefault(ai_model, {})
                    result[ai_model][mixed_name] = [0]
                    py_reader = PythonReaderTestImplementation(folder, self, test_name)
                    amount_tests = py_reader.amount_of_tests()
                    for i in range(1, amount_tests + 1):
                        py_reader.partial_write(i)
                        score = self.get_mutation_score(folder, class_name, test_name)
                        print(f'[+] Mutation score for {test_name} is: {score}% with {i} tests enabled')
                        result[ai_model][mixed_name].append(score)
                elif file.startswith(f"test_{class_name}") and file.endswith(f'_{run}.py'):
                    test_name = file.split('.')[0]
                    print(f'[+] Getting mutation score for {test_name}')
                    result.setdefault('Pynguin', {})
                    score = self.get_mutation_score(folder, class_name, test_name)
                    result['Pynguin'][mixed_name] = score
                    print(f'[+] Mutation score for {test_name} is: {score}% for Pynguin')
        return result

    def write_code(self, package, test_name, code):
        path = 'PythonPUT/' + package + '/' + test_name + '.py'
        # with constant.PRINT_LOCK:
        #     print(f'[+] {package}/{test_name} is writing code')
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

    def exec_suite(self, package, test_name):
        path = f'PythonPUT/{package}/{test_name}.py'
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
        print(f'[+] Test error: {output}')
        return output

    @staticmethod
    def get_imports_from_string(code):
        # Parse the code into an AST
        tree = ast.parse(code)

        # Initialize a list to collect import statements
        imports = []

        # Traverse the AST
        for node in ast.walk(tree):
            # Check for import statements
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(f"import {alias.name}")
            elif isinstance(node, ast.ImportFrom):
                module = node.module if node.module else ''
                for alias in node.names:
                    imports.append(f"from {module} import {alias.name}")

        # Return imports as a single string
        return "\n".join(imports)

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
        file_path = f'./PythonPUT/{package}/{class_name}.py'
        while True:
            try:
                with open(file_path, 'r') as py_file:
                    # Read the contents of the file
                    put += py_file.read()
                    break
            except FileNotFoundError as f:
                with constant.PRINT_LOCK:
                    print(f'{file_path} has encountered FileNotFoundError. Retrying...')
                    time.sleep(constant.SLEEP)
        return put

    def get_prompt(self, package, class_name):
        # start = f'{class_name} imported as {constant.DEFAULT_IMPORT}'
        class_code = self.get_program_under_test(package, class_name)
        imports = self.get_imports(package, class_name)
        extra = (f'example response: import {class_name} as {constant.DEFAULT_IMPORT} ```\ndef test_example():\n   '
                 f' assert 1 == 1\n``` only use {constant.DEFAULT_IMPORT} in your test case. '
                 f'insert any newly defined functions inside the test case or access it like module_0.function!')
        return Prompt.get_input(class_code, imports, extra)

    def create_file(self, folder, class_name, ai_model, run):
        path = f'./PythonPUT/{folder}'
        # Check if the directory exists
        if not os.path.exists(path):
            # If it doesn't exist, create it
            os.makedirs(path)
        file = f'test__{class_name}__{ai_model}__{run}'
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

    def work_already_satisfied(self, folder, class_name, ai_model, run):
        test_name = f'test__{class_name}__{ai_model}__{run}'
        path = f'PythonPUT/{folder}/.py'
        if not os.path.exists(path):
            # If it doesn't exist, create it
            return False
        count = self.count_tests(path)
        if count == constant.RETRIES:
            result = self.exec_suite(folder, test_name)
            passing = self.did_test_fail(result)
            return not passing
        else:
            return False

    @staticmethod
    def count_tests(path):
        with open(path, 'r') as py_file:
            count = 0
            for line in py_file:
                # Check if the line contains the @Test annotation
                if "def test" in line:
                    count += 1
            return count

    def pynguin(self, folder, class_name):
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
        return result

    def run_with_timeout(self, func, timeout, *args):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(func, *args)
            try:
                result = future.result(timeout=timeout)
                return result
            except concurrent.futures.TimeoutError:
                print(f"Function call timed out after {timeout} seconds. Retrying...")
                return self.run_with_timeout(func, timeout, *args)

    def generate_sbst_tool(self, folder, class_name, run):
        # Set the environment variable in the current process
        epath = f'./PythonPUT/{folder}/test_{class_name}_{run}.py'
        new_path = f'./PythonPUT/{folder}/test_{class_name}_{constant.PYNGUIN_MAX_SEARCH}_{run}.py'
        # Check if the directory exists
        if os.path.exists(new_path) and os.path.getsize(new_path) > 0:
            print(f'[+] Pynguin {new_path} is non-empty. Skipping.')
            return
        if os.path.exists(epath) and os.path.getsize(epath) > 0:
            print(f'[+] Pynguin {epath} is non-empty. Skipping.')
            return
        os.environ['PYNGUIN_DANGER_AWARE'] = 'true'
        # print(f"[+] PYNGUIN_DANGER_AWARE: {os.environ['PYNGUIN_DANGER_AWARE']}")
        iteration = 1
        while True:
            print(f'[+] Running Pynguin on {folder}/{class_name} on try {iteration}')
            iteration += 1
            timeout = int(constant.PYNGUIN_MAX_SEARCH) + 30
            result = self.run_with_timeout(self.pynguin, timeout, folder, class_name)
            # result = self.pynguin(folder, class_name)
            print(f'[+] stdout: {result.stdout}')
            print(f'[+] stderror: {result.stderr}')
            print(f'[+] Generated Pynguin tests for {folder}/{class_name}.py')
            test_name = f'test_{class_name}'
            result = self.exec_suite(folder, test_name)
            if not self.did_test_fail(result):
            # result = self.exec_mutpy(folder, class_name, test_name)
            # stats = self.get_statistics(result)
            # if stats is not None:
                old_path = f'./PythonPUT/{folder}/test_{class_name}.py'
                os.rename(old_path, new_path)
                break



