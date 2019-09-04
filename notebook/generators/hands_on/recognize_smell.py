def generator_useful(n,divider):
    """Wonderful comments"""

    for i in range(n):
        if i % divider == 0:
            continue
        yield i

for i in generator_useful(9,3):
    print('Square is', i ** 2)

for i in generator_useful(5,2):
    print('Cube is', i ** 3)

for i in generator_useful(13,5):
    print('A' * i)
