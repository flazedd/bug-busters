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

combined_dict = combined_dict['Python']['Pynguin']

d30 = {}
for key, value in combined_dict.items():
    median_value = statistics.median(value)
    d30[key] = median_value

with open(f'./results/result_8.json', 'r') as json_file:
    d60 = json.load(json_file)

d60 = d60['Python']['Pynguin']


with open(f'./results/result_7.json', 'r') as json_file:
    d90 = json.load(json_file)

d90 = d90['Python']['Pynguin']


d_all = {}
for d in [d30, d60, d90]:
    for key, value in d.items():
        if key in d_all:
            d_all[key].append(value)
        else:
            d_all[key] = [value]

with open(f'd_all.json', 'w') as json_file:
    json.dump(d_all, json_file, indent=4)
#
# # Iterate through the nested dictionary
data = {}
for project_class, list_values in d_all.items():

    project_name = project_class.split('.')[0]
    project_column = 'Project'
    data.setdefault(project_column, [])
    data[project_column].append(project_name)

    c_name = project_class.split('.')[1]
    class_column = 'Class'
    data.setdefault(class_column, [])
    data[class_column].append(c_name)

    pynguin30s_column = 'Pynguin 30s\nMedian Mutation Score'
    data.setdefault(pynguin30s_column, [])
    data[pynguin30s_column].append(round(list_values[0], 4))

    pynguin30s_column = 'Pynguin 60s\nMutation Score'
    data.setdefault(pynguin30s_column, [])
    data[pynguin30s_column].append(round(list_values[1], 4))

    pynguin30s_column = 'Pynguin 90s\nMutation Score'
    data.setdefault(pynguin30s_column, [])
    data[pynguin30s_column].append(round(list_values[2], 4))

    # print(f"The median value for '{project_class}' is: {median_value}")

df = pd.DataFrame(data)
# Set the figure size
plt.figure(figsize=(10, 8))  # Adjust the width and height as needed

# Create a subplot without frame and axes
ax = plt.subplot(111, frame_on=False)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Plot the table with a specified font size
table = pd.plotting.table(ax, df, loc='center', fontsize=12)


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
    val_30s = df.iloc[i, 2]
    val_60s = df.iloc[i, 3]
    val_90s = df.iloc[i, 4]
    if val_30s == max(val_30s, val_60s, val_90s):
        cell = table[(i + 1, 2)]
        cell.set_facecolor('lightgreen')
    if val_60s == max(val_30s, val_60s, val_90s):
        cell = table[(i + 1, 3)]
        cell.set_facecolor('lightgreen')
    if val_90s == max(val_30s, val_60s, val_90s):
        cell = table[(i + 1, 4)]
        cell.set_facecolor('lightgreen')

plt.show()