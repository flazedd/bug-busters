import json

# Loop through the JSON files 1.json to 6.json
for i in range(1, 7):
    # Read the JSON file
    with open(f'./results/result_{i}.json', 'r') as infile:
        data = json.load(infile)

    # Extract the value for dict['Java']['EvoSuite']
    evo_suite_data = data['Java']['EvoSuite']

    # Prepare the output dictionary
    output_data = {'EvoSuite': evo_suite_data}

    # Write the extracted data to a new JSON file
    with open(f'./results/evosuite_run_{i}.json', 'w') as outfile:
        json.dump(evo_suite_data, outfile, indent=4)

print("Extraction and writing completed successfully.")
