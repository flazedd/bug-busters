import radon
from radon.complexity import cc_visit, cc_rank

from config import constant

def compute_mccabe_complexity(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
    try:
        complexity = cc_visit(code)
        lines_of_code = code.count('\n') + 1
        average_complexity = sum([block.complexity for block in complexity]) / len(complexity)
        highest_complexity = max([block.complexity for block in complexity])
        return lines_of_code, average_complexity, highest_complexity
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
            loc, mccabe_complexity, highest_complexity = compute_mccabe_complexity(file_path)
            if mccabe_complexity is not None:
                # print("McCabe's complexity:", mccabe_complexity)
                print(f'arg: {arg}, highest_mccabe_complexity: {highest_complexity} loc: {loc}')
                # print("Highest McCabe's complexity:", highest_complexity)
                # print("LOC:", loc)



file_path = './PythonPUT/docstring_parser/common.py'  # Change this to the path of your Python file

