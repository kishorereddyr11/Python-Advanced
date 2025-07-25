##It allows to create process to run prallel
## when to use - cpu bound task
## prallel Execution

import multiprocessing
import time

def square_num():
    for i in range(5):
        time.sleep(1)
        print(f"Square of {i}: {i*i}")

def cube_num():
    for i in range(5):
        time.sleep(1)
        print(f"Cube of {i}: {i*i*i}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square_num)
    p2 = multiprocessing.Process(target=cube_num)

    start_time = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    total_time = time.time() - start_time
    print(f"\nTotal execution time: {total_time:.2f} seconds")