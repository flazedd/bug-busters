import json

import utility.utils
from config import constant
from utility import utils

combined_dict = {}

all_dicts = utility.utils.load_results(6)
for d in all_dicts:
    for oracle in constant.ORACLES:
        key = oracle.__str__()
        combined_dict.setdefault(key, {})
        for tool, tool_data in d[key].items():
            combined_dict[key].setdefault(tool, {})
            for metric, value in tool_data.items():
                combined_dict[key][tool].setdefault(metric, [])
                combined_dict[key][tool][metric].append(value)
                pass

objects = {}
for oracle in constant.ORACLES:
    key = oracle.__str__()
    lists = []
    objects.setdefault(key, {})
    for tool, tool_data in combined_dict[key].items():
        for metric, value in tool_data.items():
            objects[key].setdefault(metric, {})
            if isinstance(value[0], list):
                last_values = []
                for v in value:
                    last_values.append(v[-1])
                objects[key][metric][tool] = last_values
            else:
                objects[key][metric][tool] = value




# Save dictionary to JSON file
with open('yyydata.json', 'w') as json_file:
    json.dump(objects, json_file, indent=4)

print("Data saved to data.json")