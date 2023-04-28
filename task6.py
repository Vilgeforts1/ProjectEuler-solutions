sum_squares = 0
square_sum = 0

for i in range(1, 101):
    sum_squares += i ** 2
    square_sum += i

print(square_sum ** 2 - sum_squares)
