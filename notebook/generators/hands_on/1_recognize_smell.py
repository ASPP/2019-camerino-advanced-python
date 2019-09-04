def nondivisible(n,divide_by):
    for i in range(n):
        if i % divide_by != 0:
            yield i


for i in nondivisible(9,3):
    print('Square is', i ** 2)

for i in nondivisible(5,2):
    print('Cube is', i ** 3)

for i in nondivisible(13,5):
    print('A' * i)
