'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(100000)

## Function to compute factorial of a given number
def compute_factorial(number):
    print(f"Computing Factorial of  {number} : ")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000,6000,70000,8000]
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial,numbers)
    end_time = time.time() - start_time
    print(f"Results : {results}")
    print(f"Time taken : {end_time} seconds")