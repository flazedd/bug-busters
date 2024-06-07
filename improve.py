import os
import time

from config import constant
from utility import utils

oracles = constant.ORACLES
threads = []

def change_constant(n):
    file_path = './config/constant.py'  # Renamed to avoid conflict
    modified_lines = []

    # Read the file and modify the necessary line
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('ITERATION = '):
                # print('[+] Changing line!')
                modified_lines.append(f'ITERATION = {n}\n')  # Added newline character
            else:
                modified_lines.append(line)

    # # Write the modified lines back to the file
    # with open(file_path, 'w') as wfile:
    #     wfile.writelines(modified_lines)
    with open(file_path, 'w') as wfile:
        wfile.writelines(modified_lines)
        wfile.flush()  # Ensure changes are written to disk
        os.fsync(wfile.fileno())  # Ensure changes are written to disk

runs = range(4, 7)
print(runs)
start = time.time()
print('[+] Starting...')
for run in runs:
    print(f'[+] Busy on run: {run}')
    # change_constant(number)
    for oracle in oracles:
        args = oracle.get_args()
        for arg in args:
            # print(arg)
            oracle.generate_sbst_tool(arg[0], arg[1], run)
        for arg in args:
            # pass
            utils.worker(arg[0], arg[1], arg[2], oracle, run)
    end = time.time()
    print(f'[+] Completed in {(end - start)/60:.2f} minutes')

