import matplotlib.pyplot as plt

# Generate list of lists with 20 increasing numbers
lists = [[i, i*2, i*3, i*4, i*5] for i in range(1, 21)]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))  # Increase the figure size

# Plot each list as a line on a graph
for i, lst in enumerate(lists):
    ax.plot(lst, label=f'Line {i+1}')

# Add labels and title
ax.set_xlabel('Index')
ax.set_ylabel('Value')
ax.set_title('Graph with 20 Lines')

# Place the legend outside the plot area
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to make room for the legend
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show the plot
plt.grid(True)
plt.show()
