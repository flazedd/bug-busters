#

import matplotlib.pyplot as plt
import json
import numpy as np

# Load data from JSON file
with open('results/result_2024-04-29_22-59-30.json', 'r') as file:
    data = json.load(file)
x = []
y1 = []
y2 = []


# Plotting the data for each key
for key, value in data.items():
    print(key)
    for subkey, subvalue in value.items():
        print("    ", subkey)
        x.append(subkey)
        y1.append(subvalue['Improvement']['Line coverage']['%'])
        y2.append(subvalue['Improvement']['Mutations killed']['%'])



# # Data
# x = ['A', 'B', 'C', 'D']
# y1 = [10, 20, 15, 25]
# y2 = [15, 25, 20, 30]
#
# Width of the bars
bar_width = 0.35

# Plot
fig, ax = plt.subplots()
bar1 = ax.bar(np.arange(len(x)), y1, bar_width, label='Line coverage % increase')
bar2 = ax.bar(np.arange(len(x)) + bar_width, y2, bar_width, label='Mutations killed % increase')

# Add labels, title, and legend
ax.set_xlabel('Classes under test')
ax.set_ylabel('Percentage')
ax.set_title('Test suite improvement with AI generated testcases')
ax.set_xticks(np.arange(len(x)) + bar_width / 2)
ax.set_xticklabels(x)
ax.legend()

# Show plot
plt.show()