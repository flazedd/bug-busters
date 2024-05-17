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
plt.title('Average Mutation Score Achieved per Model')
plt.xlabel('Categories')
plt.ylabel('Mutation Score Percentage')

# Optionally rotate the x-axis labels if they are too long
plt.xticks(rotation=45)

# Set the y-axis range from 0 to 100
plt.ylim(0, 100)

# Show the plot
plt.tight_layout()
plt.show()
