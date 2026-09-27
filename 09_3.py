numbers = list(range(1,6))
print(f'{numbers}'"\n")

even_num=list(range(2,11,2))
print(even_num)
print('\n')

squares=[]
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

print('\n')

squares=[]
for value in range(1,11):
    square = value ** 2
    squares.append(square)
    print(squares)

print('\n')

digits=[1,2,3,4,5,6,11,7,8,9]
print(min(digits))
print(max(digits))
print(sum(digits))
print(sorted(digits))
digits.append(99)
print(digits)
digits.insert(2,21)
print(digits)

cube=[]
for value in range(1,6):
    cube.append(value**3)
print(cube)

squ=[value**2 for value in range(1,10)]
print(squ)