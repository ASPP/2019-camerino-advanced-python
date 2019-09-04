def is_not_divisible(m, n):
    for i in range(n):
        if i % m == 0:
            continue
        yield i

for i in is_not_divisible(3, 9):
    print('Square is', i ** 2)

for j in is_not_divisible(2, 5):
    print('Cube is', j ** 3)

for k in is_not_divisible(5,13):
    print('A' * k)
