import time
from multiprocessing import Pool

def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def print_fibo(num):
    print(fibo(num))

if __name__ == "__main__":
    start_time = time.time()
    num_list = [32, 33, 34, 35]

    pool = Pool(processes=4)
    pool.map(print_fibo, num_list)
    finish_time = time.time()
    elapsed_time = finish_time - start_time
    print(elapsed_time)



