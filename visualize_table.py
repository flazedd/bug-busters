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


for key, value in combined_dict['Python']['Meta_Llama_3_70B_Instruct'].items():
    for kk in value:
        nx = len(kk)
        if nx != 9:
            print(key)
            print(value)
            print(kk)
        # print(len(list))


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
# Adjust pandas display options globally
pd.set_option('display.max_columns', None)
with open(f'Mdumpdata.json', 'w') as json_file:
    json.dump(objects, json_file, indent=4)
for oracle in constant.ORACLES:
    data = {}
    key = oracle.__str__()
    for class_name, value in objects[key].items():
        groups = []
        project_name = class_name.split('.')[0]
        c_name = class_name.split('.')[1]
        project_column = 'Project'
        data.setdefault(project_column, [])
        data[project_column].append(project_name)
        class_column = 'Class'
        data.setdefault(class_column, [])
        data[class_column].append(c_name)
        for tool, tool_data in value.items():
            ndv = tool_data
            name = f'{tool}\n Median Mutation Score'
            data.setdefault(name, [])
            data[name].append(round(np.median(ndv), 4))
            groups.append(ndv)
        wilcox_column = 'p-value\nWilcoxon'
        g1, g2 = utils.adjust_for_zero_differences(groups[0], groups[1])
        wilcox_stat, wilcox_p = wilcoxon(g1, g2)
        data.setdefault(wilcox_column, [])
        data[wilcox_column].append(round(wilcox_p, 4))
        vargha_column = 'Vargha-Delaney\neffect size'
        # vd_a = utils.vargha_delaney_effect_size(g1, g2)
        estimate, magnitude = utils.VD_A(g1, g2)
        single_letter = utils.transform_string(magnitude)
        data.setdefault(vargha_column, [])
        # formatted_vd_a = utils.categorize(round(vd_a, 4))
        data[vargha_column].append(f'{single_letter} ({round(estimate, 4)})')

    # Save dictionary to JSON file
    with open(f'{tool} data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    # print("Data saved to data.json")
    df = pd.DataFrame(data)
    # Set the figure size
    plt.figure(figsize=(25, 10))  # Adjust the width and height as needed

    # Create a subplot without frame and axes
    ax = plt.subplot(111, frame_on=False)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    # Plot the table with a specified font size
    table = pd.plotting.table(ax, df, loc='center', fontsize=12)


    # Auto-adjust column widths
    def auto_adjust_column_widths(table, df):
        cell_texts = df.astype(str).values
        cell_lengths = [[len(text) for text in row] for row in cell_texts]
        col_widths = [max(lengths) for lengths in zip(*cell_lengths)]

        for i, col_width in enumerate(col_widths):
            table.auto_set_column_width(i)
            for j in range(len(df)):
                cell = table[(j + 1, i)]
                cell.set_width(col_width * 0.1)  # Adjust the factor as needed


    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(2.5, 1.5)
    for (i, j), cell in table.get_celld().items():
        if i == 0:  # Header row
            cell.set_text_props(fontsize=12)  # Set header text size
            cell.set_height(0.1)  # Adjust header height as needed
    auto_adjust_column_widths(table, df)

    # Color cells green if value exceeds 0.05
    for i in range(len(df)):
        for j in range(len(df.columns)):
            cell_val = df.iloc[i, j]
            col_name = df.columns[j]
            if 'p-value' in col_name and isinstance(cell_val, (int, float)) and 0.0 <= cell_val < 0.05:
                cell = table[(i + 1, j)]
                e_cell = table[(i + 1, j + 1)]
                e_val = df.iloc[i, j + 1]
                e_val = utils.extract_number_from_brackets(e_val)
                if e_val < 0.5:
                    cell.set_facecolor('lightgreen')
                    e_cell.set_facecolor('lightgreen')
                elif e_val > 0.5:
                    cell.set_facecolor((1, 0.8, 0.8, 1))
                    e_cell.set_facecolor((1, 0.8, 0.8, 1))


    plt.show()
