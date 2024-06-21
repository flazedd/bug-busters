import ast

import radon
from radon.complexity import cc_visit, cc_rank

from config import constant

def compute_mccabe_complexity(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
    try:
        complexity = cc_visit(code)
        lines_of_code = code.count('\n') + 1
        total_compl = sum([block.complexity for block in complexity])
        highest_complexity = max([block.complexity for block in complexity])

        # Parse the code and count the number of function definitions
        tree = ast.parse(code)
        function_count = sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree))


        return lines_of_code, total_compl, highest_complexity, function_count
    except Exception as e:
        print("Error:", e)
        return None

for oracle in constant.ORACLES:
    if oracle.__str__() == 'Python':
        args = oracle.get_args()
        for arg in args:
            project = arg[0]
            class_name = arg[1]
            file_path = f'./PythonPUT/{project}/{class_name}.py'
            loc, total_compl, highest_complexity, function_count = compute_mccabe_complexity(file_path)
            if total_compl is not None:
                name = file_path.rsplit('/', 1)[-1].rsplit('.', 1)[0]
                formatted_string = (
                    f"name: {name:<20} total cc: {total_compl:<10} "
                    f"largest cc: {highest_complexity:<10} method count: {function_count:<10} loc: {loc:<10}"
                )
                print(formatted_string)
                # print(f'name: {arg[0]}.{arg[1]} total cc: {total_compl} largest cc: {highest_complexity} method count: {function_count} loc: {loc} ')
                # print("Total CC:", total_compl)
                # print(f'arg: {arg}, highest_mccabe_complexity: {highest_complexity} loc: {loc}')
                # print("Highest McCabe's complexity:", highest_complexity)
                # print("LOC:", loc)



file_path = './PythonPUT/docstring_parser/common.py'  # Change this to the path of your Python file

