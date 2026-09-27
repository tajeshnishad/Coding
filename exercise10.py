values=[]
for value in range(1,21):
    values.append(value)
print(values)
print('\n')
no = []
for nos in range(10_0000):
    no.append(nos)
print(no)
print(min(no))
print(max(no))
print(sum(no))
print('\n')
odd_num=[val for val in range(1,21,2)]
print(odd_num)

print('\n')

lst=[]
for mul_of_3 in range(1,11):
    lst.append(mul_of_3 * 3)
print(lst)

print('\n')

cubes=[]
for cube in range(1,11):
    cubes.append(cube**3)
print(cubes)

print('\n')

cub=[cu**3 for cu in range(1,11)]
print(cub)