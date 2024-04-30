import os
import subprocess
import time

from hugchat import hugchat
from hugchat.login import Login
import re
import Test
import config
import constant

cookie_path_dir = "./cookies/"  # NOTE: trailing slash (/) is required to avoid errors
sign = Login(config.MAIL, config.PASSWORD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)


def set_pitest_in_gradle(package, classname, testname):
    target_class = package + "." + classname
    target_test = package + "." + testname
    # Read the build.gradle file
    with open("JavaProgramUnderTest/lib/build.gradle", 'r') as file:
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
        with open("JavaProgramUnderTest/lib/build.gradle", 'w') as file:
            file.write(modified_build_gradle_content)
    else:
        print("targetClasses and/or targetTests not found in build.gradle")


def get_java_code(ai_output):
    pattern = r"(@Test\s+public void \w+\(\) \{([^}]+)\})"

    # Find all test functions
    test_functions = re.findall(pattern, ai_output)
    result = ''
    try:
        result = test_functions[0][0]
    except IndexError:
        return None
    # print(type(result))
    # print(f'returning: {result}')
    return result


def get_args():
    directory = 'JavaProgramUnderTest/lib/src/test/java'
    args = []
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                if file.endswith("Test.java"):
                    file_name = file.split("Test.java")[0]
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
        print(f'{package}/{test_name} is writing code')
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


def exec_test(package, test_name):
    # Get the current directory
    current_dir = os.getcwd()

    # Change directory to the 'JavaProgramUnderTest' directory
    os.chdir(os.path.join(current_dir, 'JavaProgramUnderTest'))

    # # Execute a list command in the current directory
    # os.system("dir" if os.name == "nt" else "ls")
    test = package + "." + test_name
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


def concatenate_files_except(package, filename):
    filename = filename + ".java"
    file_path = f"JavaProgramUnderTest/lib/src/main/java/{package}"
    concatenated_content = ""

    # Check if the directory exists
    if os.path.exists(file_path) and os.path.isdir(file_path):
        # Loop through each file in the directory
        for file in os.listdir(file_path):
            file_path = os.path.join(file_path, file)

            # Check if the item is a file and is not the specified filename
            if os.path.isfile(file_path) and file != filename:
                # Read the content of the file and concatenate it
                with open(file_path, 'r') as f:
                    concatenated_content += f.read()

    return concatenated_content


def get_prompt(package, classname, testname):
    prompt = ''
    with open('JavaProgramUnderTest/lib/src/main/java/' + package + '/' + classname + '.java', 'r') as java_file:
        # Read the contents of the file
        prompt += java_file.read()
    improved_name = classname + 'Test_Improved'
    with open('JavaProgramUnderTest/lib/src/test/java/' + package + '/' + testname + '.java', 'r') as java_test_file:
        # Read the contents of the file
        prompt += java_test_file.read()
    prompt += (
        f'give me back 1 additional test case that starts with @Test, it should only make 1 assertion and '
        f'it should pass.')
    return prompt


# expects tuple with (folder, file_name, model_number)
def worker(folder, file_name, selection):
    test_name = file_name + 'Test'
    start = time.time()
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    chatbot.switch_llm(selection)
    l = chatbot.get_remote_llms()
    with constant.PRINT_LOCK:
        print(f'{folder} has switched to {l[selection].name}')
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    prompt = get_prompt(folder, file_name, test_name)
    tests_required = constant.RETRIES
    test_handle = Test.Test(folder, test_name)
    iterations = 0
    failing_tests = 0
    replies_without_tests = 0
    while tests_required > 0:
        iterations += 1
        with constant.PRINT_LOCK:
            print(f'{folder} is on iteration {iterations}')
        response = chatbot.chat(prompt)
        response.wait_until_done()
        new_test_case = get_java_code(response.text)
        if new_test_case is None:
            replies_without_tests += 1
            prompt = 'try again. remember, 1 test case. 1 assertion'
            continue
        test_handle.add_test(new_test_case)
        test_handle.write()
        improved_test = test_name + "_Improved"
        result = exec_test(folder, improved_test)
        if did_test_fail(result):
            failing_tests += 1
            test_handle.remove_last_test()
            error = get_test_errors(result, improved_test)
            prompt = error + "make it pass, different function name than the ones you sent before"
            continue
        else:
            prompt = ('It passed. Now give another completely new test case.')
            tests_required -= 1
    end = time.time()
    with constant.PRINT_LOCK:
        print(f'{folder} finished in {end - start} seconds. '
              f'Iterations: {iterations}. ',
              f'Stricly needed iterations: {constant.RETRIES}. '
              f'Tests that failed:  {failing_tests}. '
              f'Replies without tests: {replies_without_tests}. ')
