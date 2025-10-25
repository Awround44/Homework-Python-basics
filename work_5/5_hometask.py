# Task 5
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.20f} seconds")
        return result
    return wrapper

#sum of two numbers
@time_decorator
def sum_numbers(a: int, b: int) -> int:
    result = a + b
    print(f"Sum: {result}")
    return result

@time_decorator
def process_files():
    with open('input.txt', 'r') as infile:
        a, b = map(int, infile.read().strip().split())
    result = a + b
    with open('output.txt', 'w') as outfile:
        outfile.write(f"Sum: {result}\n")
    return result

sum_numbers(5, 3)
process_files()
