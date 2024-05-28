import ast
import glob
import json
import os
from datetime import datetime
import time
from utility import credentails
from config import constant


def get_most_recent_file(directory):
    # List all files in the directory
    files = os.listdir(directory)

    # Filter the files to match the pattern 'result_date_timestamp.json'
    result_files = [f for f in files if f.startswith('result_') and f.endswith('.json')]

    # If no matching files are found, return None
    if not result_files:
        return None

    # Extract the timestamp from the filenames and sort the files by timestamp
    result_files.sort(key=lambda x: datetime.strptime(x, 'result_%Y-%m-%d_%H-%M-%S.json'), reverse=True)

    # Construct the full path to the most recent file
    return result_files[0]


def load_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def load_or_create_json(filepath):
    # Check if the file exists
    if not os.path.exists(filepath):
        # Create the file with an empty dictionary
        with open(filepath, 'w') as file:
            json.dump({}, file)

    # Read the file and return its contents as a dictionary
    with open(filepath, 'r') as file:
        data = json.load(file)

    return data


def save_dict_to_json(dictionary, filepath):
    with open(filepath, 'w') as file:
        json.dump(dictionary, file, indent=4)


# def save_results(results, filename):
#     # Generate a filename based on the current date and time
#     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     filename_with_timestamp = f"results/{filename}_{timestamp}.json"
#
#     # Save the results to the JSON file with indentation for readability
#     with open(filename_with_timestamp, 'w') as file:
#         json.dump(results, file, indent=4)


def save_results(results):
    # Ensure the directory exists
    os.makedirs('results', exist_ok=True)

    # Generate the filename with the given number
    filename = f"results/result_{constant.ITERATION}.json"

    # Save the results to the JSON file with indentation for readability
    with open(filename, 'w') as file:
        json.dump(results, file, indent=4)


def load_results(highest_number):
    results = []
    for i in range(1, highest_number + 1):  # Assuming result files are from result_1.json to result_6.json
        filename = f'results/result_{i}.json'
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                results.append(data)
        except FileNotFoundError:
            pass  # Skip if file doesn't exist
    return results

def get_identifier(ai_model_name):
    start_index = ai_model_name.find('/')
    s = ai_model_name[start_index + 1:]
    s = s.replace('-', '_').replace('.', '_')
    return s


def get_class_names_from_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Parse the file content to an AST
    parsed_ast = ast.parse(file_content)

    # Extract class names
    class_names = [node.name for node in ast.walk(parsed_ast) if isinstance(node, ast.ClassDef)]

    return class_names


# expects tuple with (folder, file_name, model_number)
def worker(folder, class_name, selection, oracle):
    start = time.time()
    chatbot = credentails.get_chatbot()
    l = chatbot.get_remote_llms()
    ident = get_identifier(l[selection].name)
    if oracle.work_already_satisfied(folder, class_name, ident):
        print(f'[+] Work satisfied for {folder}/{class_name}')
        return
    else:
        print(f'[+] Worker active on {folder}/{class_name}/{ident}')
    chatbot.switch_llm(selection)
    with constant.PRINT_LOCK:
        print(f'[+] {folder} has switched to {l[selection].name}')
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    prompt = oracle.get_prompt(folder, class_name)

    iterations = 0
    failing_tests = 0
    replies_without_tests = 0
    # Name without extension .java, .py

    test_name = oracle.create_file(folder, class_name, ident)
    test_handle = oracle.get_test_instance(folder, class_name, test_name)
    tests_required = test_handle.get_required_tests()
    while tests_required > 0:
        iterations += 1
        with constant.PRINT_LOCK:
            print(f'[+] {folder} is on iteration {iterations}')
        response = chatbot.chat(prompt)
        time.sleep(constant.SLEEP)
        response.wait_until_done()
        print(f'[+] AI response:\n\n{response.text}')
        new_test_case = oracle.get_code(response.text)  #get_java_code(response.text)
        if new_test_case is None:
            with constant.PRINT_LOCK:
                print('[+] No test case found in reply')
            replies_without_tests += 1
            prompt = 'This did not work. Remember what i said: 1 test case, 1 assertion'
            continue
        test_handle.add_test(new_test_case)
        # test_handle.add_imports(response.text)
        try:
            test_handle.write()
        except UnicodeEncodeError:
            test_handle.remove_last_test()
            print(f'[+] Encountered Unicode char in response, trying again')
            prompt = 'no unicode character please in the test case'
            continue
        result = oracle.exec_test(folder, test_name, new_test_case)  #exec_test(folder, improved_test, new_test_case)
        if oracle.did_test_fail(result):
            with constant.PRINT_LOCK:
                print('[+] Did find a test but it failed')
            # test_handle.empty_file() # Empty the file with failing test so project can compile
            failing_tests += 1
            test_handle.remove_last_test()
            error = oracle.get_test_errors(result, test_name)
            prompt = error + "Change the test case you sent"
            continue
        else:
            with constant.PRINT_LOCK:
                print('[+] Test case found and compiles')
            prompt = 'It passed. Now give another completely new test case.'
            tests_required -= 1
    end = time.time()
    with constant.PRINT_LOCK:
        print(f'[+] {folder} finished in {(end - start)/60:.2f} minutes. '
              f'Iterations: {iterations}. ',
              f'Stricly needed iterations: {constant.RETRIES}. '
              f'Tests that failed:  {failing_tests}. '
              f'Replies without tests: {replies_without_tests}. ')
