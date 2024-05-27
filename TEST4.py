import pandas as pd
import matplotlib.pyplot as plt
import statistics
from scipy import stats
from tabulate import tabulate

# Sample structure of objects, replace this with your actual data
objects = {
    'oracle1': {
        'classA': {
            'tool1': [1.2, 3.4, 2.5],
            'tool2': [2.3, 3.7, 1.8]
        },
        'classB': {
            'tool1': [1.0, 3.2, 2.8],
            'tool2': [2.5, 3.5, 2.0]
        }
    },
    'oracle2': {
        'classA': {
            'tool1': [1.3, 3.3, 2.7],
            'tool2': [2.1, 3.9, 1.9]
        },
        'classB': {
            'tool1': [1.1, 3.0, 2.9],
            'tool2': [2.4, 3.6, 2.1]
        }
    }
}

# Replace constant.ORACLES with actual list of oracles
constant = type('constant', (object,), {})()
constant.ORACLES = ['oracle1', 'oracle2']

for oracle in constant.ORACLES:
    data = {}
    key = oracle.__str__()
    for class_name, value in objects[key].items():
        groups = []
        class_column = 'Class'
        data.setdefault(class_column, [])
        data[class_column].append(class_name)
        for tool, tool_data in value.items():
            name = f'{tool} Median Mutation Score'
            data.setdefault(name, [])
            data[name].append(statistics.mean(tool_data))
            groups.append(tool_data)
        p_column = 'p-value Mann-Whitney U'
        u_statistic, p_value = stats.mannwhitneyu(groups[0], groups[1])
        data.setdefault(p_column, [])
        data[p_column].append(p_value)
    df = pd.DataFrame(data)
    # Set the figure size
    plt.figure(figsize=(10, 5))  # Adjust the width and height as needed

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


    auto_adjust_column_widths(table, df)

    plt.show()
    # # Print the DataFrame as a fancy table using tabulate
    # table_str = tabulate(df, headers='keys', tablefmt='fancy_grid')
    # print(table_str)
    #
    # # Plotting the table using matplotlib
    # fig, ax = plt.subplots(figsize=(12, 6))  # Adjust figure size as needed
    # ax.axis('tight')
    # ax.axis('off')
    #
    # table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    # table.auto_set_font_size(False)
    # table.set_fontsize(12)
    # table.auto_set_column_width(col=list(range(len(df.columns))))  # Automatically set column widths
    # # Set row heights
    # row_height = 0.1  # Adjust this value as needed
    # for i in range(len(df)):
    #     table[i, -1].set_height(row_height)
    # for j in range(len(df.columns)):
    #     table[0, j].set_height(row_height)
    plt.show()
