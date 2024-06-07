import json

# Define the filenames
filenames = ['result_1.json', 'result_2.json']


def calculate_average_score(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

        # Navigate to the scores
        scores = data["Python"]["Pynguin"]

        # Calculate the average score
        average_score = sum(scores.values()) / len(scores)

        return average_score


# Calculate and print the average scores for each file
for filename in filenames:
    average_score = calculate_average_score(filename)
    print(f"Average score for {filename}: {average_score:.2f}")
