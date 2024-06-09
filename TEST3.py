import matplotlib.pyplot as plt

# Generate list of lists with 5 increasing numbers
lists = [[i, i*2, i*3, i*4, i*5] for i in range(1, 21)]

# Plot each list as a line on a graph
for i, lst in enumerate(lists):
    plt.plot(lst, label=f'Line {i+1}')

# Add labels and legend
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Graph with 5 Lines')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
