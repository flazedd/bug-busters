import os

# Define the directory path
directory = './PythonPUT'
iteration = 0
# Iterate over each folder in the directory
for folder_name in os.listdir(directory):
    folder_path = os.path.join(directory, folder_name)
    if os.path.isdir(folder_path):
        # Iterate over each file in the folder
        for file_name in os.listdir(folder_path):
            if (not file_name.startswith('test__')) and file_name.endswith('8.py'):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    # Delete the file
                    # os.remove(file_path)
                    iteration += 1
                    print(f"[{iteration}] Will delete file: {file_path}")

                # else:
                #     print(f"Not a file: {file_path}")
    else:
        print(f"Not a directory: {folder_path}")
