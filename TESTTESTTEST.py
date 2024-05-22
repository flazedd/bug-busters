import ast

def extract_first_function_code(code):
    # Parse the code into an Abstract Syntax Tree (AST)
    tree = ast.parse(code)

    # Iterate through the nodes in the tree
    for node in ast.walk(tree):
        # Check if the node is a function definition
        if isinstance(node, ast.FunctionDef):
            # Get the source code of the function
            function_code = ast.unparse(node)
            return function_code.strip()

    # If no function definition is found, return None
    return None

# Example usage
if __name__ == "__main__":
    # Example Python code
    code = """
def function1():
    pass

def function2():
    pass

def function3():
    pass
"""

    # Extract the code of the first function definition
    first_function_code = extract_first_function_code(code)

    if first_function_code:
        print("First function code:")
        print(first_function_code)
    else:
        print("No function definition found in the code.")
