import json
from scipy import stats
import pandas as pd
from matplotlib import pyplot as plt
import statistics
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

# Sample data in a DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'City': ['New York', 'Los Angeles', 'Chicago']}


for oracle in constant.ORACLES:
    data = {}
    key = oracle.__str__()
    for class_name, value in objects[key].items():
        sbst_name = value.keys()[0]
        llm_name = value.keys()[1]
        class_column = 'Class'
        sbst_column = f'{sbst_name} Median Mutation Score'
        llm_column = f'{llm_name} Median Mutation Score'
        p_column = 'p-value Mann-Whitney U'
        data.setdefault(class_column, [])
        data.setdefault(sbst_column, [])
        data.setdefault(llm_column, [])
        data.setdefault(p_value, [])
        data[class_column].append(class_name)
        group1 = value.values()[0]
        group2 = value.values()[1]
        sbst_median = statistics.mean(group1)
        llm_median = statistics.mean(group2)
        data[sbst_column].append(sbst_median)
        data[llm_column].append(llm_median)
        u_statistic, p_value = stats.mannwhitneyu(group1, group2)
        data[p_column].append(p_value)
    df = pd.DataFrame(data)
    # Plotting the table
    plt.figure(figsize=(8, 3))
    plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center', colWidths=[0.2, 0.1, 0.2])
    plt.axis('off')  # Turn off axis
    plt.show()

# # Save dictionary to JSON file
# with open('yyydata.json', 'w') as json_file:
#     json.dump(objects, json_file, indent=4)
#
# print("Data saved to data.json")
