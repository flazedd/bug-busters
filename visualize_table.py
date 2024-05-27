import json

import numpy as np
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
# Adjust pandas display options globally
pd.set_option('display.max_columns', None)

for oracle in constant.ORACLES:
    data = {}
    key = oracle.__str__()
    for class_name, value in objects[key].items():
        groups = []
        class_column = 'Class'
        data.setdefault(class_column, [])
        data[class_column].append(class_name)
        for tool, tool_data in value.items():
            ndv = np.array(tool_data)
            name = f'{tool}\n Median Mutation Score'
            data.setdefault(name, [])
            data[name].append(statistics.mean(ndv))
            groups.append(ndv)
            shapiro_stat, shapiro_p = stats.shapiro(ndv)
            shap_name = f'{tool}\np-value Shapiro-Wilk'
            data.setdefault(shap_name, [])
            data[shap_name].append(round(shapiro_p, 4))
            # ndv = np.array(tool_data)
            ks_stat, ks_p = stats.kstest(ndv, 'norm', args=(np.mean(ndv), np.std(ndv)))
            ks_name = f'{tool}\np-value Kolmogorov-Smirnov'
            data.setdefault(ks_name, [])
            data[ks_name].append(round(ks_p, 4))
        levene_column = 'p-value\nLevene'
        levene_stat, levene_p = stats.levene(groups[0], groups[1])
        data.setdefault(levene_column, [])
        data[levene_column].append(round(levene_p, 4))
        t_column = 'p-value\nt-test'
        t_statistic, tp_value = stats.ttest_ind(groups[0], groups[1])
        data.setdefault(t_column, [])
        data[t_column].append(round(tp_value, 4))
        p_column = 'p-value\nMann-Whitney U'
        u_statistic, p_value = stats.mannwhitneyu(groups[0], groups[1])
        data.setdefault(p_column, [])
        data[p_column].append(round(p_value, 4))
    # Save dictionary to JSON file
    with open('hhhdata.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("Data saved to data.json")
    df = pd.DataFrame(data)
    # Set the figure size
    plt.figure(figsize=(25, 5))  # Adjust the width and height as needed

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
            cell.set_height(0.2)  # Adjust header height as needed
    auto_adjust_column_widths(table, df)

    # Color cells green if value exceeds 0.05
    for i in range(len(df)):
        for j in range(len(df.columns)):
            cell_val = df.iloc[i, j]
            if isinstance(cell_val, (int, float)) and 0.05 < cell_val <= 1:
                cell = table[(i + 1, j)]
                cell.set_facecolor('lightgreen')

    plt.show()

# # Save dictionary to JSON file
# with open('yyydata.json', 'w') as json_file:
#     json.dump(objects, json_file, indent=4)
#
# print("Data saved to data.json")
