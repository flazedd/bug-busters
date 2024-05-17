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

print(f'data points: {data_points}')
print(f'sorted data points: {sorted_data}')

categories = [x[0] for x in sorted_data]
values = [x[1] for x in sorted_data]

# Create a bar chart
plt.figure(figsize=(10, 6))  # Optional: specify the figure size
plt.bar(categories, values, color='blue')  # You can change the color as needed

# Add titles and labels
plt.title('Averge mutation score achieved per model')
plt.xlabel('Categories')
plt.ylabel('Mutation score percentage')

# Optionally rotate the x-axis labels if they are too long
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()  # Adjusts the plot to ensure everything fits without overlap
plt.show()

