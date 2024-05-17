import matplotlib.pyplot as plt

# Dummy data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [23, 45, 56, 78]

# Create a bar chart
plt.figure(figsize=(10, 6))  # Optional: specify the figure size
plt.bar(categories, values, color='blue')  # You can change the color as needed

# Add titles and labels
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Optionally rotate the x-axis labels if they are too long
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()  # Adjusts the plot to ensure everything fits without overlap
plt.show()
