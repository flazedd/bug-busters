import matplotlib.pyplot as plt
import json
import numpy as np

from config import constant
from utility import utils

utils.compute_combined_results()

with open(f'./results/combined.json', 'r') as json_file:
    combined_dict = json.load(json_file)

for oracle in constant.ORACLES:
    categories = []
    values = []
    key = oracle.__str__()
    for tool, data in combined_dict[key].items():
        values_per_class = []
        for project_class, lists in data.items():
            if tool == "Meta_Llama_3_70B_Instruct":
                arr = np.array(lists)
                average = np.average(arr, axis=0)[-1]
                # print(f'avg is {average}')
                values_per_class.append(average)
            else:
                average = np.average(lists)
                values_per_class.append(average)
                # print(f'avg is {average}')
        categories.append(tool)
        tg = np.average(values_per_class)
        values.append(tg)
    print(categories)
    print(values)
    # Create the bar chart
    plt.bar(categories, values, color=[(1, 0.8, 0.8, 1), 'lightgreen'])

    # Add title and labels
    plt.title(f'Average mutation score over all {key} classes over all runs')
    plt.xlabel('Test generation method')
    plt.ylabel('Mutation score %')

    # Show the bar chart
    plt.show()

# for main_key, sub_dict in data.items():
#     one_time = True
#     data_points = []
#     for llm_key, metrics in sub_dict.items():
#         if one_time:
#             one_time = False
#         else:
#             lists = []
#             for test_class, list_values in metrics.items():
#                 lists.append(list_values)
#             transposed = list(zip(*lists))
#             averaged_list = [np.mean(position) for position in transposed]
#             data_points.append(averaged_list)
#     # Plotting the data
#     plt.figure(figsize=(10, 6))
#
#     for i, averaged_list in enumerate(data_points):
#         x = list(range(len(averaged_list)))
#         y = averaged_list
#         plt.plot(x, y, label=f'{llm_key}')
#     plt.xticks(ticks=range(len(data_points[0])))
#     plt.xlabel('Amount of tests enabled')
#     plt.ylabel('Average Mutation Score')
#     plt.title(f'{main_key} corpus Increase in Mutation Score over tests added')
#     plt.legend()
#     # plt.ylim(0, 100)
#     plt.grid(True)
#     plt.show()
#
#
#
# for main_key, sub_dict in data.items():
#     one_time = True
#     data_points = []
#     for llm_key, metrics in sub_dict.items():
#         if one_time:
#             average = np.mean(list(metrics.values()))
#             data_points.append((llm_key, average))
#             one_time = False
#         else:
#             average = 0
#             for test_class, list_values in metrics.items():
#                 average += list_values[-1]
#             average /= len(metrics)
#             data_points.append((llm_key, average))
#     # sorted_data = sorted(data_points, key=lambda x: x[1], reverse=True)
#     sorted_data = data_points
#     categories = [x[0] for x in sorted_data]
#     values = [x[1] for x in sorted_data]
#     cmap = plt.get_cmap('coolwarm')  # You can choose other colormaps like 'plasma', 'inferno', 'magma', etc.
#     colors = cmap(np.linspace(0, 1, len(categories)))
#     max_bar_width = 0.1  # Adjust this value as needed
#     plt.figure(figsize=(10, 6))
#     bars = plt.bar(categories, values, color=colors)
#     plt.title(f'Average Mutation Score for {main_key} corpus')
#     plt.xlabel('Approaches')
#     plt.ylabel('Mutation Score %')
#     plt.xticks(rotation=45)
#     # plt.ylim(0, 100)
#     plt.tight_layout()
#     plt.show()

# import json
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Your JSON data as a Python dictionary
# data = {
#     "Java": {
#         "Meta_Llama_3_70B_Instruct": {
#             "Directors": [0, 6, 12, 18, 20, 21, 22, 23],
#             "AbstractNFeAdaptadorBean": [0, 30, 60, 90, 92, 93, 94, 94],
#             "OpMatcher": [0, 10, 20, 30, 31, 31, 31, 31],
#             "Contract": [0, 18, 36, 54, 55, 55, 55, 56],
#             "Util": [0, 8, 16, 24, 24, 24, 25, 25]
#         },
#         "Evosuite": {
#             "Directors": [0, 6, 12, 15, 15, 15, 16, 16],
#             "AbstractNFeAdaptadorBean": [0, 20, 40, 56, 56, 56, 56, 56],
#             "OpMatcher": [0, 14, 28, 42, 44, 46, 48, 49],
#             "Contract": [0, 4, 8, 10, 10, 11, 11, 12],
#             "Util": [0, 16, 32, 40, 40, 40, 40, 40]
#         }
#     }
# }
#
#
# # Extract the arrays for Meta_Llama_3_70B_Instruct and Evosuite
# meta_llama_arrays = list(data["Java"]["Meta_Llama_3_70B_Instruct"].values())
# evosuite_arrays = list(data["Java"]["Evosuite"].values())
#
# # Calculate the averages for each position in the arrays
# meta_llama_averages = np.mean(meta_llama_arrays, axis=0)
# evosuite_averages = np.mean(evosuite_arrays, axis=0)
#
# # Plot the results
# x = np.arange(0, 8)  # X-axis labels
#
# plt.figure(figsize=(10, 6))
# plt.plot(x, meta_llama_averages, marker='o', label='Meta_Llama_3_70B_Instruct')
# plt.plot(x, evosuite_averages, marker='s', label='Evosuite')
#
# plt.xlabel('Amount of tests generated')
# plt.ylabel('Average Mutation Score in %')
# plt.title('Mutation score improvement over amount of tests')
# plt.legend()
# plt.grid(True)
#
# plt.show()

