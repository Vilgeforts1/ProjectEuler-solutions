
"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""

# set of prime numbers from task 7
n = 2000000
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

print(sum(numbers))
