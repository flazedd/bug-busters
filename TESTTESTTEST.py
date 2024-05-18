import subprocess
import os


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

print(exec_mutpy('codetiming', '_timers', 'test__timers'))
