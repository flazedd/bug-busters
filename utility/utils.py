import ast
import glob
import json
import os
from datetime import datetime
import time
from typing import List

from utility import credentails
from config import constant
import numpy as np
from scipy.stats import rankdata
from bisect import bisect_left
from typing import List
import scipy.stats as ss


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


def save_results(results, run):
    # Ensure the directory exists
    os.makedirs('results', exist_ok=True)

    # Generate the filename with the given number
    filename = f"results/result_{run}.json"

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
            print(f'[+] File {filename} not found')
            pass  # Skip if file doesn't exist
    return results


# def adjust_for_zero_differences(list1, list2, epsilon=1e-10):
#     """
#     Adjust the elements of list2 by adding a small epsilon value if the difference between corresponding elements of list1 and list2 is zero.
#
#     Parameters:
#     list1 (list): The first list of values.
#     list2 (list): The second list of values.
#     epsilon (float): The small value to add to elements in list2 if the difference is zero (default is 1e-10).
#
#     Returns:
#     tuple: Two lists, the original list1 and the adjusted list2.
#     """
#     if len(list1) != len(list2):
#         raise ValueError("Both lists must have the same length.")
#
#     adjusted_list2 = [
#         val2 + epsilon if val1 == val2 else val2
#         for val1, val2 in zip(list1, list2)
#     ]
#
#     return list1, adjusted_list2
def extract_number_from_brackets(string):
    # Find the positions of the opening and closing brackets
    start = string.find('(')
    end = string.find(')')

    # Check if both brackets are found and are in the correct order
    if start != -1 and end != -1 and start < end:
        try:
            # Extract the substring containing the number
            number_str = string[start + 1:end]
            # Convert the extracted substring to a float and return it
            return float(number_str)
        except ValueError:
            return "Invalid format: content inside brackets is not a float"
    else:
        return "Invalid format: brackets not found or incorrect order"


# Test cases
print(extract_number_from_brackets("M (0.7)"))  # Should return 0.7
print(extract_number_from_brackets("L (0.2)"))  #


def VD_A(treatment: List[float], control: List[float]):
    """
    Computes Vargha and Delaney A index
    A. Vargha and H. D. Delaney.
    A critique and improvement of the CL common language
    effect size statistics of McGraw and Wong.
    Journal of Educational and Behavioral Statistics, 25(2):101-132, 2000
    The formula to compute A has been transformed to minimize accuracy errors
    See: http://mtorchiano.wordpress.com/2014/05/19/effect-size-of-r-precision/
    :param treatment: a numeric list
    :param control: another numeric list
    :returns the value estimate and the magnitude
    """
    m = len(treatment)
    n = len(control)

    if m != n:
        raise ValueError("Data d and f must have the same length")

    r = ss.rankdata(treatment + control)
    r1 = sum(r[0:m])

    # Compute the measure
    # A = (r1/m - (m+1)/2)/n # formula (14) in Vargha and Delaney, 2000
    A = (2 * r1 - m * (m + 1)) / (2 * n * m)  # equivalent formula to avoid accuracy errors

    levels = [0.147, 0.33, 0.474]  # effect sizes from Hess and Kromrey, 2004
    magnitude = ["negligible", "small", "medium", "large"]
    scaled_A = (A - 0.5) * 2

    magnitude = magnitude[bisect_left(levels, abs(scaled_A))]
    estimate = A

    return estimate, magnitude

def transform_string(input_str):
    if input_str == "negligible":
        return "-"
    else:
        return input_str[0].upper()

# def categorize(x):
#     if (0 <= x <= 0.25) or (0.75 <= x <= 1.00):
#         return f"L ({x})"
#     elif (0.25 < x <= 0.35) or (0.65 <= x < 0.75):
#         return f"M ({x})"
#     elif (0.35 < x <= 0.45) or (0.55 <= x < 0.65):
#         return f"S ({x})"
#     else:
#         return f"- ({x})"


def adjust_for_zero_differences(list1, list2, epsilon=1e-10):
    """
    Adjust the elements of list1 and list2 by adding a small epsilon value if the difference between corresponding elements of list1 and list2 is zero.
    Alternates between adding epsilon to val1 and val2.

    Parameters:
    list1 (list): The first list of values.
    list2 (list): The second list of values.
    epsilon (float): The small value to add to elements in list1 and list2 if the difference is zero (default is 1e-10).

    Returns:
    tuple: Two lists, the adjusted list1 and the adjusted list2.
    """
    if len(list1) != len(list2):
        print(f'List1 is: {list1} with length {len(list1)}')
        print(f'List2 is: {list2} with length {len(list2)}')
        raise ValueError("Both lists must have the same length.")

    adjusted_list1 = []
    adjusted_list2 = []

    add_to_val1 = True  # Start by adding epsilon to val1

    for val1, val2 in zip(list1, list2):
        if val1 == val2:
            if add_to_val1:
                adjusted_list1.append(val1 + epsilon)
                adjusted_list2.append(val2)
            else:
                adjusted_list1.append(val1)
                adjusted_list2.append(val2 + epsilon)
            add_to_val1 = not add_to_val1  # Alternate adding epsilon to val1 and val2
        else:
            adjusted_list1.append(val1)
            adjusted_list2.append(val2)

    return adjusted_list1, adjusted_list2


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


def compute_combined_results() -> None:
    combined_dict = {}

    all_dicts = load_results(12)
    for d in all_dicts:
        for oracle in constant.ORACLES:
            key = oracle.__str__()
            combined_dict.setdefault(key, {})
            for tool, tool_data in d[key].items():
                combined_dict[key].setdefault(tool, {})
                for metric, value in tool_data.items():
                    combined_dict[key][tool].setdefault(metric, [])
                    combined_dict[key][tool][metric].append(value)

    with open(f'./results/combined.json', 'w') as json_file:
        json.dump(combined_dict, json_file, indent=4)


# def vargha_delaney_effect_size(x: List, y: List) -> float:
#     """
#     Calculate the Vargha-Delaney A effect size.
#     """
#     m = len(x)
#     n = len(y)
#     r = rankdata(np.concatenate([x, y]))
#     r1 = np.sum(r[:m])
#     A = (r1 / m - (m + 1) / 2) / n
#     return A


# expects tuple with (folder, file_name, model_number)
def worker(folder, class_name, selection, oracle, run):
    start = time.time()
    chatbot = credentails.get_chatbot()
    l = chatbot.get_remote_llms()
    ident = get_identifier(l[selection].name)
    if oracle.work_already_satisfied(folder, class_name, ident, run):
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

    test_name = oracle.create_file(folder, class_name, ident, run)
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
        print(f'[+] {folder} finished in {(end - start) / 60:.2f} minutes. '
              f'Iterations: {iterations}. ',
              f'Stricly needed iterations: {constant.RETRIES}. '
              f'Tests that failed:  {failing_tests}. '
              f'Replies without tests: {replies_without_tests}. ')
