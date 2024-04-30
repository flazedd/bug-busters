import json
from datetime import datetime
import os

def save_results(results, filename):
    # Create the results directory if it doesn't exist
    os.makedirs("results", exist_ok=True)

    # Generate a filename based on the current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename_with_timestamp = f"results/{filename}_{timestamp}.json"

    # Save the results to the JSON file with indentation for readability
    with open(filename_with_timestamp, 'w') as file:
        json.dump(results, file, indent=4)

# Example usage
results = [{"Line Coverage %": "69", "Mutations killed %": "48"},
           {"Line Coverage %": "75", "Mutations killed %": "52"},
           {"Line Coverage %": "80", "Mutations killed %": "55"},
           {"Line Coverage %": "85", "Mutations killed %": "60"}]

save_results(results, "results")
