import os
import subprocess
import time

from classes.abstract_language import LanguageImplementation
from classes.java_test import JavaTestImplementation
from config import constant
from classes.prompt import Prompt


class PythonImplementation(LanguageImplementation):
    def get_test_instance(self, folder, class_name, test_name):
        pass

    def get_code(self, ai_output):
        start = ai_output.rfind('def test')
        if start == -1:
            print('[+] def test not found')
        semi_end = ai_output.rfind('\n    ')
        if semi_end == -1:
            print('[+] semi end not found')
        end = ai_output.rfind('\n', semi_end)
        if end == -1:
            print('[+] end not found')
        return ai_output[start:end + 1]

    def get_args(self):
        directory = 'PythonPUT/'
        args = []
        for folder in os.listdir(directory):
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

    def get_dict(self, folder, file_name, test_name):
        directory = 'JavaProgramUnderTest/lib/src/test/java'
        result = {}
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
        pass

    def exec_test(self, package, test_name, test_string):
        pass

    def did_test_fail(self, output):
        pass

    def get_test_errors(self, output, test_name_improved):
        pass

    def get_imports(self, package, class_name):
        pass

    def get_prompt(self, package, class_name):
        pass

    def create_file(self, folder, class_name, ai_model):
        pass

    def __str__(self):
        pass

    def work_already_satisfied(self, folder, class_name, ai_model):
        pass
