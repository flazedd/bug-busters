import json
import matplotlib.pyplot as plt

# Function to save the dictionaries into a JSON file
def save_results(results, filename):
    with open(filename, 'w') as file:
        json.dump(results, file)

# Function to load the dictionaries from a JSON file
def load_results(filename):
    with open(filename, 'r') as file:
        results = json.load(file)
    return results

# Function to visualize the data for line coverage
def visualize_line_coverage(results):
    line_coverage = [int(result['Line Coverage %']) for result in results]

    plt.figure(figsize=(10, 6))
    plt.plot(line_coverage, color='blue')
    plt.xlabel('Test Case')
    plt.ylabel('Line Coverage %')
    plt.title('Line Coverage')
    plt.grid(True)
    plt.show()

# Function to visualize the data for mutations killed
def visualize_mutations_killed(results):
    mutations_killed = [int(result['Mutations killed %']) for result in results]

    plt.figure(figsize=(10, 6))
    plt.plot(mutations_killed, color='red')
    plt.xlabel('Test Case')
    plt.ylabel('Mutations killed %')
    plt.title('Mutations Killed')
    plt.grid(True)
    plt.show()

# Example dictionaries
results = [{'Line Coverage %': '69', 'Mutations killed %': '48'},
           {'Line Coverage %': '75', 'Mutations killed %': '52'},
           {'Line Coverage %': '80', 'Mutations killed %': '55'},
           {'Line Coverage %': '85', 'Mutations killed %': '60'}]

# Save the dictionaries to a JSON file
save_results(results, 'results.json')

# Load the dictionaries from the JSON file
loaded_results = load_results('results.json')

# Visualize the data for line coverage
visualize_line_coverage(loaded_results)

# Visualize the data for mutations killed
visualize_mutations_killed(loaded_results)
