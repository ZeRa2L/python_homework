pi = 3.1415926
radius = 42
space = pi * (radius ** 2)
space = round(space, 4)

print('Площадь круга:', space)

point_1 = (23, 34)
distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** .5

print('Расстояние от нуля до точки:', distance_1)

if distance_1 <= radius:
    print('True')
else:
    print('False')

point_2 = (30, 30)
distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** .5

print('Расстояние от нуля до точки:', distance_2)

if distance_2 <= radius:
    print('True')
else:
    print('False')