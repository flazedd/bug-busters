import os
import glob


def construct_dynamic_path(base_directory):
    # Define the initial parts of the path
    part1 = os.path.join(base_directory, "73")

    # Search for the single directory at this level
    search_pattern = os.path.join(part1, "*")
    directories = [d for d in glob.glob(search_pattern) if os.path.isdir(d)]

    # Check if there is exactly one directory
    if len(directories) != 1:
        raise Exception(f"Expected exactly one directory at {part1}, found {len(directories)}")

    # Construct the final path
    target_directory = directories[0]
    final_path = os.path.join(target_directory, "tests")
# C:\Users\reini\Downloads\results\results\default120\73\osa_ora_server_utils_StringEncoder64\tests\1\osa\ora\server\utils\StringEncoder64_ESTest.java
    return final_path


# Example usage
base_directory = r'C:\Users\reini\Downloads\results\results\default120'
try:
    constructed_path = construct_dynamic_path(base_directory)
    print(f"Constructed path: {constructed_path}")
except Exception as e:
    print(e)
