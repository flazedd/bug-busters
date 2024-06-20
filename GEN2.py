from config import constant

oracles = constant.ORACLES


print('[+] Starting...')
for oracle in oracles:
    args = oracle.get_args()
    # arg = ('templateit_5', 'OpMatcher', 1)
    # gen_es_tests(arg[0], arg[1])
    for arg in args:
        for i in range(7, 13):
            test_name = f'{arg[1]}_ESTest_{i}'
            result = oracle.exec_suite(arg[0], test_name)
            if oracle.did_test_fail(result):
                print(f'[+] FAILED: {test_name}')
            else:
                print(f'[+] PASSED: {test_name}')
