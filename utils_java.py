import os
import subprocess
import time

from hugchat import hugchat
from hugchat.login import Login
import re
import Test
import config
import constant


def set_pitest_in_gradle(package, classname, testname):
    pass


def get_java_code(ai_output):
    # print(ai_output)
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


def get_args():
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


def get_statistics(terminal_output):
    start = terminal_output.find("- Statistics")
    result = terminal_output[start:]
    s1 = result.find(">> Line Coverage (for mutated classes only):")
    s2 = result.find(">> Generated")
    s3 = result.find(">> Mutations")
    s4 = result.find(">> Ran")
    part1 = result[s1:s2]
    part2 = result[s2:s3]
    part3 = result[s3:s4]
    statistics = {'Line coverage %': find_numbers_before_percent(part1),
                  'Mutations killed %': find_numbers_before_percent(part2),
                  # 'Mutations': find_numbers_before_percent(part3)
                  }
    return statistics


def exec_pitest():
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


def write_code(package, test_name, code):
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
                time.sleep(1)


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

def exec_test(package, test_name, test_string):
    # Get the current directory
    current_dir = os.getcwd()

    # Change directory to the 'JavaProgramUnderTest' directory
    os.chdir(os.path.join(current_dir, 'JavaProgramUnderTest'))

    # # Execute a list command in the current directory
    # os.system("dir" if os.name == "nt" else "ls")
    newly_added_test = get_signature(test_string)
    test = package + "." + test_name + "." + newly_added_test
    result = subprocess.run(["gradlew", "test", "--tests", test, "--info"], shell=True, stdout=subprocess.PIPE,
                            text=True)
    result = result.stdout
    os.chdir(current_dir)
    return result


def did_test_fail(output):
    target = "FAILED"
    start_index = output.find(target)
    return start_index >= 0


def get_test_errors(output, test_name_improved):
    # print(f"[get_test_errors]output received: {output}")
    pattern = rf'{test_name_improved}\s>\s(\w+)\(\) FAILED[\s\S](.*)'
    matches = re.findall(pattern, output)
    result = ''
    for i in range(0, len(matches)):
        result += matches[i][-1] + '\n'
    return result


def get_imports(package, test_name):
    with open('JavaProgramUnderTest/lib/src/test/java/' + package + '/' + test_name + '.java', 'r') as java_test_file:
        # Read the contents of the file
        contents = java_test_file.read()
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


def get_program_under_test(package, class_name):
    with open('JavaProgramUnderTest/lib/src/main/java/' + package + '/' + class_name + '.java', 'r') as java_file:
        # Read the contents of the file
        prompt = java_file.read()
        return prompt

def get_specific_prompt():
    return 'your code snippet should start with @Test'
