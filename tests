#TESTS

import time
from random import randint

tests = [randint(0, 45) for i in range(10)]

def fib(n):
    a1, a2 = 0, 1

    if n == 0: return a1
    elif n == 1: return a2
    else:
        for i in range(n-1):
            a1, a2 = a2, a1+a2
        return a2

for i in range(len(tests)):

    t_start = time.perf_counter()

    ans = fib(tests[i])

    print('NUM:', i+1, ' TIME:', (time.perf_counter() - t_start), 'INP: ', tests[i], ' ANS:', ans)
