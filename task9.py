
"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""
from math import sqrt

a, b = 0, 0


for i in range(1, 500):
    for j in range(i + 1, 501):
        if sqrt(i ** 2 + j ** 2) + i + j == 1000:
            a, b = i, j

c = 1000 - (b + a)
print(a, b, c)
print(f"{a}^2 + {b}^2 = {c}^2")
print(a + b + c)
print(a * b * c)
