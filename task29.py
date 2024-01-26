

result = []

for i in range(2, 101):
    for j in range(2, 101):
        if i ** j not in result:
            result.append(i ** j)

print(len(result))