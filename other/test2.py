import matplotlib.pyplot as plt
import numpy as np

data = {
    "Java": {
        "Meta": {
            "Directors": 29,
            "OpMatcher": 31,
            "Contract": 56,
            "Util": 0
        },
        "Phi": {
            "Directors": 0,
            "OpMatcher": 24
        },
        "c4ai": {
            "OpMatcher": 28
        },
        "gemma": {
            "OpMatcher": 31
        },
        "Mistral": {
            "OpMatcher": 41
        },
        "Mixtral": {
            "OpMatcher": 24
        },
        "Nous": {
            "OpMatcher": 0
        },
        "Yi": {
            "OpMatcher": 0
        },
        "zephyr": {
            "OpMatcher": 0
        }
    }
}
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

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color=colors)

# Add titles and labels
plt.title('Average Mutation Score Achieved per Model')
plt.xlabel('Categories')
plt.ylabel('Mutation Score Percentage')

# Optionally rotate the x-axis labels if they are too long
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
