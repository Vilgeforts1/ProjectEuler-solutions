import numpy as np

""" 2^15 = 32678 and the sum of its digits is 3 + 2 + 6 + 7 + 8 = 26
    What is the sum of the digits of the number 2^1000?"""

num = 2 ** 1000
result = list(str(num))

print(np.sum(list(map(lambda x: int(x), result))))
