import concurrent.futures
import time

def function_to_run(arg1, arg2):
    # Simulating a long-running process and printing the arguments
    print(f"Function called with arguments: {arg1}, {arg2}")
    time.sleep(5)  # Simulate a long-running process
    return "Completed"

def run_with_timeout(func, timeout, *args):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(func, *args)
        try:
            result = future.result(timeout=timeout)
            return result
        except concurrent.futures.TimeoutError:
            print(f"Function call timed out after {timeout} seconds. Retrying...")
            return run_with_timeout(func, timeout, *args)

if __name__ == "__main__":
    timeout = 7  # 1 minute
    arg1 = "Hello"
    arg2 = "World"
    result = run_with_timeout(function_to_run, timeout, arg1, arg2)
    print(result)
