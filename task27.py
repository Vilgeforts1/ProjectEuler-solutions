from tqdm import tqdm
import math


def is_prime(number):
    # список простых чисел начинается с 2, всё остальное можно сразу отмести
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number))
    divisors = range(2, (number_sqrt + 1))
    # Если число не простое, то в отрезке от 1 до квадратного корня числа, точно будут его делители.
    for element in divisors:
        if number % element == 0:
            return False
    return True


def prime_numbers(n, lst):
    for i in range(3, n + 1, 2):
        stop = 0
        q = (n ** 0.5) + 2
        for num in lst:
            if num > q:
                break
            if i % num == 0:
                stop = 1
                break
        if stop == 0:
            lst.append(i)


a_dividers = [2]

prime_numbers(999, a_dividers)
negative_numbers = list(map(lambda x: x * (-1), a_dividers.copy()))


a_dividers += negative_numbers
a_dividers += [1]
a_dividers.sort()
b_dividers = a_dividers.copy()


#print(a_dividers, b_dividers, sep='\n')


stopp = True
coefficient_a, coefficient_b = 0, 0
maximum_numbers = 0
while stopp:
    for a in tqdm(a_dividers):
        for b in b_dividers:
            count = 0
            for n in range(0, 1002):
                d = n ** 2 + a * n + b
                if is_prime(d):
                    count += 1
                else:
                    break
            if maximum_numbers <= count:
                maximum_numbers = count
                coefficient_a, coefficient_b = a, b
    stopp = False

print(maximum_numbers)
print(coefficient_a, coefficient_b)
print(coefficient_a * coefficient_b)

