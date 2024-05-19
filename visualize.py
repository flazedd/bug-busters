import matplotlib.pyplot as plt
import json
import numpy as np
from utility import utils

recent_file = utils.get_most_recent_file('./results')
print(recent_file)
data = utils.load_json_file(f'./results/{recent_file}')
print(data)

# Dummy data
data_points = []

for main_key, sub_dict in data.items():
    for llm_key, metrics in sub_dict.items():
        average = np.mean(list(metrics.values()))
        data_points.append((llm_key, average))

# Sort the list of tuples by the second element in descending order
sorted_data = sorted(data_points, key=lambda x: x[1], reverse=True)

# Assuming sorted_data is already defined
categories = [x[0] for x in sorted_data]
values = [x[1] for x in sorted_data]

# Create a colormap from matplotlib
cmap = plt.get_cmap('coolwarm')  # You can choose other colormaps like 'plasma', 'inferno', 'magma', etc.
colors = cmap(np.linspace(0, 1, len(categories)))

# Set a maximum width for bars
max_bar_width = 0.1  # Adjust this value as needed

# Create a bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color=colors)

# # Adjust bar width if necessary
# for bar in bars:
#     bar.set_width(min(bar.get_width(), max_bar_width))

# Add titles and labels
plt.title('Average Mutation Score for Java corpus')
plt.xlabel('Approaches')
plt.ylabel('Mutation Score %')

# Optionally rotate the x-axis labels if they are too long
plt.xticks(rotation=45)

# Set the y-axis range from 0 to 100
plt.ylim(0, 100)

# Show the plot
plt.tight_layout()
plt.show()

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

