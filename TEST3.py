import numpy as np

# Sample list of lists
list_of_lists = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Convert the list of lists to a numpy array
array = np.array(list_of_lists)

# Flatten the array to a 1D list and calculate the average
average_value = np.average(array[0])

print("Average value:", average_value)
