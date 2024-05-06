import threading
import time

import utils


# templateit_5.OpMatcherTest_Improved
# jnfe_6.AbstractNFeAdaptadorBeanTest_Improved

# #expects (folder, filename, model_number)
# t1 = ('templateit_5', 'OpMatcher', 1)
# t2 = ('jnfe_6', 'AbstractNFeAdaptadorBean', 1)

args = utils.get_args()
print(args)
threads = []
# args = [args[0]]
# print(args)

start = time.time()

for arg in args:
    utils.worker(arg[0], arg[1], arg[2])

# for arg in args:
#     thread = threading.Thread(target=utils.worker, args=arg)
#     threads.append(thread)
#     thread.start()
#
# # Wait for all threads to complete
# for thread in threads:
#     thread.join()

end = time.time()
print(f'\n\nCompleted in {end - start} seconds')

