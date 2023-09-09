from math import sqrt
import numpy as np


def dividers(x, massive=None):
    limit = int(sqrt(x) + 1)
    if massive is None:
        massive = set()
    for i in range(1, limit):
        if x % i == 0:
            massive.add(i)
            massive.add(x // i)
    return massive


def series_sum(n):
    return np.sum([i for i in range(1, n + 1)])


count = 8
while len(dividers(series_sum(count))) <= 500:
    count += 1

print(f'Result is {series_sum(count)}')

