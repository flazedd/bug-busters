import os
import subprocess
import time

from classes.abstract_language import LanguageImplementation
from classes.java_test import JavaTestImplementation
from config import constant
from classes.prompt import Prompt


class JavaImplementation(LanguageImplementation):
    def get_code(self, ai_output):
        # start = ai_output.find('```java')
        # if start == -1:
        #     print('[+] begin java code not found')
        #     return None
        begin = ai_output.find("@Test")
        if begin == -1:
            print('[+] @Test annotation not found')
            return None  # @Test not found

        counter = 0
        end = begin

        for char in ai_output[begin:]:
            if char == "{":
                counter += 1
            elif char == "}":
                counter -= 1

            if counter < 0 or char == '`':
                return ai_output[begin:end]

            end += 1

        return ai_output[begin:end]

    def get_args(self):
        directory = 'JavaProgramUnderTest/lib/src/main/java'
        args = []
        for folder in os.listdir(directory):
            folder_path = os.path.join(directory, folder)
            if os.path.isdir(folder_path):
                for file in os.listdir(folder_path):
                    if file.startswith('__'):
                        continue
                    file_name = file.split('.java')[0]
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

    @staticmethod
    def exec_pitest():
        # Get the current directory
        current_dir = os.getcwd()

        # Change directory to the 'JavaProgramUnderTest' directory
        os.chdir(os.path.join(current_dir, 'JavaProgramUnderTest'))

        # # Execute a list command in the current directory
        # os.system("dir" if os.name == "nt" else "ls")

        result = subprocess.run(["gradlew", "pitest", "--rerun-tasks"], shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True)
        result = result.stdout
        os.chdir(current_dir)
        return result

    @staticmethod
    def set_pitest_in_gradle(folder, class_name, test_name):
        target_class = folder + "." + class_name
        target_test = folder + "." + test_name
        # Read the build.gradle file
        with open("./JavaProgramUnderTest/lib/build.gradle", 'r') as file:
            build_gradle_content = file.read()

        # Search for targetClasses
        start_class = build_gradle_content.find("targetClasses = ['") + len("targetClasses = ['")
        end_class = build_gradle_content.find("']", start_class)
        start_test = build_gradle_content.find("targetTests = ['") + len("targetTests = ['")
        end_test = build_gradle_content.find("']", start_test)

        if start_class != -1 and end_class != -1 and start_test != -1 and end_test != -1:
            modified_build_gradle_content = (
                    build_gradle_content[:start_class]
                    + target_class
                    + build_gradle_content[end_class:start_test]
                    + target_test
                    + build_gradle_content[end_test:]
            )

            # Write back to build.gradle
            with open("./JavaProgramUnderTest/lib/build.gradle", 'w') as file:
                file.write(modified_build_gradle_content)
        else:
            print("targetClasses and/or targetTests not found in build.gradle")

    def get_mutation_score(self, folder, class_name, test_name):
        self.set_pitest_in_gradle(folder, class_name, test_name)
        result = self.exec_pitest()
        return self.get_statistics(result)

    # ('a4j_2', 'Directors', 1)
    # ('templateit_5', 'OpMatcher', 1)
    # ('tullibee_1', 'Contract', 1)
    # ('tullibee_1', 'Util', 1)
    def get_dict(self):
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


        # for folder in os.listdir(directory):
        #     folder_path = os.path.join(directory, folder)
        #     if os.path.isdir(folder_path):
        #         for file in os.listdir(folder_path):

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
        # print(f'current dir is: {current_dir}')

        # Change directory to the 'JavaProgramUnderTest' directory
        os.chdir(os.path.join(current_dir, 'JavaProgramUnderTest'))

        # # Execute a list command in the current directory
        # os.system("dir" if os.name == "nt" else "ls")
        newly_added_test = self.get_signature(test_string)
        test = package + "." + test_name + "." + newly_added_test
        result = subprocess.run(["gradlew", "test", "--tests", test, "--info"], shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True)
        result = f'{result.stdout} {result.stderr}'
        os.chdir(current_dir)
        return result

    def did_test_fail(self, output):
        target = "FAILED"
        start_index = output.find(target)
        return start_index >= 0

    def get_test_errors(self, output, test_name_improved):
        id = ':lib:test FAILED'
        semi = output.find(id) + len(id)
        output = output[semi:]
        print(f"[+] Semi-filtered test error:\n\n {output}")
        suitable = output.find('error: no suitable method found')
        suitable2 = output.find('^', suitable)
        if suitable != -1:
            return output[suitable:suitable2]
        begin = max(output.find('FAILED'), 0)
        end = output.find('FAILURE')
        return output[begin:end]

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
        class_code = self.get_program_under_test(package, class_name)
        imports = self.get_imports(package, class_name)
        extra = ('your code snippet should start with @Test '
                 'and examples of asserting methods: assertEquals(), assertArrayEquals()')
        return Prompt.get_input(class_code, imports, extra)

    def get_test_instance(self, folder, class_name, test_name):
        return JavaTestImplementation(folder, class_name, self, test_name)

    def create_file(self, folder, class_name, ai_model):
        path = f'./JavaProgramUnderTest/lib/src/test/java/{folder}'
        # Check if the directory exists
        if not os.path.exists(path):
            # If it doesn't exist, create it
            os.makedirs(path)
        file = f'Test__{class_name}__{ai_model}'
        file_name = f'{file}.java'
        file_path = os.path.join(path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w'):
                pass
            print(f"[+] File '{file_name}' created in '{path}'")
        else:
            print(f"[+] File '{file_name}' already exists in '{path}'")
        # Return file without .java extension
        return file

    def __str__(self):
        return 'Java'

    def work_already_satisfied(self, folder, class_name, ai_model):
        path = f'JavaProgramUnderTest/lib/src/test/java/{folder}/Test__{class_name}__{ai_model}.java'
        if not os.path.exists(path):
            # If it doesn't exist, create it
            return False
        with open(path, 'r') as java_file:
            count = 0
            for line in java_file:
                # Check if the line contains the @Test annotation
                if "@Test" in line:
                    count += 1
            return count == constant.RETRIES


