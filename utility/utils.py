import time

from config import constant
from utility import utils_java, credentails, utils_python
from classes.test import Test


# cookie_path_dir = "./cookies/"  # NOTE: trailing slash (/) is required to avoid errors
# sign = Login(config.MAIL, config.PASSWORD)
# cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)


# def set_pitest_in_gradle(package, classname, testname):
#     target_class = package + "." + classname
#     target_test = package + "." + testname
#     # Read the build.gradle file
#     with open("../JavaProgramUnderTest/lib/build.gradle", 'r') as file:
#         build_gradle_content = file.read()
#
#     # Search for targetClasses
#     start_class = build_gradle_content.find("targetClasses = ['") + len("targetClasses = ['")
#     end_class = build_gradle_content.find("']", start_class)
#     start_test = build_gradle_content.find("targetTests = ['") + len("targetTests = ['")
#     end_test = build_gradle_content.find("']", start_test)
#
#     if start_class != -1 and end_class != -1 and start_test != -1 and end_test != -1:
#         modified_build_gradle_content = (
#                 build_gradle_content[:start_class]
#                 + target_class
#                 + build_gradle_content[end_class:start_test]
#                 + target_test
#                 + build_gradle_content[end_test:]
#         )
#
#         # Write back to build.gradle
#         with open("../JavaProgramUnderTest/lib/build.gradle", 'w') as file:
#             file.write(modified_build_gradle_content)
#     else:
#         print("targetClasses and/or targetTests not found in build.gradle")
#
#
# def get_java_code(ai_output, language):
#     if language == "java":
#         return utils_java.get_java_code(ai_output)
#     elif language == "python":
#         return utils_python.get_java_code(ai_output)
#
#
# def get_args(language):
#     if language == "java":
#         return utils_java.get_args()
#     elif language == "python":
#         return utils_python.get_args()
#     else:
#         raise Exception("Language not supported")
#
#
# # removed def find_numbers_before_percent(string):
#
# def get_statistics(terminal_output):
#     return utils_java.get_statistics(terminal_output)
#
#
# def exec_pitest():
#     return utils_java.exec_pitest()
#
#
# def write_code(package, test_name, code):
#     utils_java.write_code(package, test_name, code)
#
#
# def exec_test(package, test_name, test_string):
#     return utils_java.exec_test(package, test_name, test_string)
#
#
# def did_test_fail(output):
#     return utils_java.did_test_fail(output)
#
#
# def get_test_errors(output, test_name_improved):
#     return utils_java.get_test_errors(output, test_name_improved)


# def concatenate_files_except(package, filename):
#     filename = filename + ".java"
#     file_path = f"JavaProgramUnderTest/lib/src/main/java/{package}"
#     concatenated_content = ""
#
#     # Check if the directory exists
#     if os.path.exists(file_path) and os.path.isdir(file_path):
#         # Loop through each file in the directory
#         for file in os.listdir(file_path):
#             file_path = os.path.join(file_path, file)
#
#             # Check if the item is a file and is not the specified filename
#             if os.path.isfile(file_path) and file != filename:
#                 # Read the content of the file and concatenate it
#                 with open(file_path, 'r') as f:
#                     concatenated_content += f.read()
#
#     return concatenated_content


# def get_imports(package, test_name):
#     return utils_java.get_imports(package, test_name)
#
#
# def get_prompt(package, class_name, language):
#     prompt = ''
#     if language == 'java':
#         prompt += utils_java.get_program_under_test(package, class_name)
#     # elif language == 'python':
#     #     prompt += utils_python.get_program_under_test(package, class_name)
#     imports = get_imports(package, class_name)
#     prompt += '\nyou can use these imports only\n' + imports
#     prompt += 'give me back 1 single test case, it should only make 1 single assertion and it should pass!. '
#     prompt += utils_java.get_specific_prompt()
#     return prompt


def get_identifier(ai_model_name):
    start_index = ai_model_name.find('/')
    end_index = ai_model_name.find('-', start_index)
    return ai_model_name[start_index + 1:end_index]


# expects tuple with (folder, file_name, model_number)
def worker(folder, class_name, selection, oracle):
    test_name = class_name + 'Test'
    start = time.time()
    chatbot = credentails.get_chatbot()
    chatbot.switch_llm(selection)
    l = chatbot.get_remote_llms()
    with constant.PRINT_LOCK:
        print(f'[+] {folder} has switched to {l[selection].name}')
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    prompt = oracle.get_prompt(folder, class_name)
    tests_required = constant.RETRIES
    test_handle = oracle.get_test_instance(folder, class_name)  #Test(folder, class_name)
    iterations = 0
    failing_tests = 0
    replies_without_tests = 0
    while tests_required > 0:
        iterations += 1
        with constant.PRINT_LOCK:
            print(f'[+] {folder} is on iteration {iterations}')
        response = chatbot.chat(prompt)
        response.wait_until_done()
        new_test_case = oracle.get_code(response.text) #get_java_code(response.text)
        if new_test_case is None:
            with constant.PRINT_LOCK:
                print('[+] No test case found in reply')
            replies_without_tests += 1
            prompt = 'try again. remember, 1 test case. 1 assertion'
            continue
        test_handle.add_test(new_test_case)
        test_handle.write()
        improved_test = test_name + "_LLM"
        result = oracle.exec_test(folder, improved_test, new_test_case) #exec_test(folder, improved_test, new_test_case)
        if oracle.did_test_fail(result):
            with constant.PRINT_LOCK:
                print('[+] Did find a test but it failed')
            failing_tests += 1
            test_handle.remove_last_test()
            error = oracle.get_test_errors(result, improved_test)
            prompt = error + "make it pass, different function name than the ones you sent before"
            continue
        else:
            with constant.PRINT_LOCK:
                print('[+] Test case found and compiles')
            prompt = ('It passed. Now give another completely new test case.')
            tests_required -= 1
    end = time.time()
    with constant.PRINT_LOCK:
        print(f'[+] {folder} finished in {end - start} seconds. '
              f'Iterations: {iterations}. ',
              f'Stricly needed iterations: {constant.RETRIES}. '
              f'Tests that failed:  {failing_tests}. '
              f'Replies without tests: {replies_without_tests}. ')
