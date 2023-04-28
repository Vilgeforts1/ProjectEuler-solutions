"""The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145
Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a
starting number below one million is sixty terms.
How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?"""
from math import factorial
from tqdm import tqdm
from datetime import datetime

start = datetime.now()


def sum_of_fact(number):
    if isinstance(number, (int, float)):
        number = str(number)
    result = 0
    for digit in number:
        result += factorial(int(digit))
    return result


r = 0
for i in tqdm(range(2, 1000000)):
    i = str(i)
    fact_digits = sum_of_fact(i)
    count = 1
    repeat = []
    while i != str(fact_digits) and fact_digits not in repeat:
        repeat.append(fact_digits)
        fact_digits = sum_of_fact(fact_digits)
        count += 1
    if count == 60:
        r += 1

end = datetime.now() - start
print(r)
print(end)
