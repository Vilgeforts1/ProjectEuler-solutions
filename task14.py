import numpy as np

N = 1000000


def longest_chain(n):
    counter = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
            counter += 1
        else:
            n = 3 * n + 1
            counter += 1
    return counter


result = 0
maximum = 0
while N != 13:
    length_chain = longest_chain(N)
    if length_chain > maximum:
        maximum = length_chain
        result = N
    N -= 1

print(result)