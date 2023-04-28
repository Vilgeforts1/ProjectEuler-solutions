
"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""
from datetime import datetime

start = datetime.now()


n = int(input("Number of prime numbers: "))
numbers = [2]

for i in range(3, n + 1, 2):
    stop = 0
    q = (n ** 0.5) + 2
    for num in numbers:
        if num > q:
            break
        if i % num == 0:
            stop = 1
            break
    if stop == 0:
        numbers.append(i)

print(numbers)
print(datetime.now() - start)

