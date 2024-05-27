import json
import time

from utility import utils
from config import constant
from datetime import datetime
from config.constant import ORACLES

# args = utils.get_args()
# print(args)
obj: dict = {}
start = time.time()
for oracle in ORACLES:
    start_oracle = time.time()
    print(f'[+] Current oracle: {oracle}')
    key = oracle.__str__()
    obj[key] = oracle.get_dict()
    end_oracle = time.time()
    print(f'[+] Completed {key} in {(end_oracle - start_oracle) / 60:.2f} minutes')
    # for arg in oracle.get_args():
    #     print(arg)
    #     folder = arg[0]
    #     file_name = arg[1]
    #     oracle.get_dict()

# utils.save_dict_to_json(obj, './results/result.json')
utils.save_results(obj)
end = time.time()
print(f'[+] Completed in {(end - start)/60:.2f} minutes')
