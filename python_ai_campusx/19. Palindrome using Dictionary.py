import time

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

start = time.time()
print(fib(4))
print("This code took", time.time() - start, "sec")
