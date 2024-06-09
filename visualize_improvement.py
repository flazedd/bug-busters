import json

import numpy as np
from scipy import stats
import pandas as pd
from matplotlib import pyplot as plt
import statistics
import utility.utils
from config import constant
from utility import utils
from scipy.stats import wilcoxon


utils.compute_combined_results()

with open(f'./results/combined.json', 'r') as json_file:
    combined_dict = json.load(json_file)

# combined_dict = combined_dict['Python']['Pynguin']

for oracle in constant.ORACLES:
    data = {}
    key = oracle.__str__()
    counter = 0
    fig, ax = plt.subplots(figsize=(10, 6))
    for project_class, nested_lists in combined_dict[key]["Meta_Llama_3_70B_Instruct"].items():
        counter += 1
        arr = np.array(nested_lists)
        medians = np.median(arr, axis=0)
        lst = medians.tolist()
        c_name = project_class.split('.')[1]
        plt.plot(lst, label=f'{c_name}')
        if counter % 10 == 0:
            # Add labels and legend
            plt.xlabel('Index')
            plt.ylabel('Value')
            part = 'first' if counter < 12 else 'last'
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            ax.set_title(f'{key} corpus {part} 10 classes')
            ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.tight_layout(rect=[0, 0, 0.85, 1])
            plt.grid(True)
            plt.show()
            fig, ax = plt.subplots(figsize=(10, 6))