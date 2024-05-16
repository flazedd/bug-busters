def print_first_three_words(file_path):
    with open(file_path, 'r') as file:
        # Read the file
        content = file.read()

        # Extract the first three words
        first_three_words = ' '.join(content.split()[:3])
        print(first_three_words)

# File path
file_path = "../JavaProgramUnderTest/lib/src/main/java/templateit_5/OpMatcher.java"

# Print the first three words
print_first_three_words(file_path)
