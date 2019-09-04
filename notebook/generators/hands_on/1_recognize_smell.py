#for i in range(9):
#    if i % 3 == 0:
#        continue
#    print('Square is', i ** 2)

def square_iterator(n):
    for i in range(n):
        if i % 3 != 0:
            yield i **2

for i in square_iterator(9):
    print('Square is', i)

#for j in range(5):
#    if j % 2 == 0:
#        continue
#    print('Cube is', j ** 3)

def cube_iterator(n):
    for i in range(n):
        if i % 2 != 0:
            yield i ** 3

for i in cube_iterator(5):
    print('Cube is', i)


#for k in range(13):
#    if k % 5 == 0:
#        continue
#    print('A' * k)

def a_times(n):
    for k in range(n):
        if k % 5 != 0:
            yield 'A'*k

for i in a_times(13):
    print(i)
