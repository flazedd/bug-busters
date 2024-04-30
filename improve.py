import threading
import utils


# templateit_5.OpMatcherTest_Improved
# jnfe_6.AbstractNFeAdaptadorBeanTest_Improved

# #expects (folder, filename, model_number)
# t1 = ('templateit_5', 'OpMatcher', 1)
# t2 = ('jnfe_6', 'AbstractNFeAdaptadorBean', 1)

args = utils.get_args()
threads = []
for arg in args:
    thread = threading.Thread(target=utils.worker, args=arg)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
