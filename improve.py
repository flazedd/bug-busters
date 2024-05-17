import time

from config import constant
from utility import utils

# templateit_5.OpMatcherTest_Improved
# jnfe_6.AbstractNFeAdaptadorBeanTest_Improved

# #expects (folder, filename, model_number)
# t1 = ('templateit_5', 'OpMatcher', 1)
# t2 = ('jnfe_6', 'AbstractNFeAdaptadorBean', 1)

# args = utils.get_args()
# print(args)
oracles = constant.ORACLES
threads = []
# [('a4j_2', 'Directors', 1), ('templateit_5', 'OpMatcher', 1), ('tullibee_1', 'Contract', 1), ('tullibee_1', 'Util', 1)]
# [('a4j_2', 'Directors', 1)]
# args = [('templateit_5', 'OpMatcher', 1)]
# print(args)

start = time.time()
for oracle in oracles:
    args = oracle.get_args()
    # print(oracle.get_args())
    # args = [('templateit_5', 'OpMatcher', 0)]
    for arg in args:
        utils.worker(arg[0], arg[1], arg[2], oracle)

# for arg in args:
#     utils.worker(arg[0], arg[1], arg[2])

# for arg in args:
#     thread = threading.Thread(target=utils.worker, args=arg)
#     threads.append(thread)
#     thread.start()
#
# # Wait for all threads to complete
# for thread in threads:
#     thread.join()

end = time.time()
print(f'[+] Completed in {end - start:.2f} seconds')

