
"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

n = 600851475143
dividers = []
divide = 0

for i in range(2, n):
    while n % i == 0:
        dividers.append(i)
        n /= i
    divide = n
    if divide == 1:
        break

print(*dividers)


