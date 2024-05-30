import glob
import os

from config import constant

oracles = constant.ORACLES


# args = [('templateit_5', 'OpMatcher', 1)]

# Define the directory components
dir_components = []

# Construct the path
# base_dir = os.path.join("C:", "Users", "reini", "Downloads", "results", "results", "default120")
base_dir = r'C:\Users\reini\Downloads\results\results\default120'
def gen_es_tests(folder, class_name):
    for i in range(1, 9):
        num = folder.split('_')[1]
        path = os.path.join(base_dir, num)
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                target = os.path.join(item_path, 'tests', str(i), '**', f'{class_name}_ESTest.java')
                # print(f"Target: {target}")
                matching_files = glob.glob(target, recursive=True)
                for file_path in matching_files:
                    # print(f"[+] Found file: {file_path}")
                    wr = './JavaProgramUnderTest/lib/src/test/java/' + folder + '/' + f'{class_name}_ESTest_{i}.java'
                    if not os.path.exists(wr):
                        with open(wr, 'w') as f:
                            pass
                        print(f'[+] Created: {wr}')
                    elif os.path.getsize(wr) > 0:
                        print(f'[+] Work satisfied for: {wr}')
                        break
                    else:
                        print(f'[+] Already exists but empty: {wr}')
                    with open(file_path, 'r') as f:
                        # content = f.read()
                        test_seen = False
                        modified_content = [f'package {folder};\n',
                                            f'import static org.junit.jupiter.api.Assertions.*;\n',
                                            f'import org.junit.jupiter.api.Test;\n\n',
                                            f'public class {class_name}_ESTest_{i} {{\n\n']
                        for line in f:
                            # print(line)
                            if line.startswith('  @Test'):
                                test_seen = True
                            if not test_seen:
                                continue
                            line = line.replace('(timeout = 4000)', '')
                            line = line.replace('verifyException', '//verifyException')
                            modified_content.append(line)
                        # modified_content.append('\n}')
                        with open(wr, 'w') as writ:
                            writ.writelines(modified_content)





print('[+] Starting...')
for oracle in oracles:
    args = oracle.get_args()
    # arg = ('templateit_5', 'OpMatcher', 1)
    # gen_es_tests(arg[0], arg[1])
    for arg in args:
        # print(arg)
        gen_es_tests(arg[0], arg[1])