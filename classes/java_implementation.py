import os
import re
import subprocess
import time

from classes.abstract_language import LanguageImplementation
from classes.java_test import JavaTestImplementation
from config import constant


class JavaImplementation(LanguageImplementation):
    def get_code(self, ai_output):
        result = ''
        s1 = ai_output.find('```java')
        if s1 == -1:
            return None
        s2 = ai_output.find('@Test', s1)
        if s2 == -1:
            return None
        s3 = ai_output.find('```', s2)
        if s3 == -1:
            return None
        result += ai_output[s2:s3]
        return result

    def get_args(self):
        directory = 'JavaProgramUnderTest/lib/src/test/java'
        args = []
        for folder in os.listdir(directory):
            folder_path = os.path.join(directory, folder)
            if os.path.isdir(folder_path):
                for file in os.listdir(folder_path):
                    if file.endswith("Test_EvoSuite.java"):
                        file_name = file.split("Test_EvoSuite.java")[0]
                        arg = (folder, file_name, constant.MODEL)
                        args.append(arg)
        return args

    def find_numbers_before_percent(self, string):
        i = -1
        while True:
            if string[i] == '%':
                i -= 1
                break
            i -= 1

        numbers = ''
        while True:
            if string[i].isdigit():
                numbers = string[i] + numbers
                i -= 1
            else:
                break

        return int(numbers) if numbers else None

    def get_statistics(self, terminal_output):
        start = terminal_output.find("- Statistics")
        result = terminal_output[start:]
        s1 = result.find(">> Line Coverage (for mutated classes only):")
        s2 = result.find(">> Generated")
        s3 = result.find(">> Mutations")
        s4 = result.find(">> Ran")
        part1 = result[s1:s2]
        part2 = result[s2:s3]
        part3 = result[s3:s4]
        # statistics = {'Line coverage %': self.find_numbers_before_percent(part1),
        #               'Mutations killed %': self.find_numbers_before_percent(part2),
        #               # 'Mutations': find_numbers_before_percent(part3)
        #               }
        # return statistics
        return self.find_numbers_before_percent(part2)

    def get_mutation_score(self, folder, file_name, test_name):
        pass

    def exec_pitest(self):
        # Get the current directory
        current_dir = os.getcwd()

        # Change directory to the 'JavaProgramUnderTest' directory
        os.chdir(os.path.join(current_dir, 'JavaProgramUnderTest'))

        # # Execute a list command in the current directory
        # os.system("dir" if os.name == "nt" else "ls")

        result = subprocess.run(["gradlew", "pitest", "--rerun-tasks"], shell=True, stdout=subprocess.PIPE, text=True)
        result = result.stdout
        os.chdir(current_dir)
        return result

    def write_code(self, package, test_name, code):
        path = 'JavaProgramUnderTest/lib/src/test/java/' + package + '/' + test_name + '.java'
        with constant.PRINT_LOCK:
            print(f'[+] {package}/{test_name} is writing code')
        while True:
            try:
                with (open(path, 'w') as java_test_file):
                    # Read the contents of the file
                    java_test_file.write(code)
                    break
            except FileNotFoundError as f:
                with constant.PRINT_LOCK:
                    print(f'{package}/{test_name} has encountered FileNotFoundError. Retrying...')
                    time.sleep(constant.SLEEP)

    def get_signature(self, test_string):
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
        # Get the current directory
        current_dir = os.getcwd()

        # Change directory to the 'JavaProgramUnderTest' directory
        os.chdir(os.path.join(current_dir, 'JavaProgramUnderTest'))

        # # Execute a list command in the current directory
        # os.system("dir" if os.name == "nt" else "ls")
        newly_added_test = self.get_signature(test_string)
        test = package + "." + test_name + "." + newly_added_test
        result = subprocess.run(["gradlew", "test", "--tests", test, "--info"], shell=True, stdout=subprocess.PIPE,
                                text=True)
        result = result.stdout
        os.chdir(current_dir)
        return result

    def did_test_fail(self, output):
        target = "FAILED"
        start_index = output.find(target)
        return start_index >= 0

    def get_test_errors(self, output, test_name_improved):
        # print(f"[get_test_errors]output received: {output}")
        pattern = rf'{test_name_improved}\s>\s(\w+)\(\) FAILED[\s\S](.*)'
        matches = re.findall(pattern, output)
        result = ''
        for i in range(0, len(matches)):
            result += matches[i][-1] + '\n'
        return result

    def get_imports(self, package, class_name):
        with open(f'JavaProgramUnderTest/lib/src/main/java/{package}/{class_name}.java') as java_file:
            contents = java_file.read()
            result = ""
            s2 = 0
            while True:
                s1 = contents.find('import', s2)
                if s1 == -1:
                    break
                s2 = contents.find('\n', s1)
                if s2 == -1:
                    with constant.PRINT_LOCK:
                        print('Could not find newline after import was found')
                result += contents[s1:s2] + '\n'
            return result

    def get_program_under_test(self, package, class_name):
        put = ''
        file_path = f'JavaProgramUnderTest/lib/src/main/java/{package}/{class_name}.java'
        while True:
            try:
                with open(file_path, 'r') as java_file:
                    # Read the contents of the file
                    put += java_file.read()
                    break
            except FileNotFoundError as f:
                with constant.PRINT_LOCK:
                    print(f'{package}/{class_name} has encountered FileNotFoundError. Retrying...')
                    time.sleep(constant.SLEEP)
        return put

    def get_prompt(self, package, class_name):
        prompt = ''
        prompt += self.get_program_under_test(package, class_name)
        imports = self.get_imports(package, class_name)
        prompt += '\nyou can use these imports only\n' + imports
        prompt += 'give me back 1 single test case, it should only make 1 single assertion and it should pass!. '
        prompt += 'your code snippet should start with @Test'
        return prompt

    def get_test_instance(self, folder, class_name):
        return JavaTestImplementation(folder, class_name, self)
