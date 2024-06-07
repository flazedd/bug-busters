def change_constant(n):
    file_path = './config/constant.py'  # Renamed to avoid conflict
    modified_lines = []

    # Read the file and modify the necessary line
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('ITERATION = '):
                print('[+] Changing line!')
                modified_lines.append(f'ITERATION = {n}\n')  # Added newline character
            else:
                modified_lines.append(line)

    # Write the modified lines back to the file
    with open(file_path, 'w') as wfile:
        wfile.writelines(modified_lines)


# Example usage
change_constant(3)
