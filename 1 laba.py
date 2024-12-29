from math import *

x, y, z = float(input('Введите x: ')), float(input('Введите y: ')), float(input('Введите z: '))

if x==0 or abs(x - x**2 * y**2) == 0 or z == 0:
    print('Недопустимые значения x, y или z.')
else:
	s = ((1 + sin(x + y)**2) / (abs(x - x**2 * y**2))) * x**abs(y) + atan(1/z)
	print(f'Результат : {s}')