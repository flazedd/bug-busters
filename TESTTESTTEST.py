import pandas as pd
import matplotlib.pyplot as plt

# Sample data in a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Plotting the table
plt.figure(figsize=(8, 3))
plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center', colWidths=[0.2, 0.1, 0.2])
plt.axis('off')  # Turn off axis
plt.show()
