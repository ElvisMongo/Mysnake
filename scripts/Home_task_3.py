x1, y1, x2, y2, x3, y3 = list(map(int, input('Input numbers: ').split( ))) # - Задача про прямоугольный треугольник
a = (x2-x1)**2+(y2-y1)**2
b = (x3-x1)**2+(y3-y1)**2
c = (x3-x2)**2+(y3-y2)**2

if (a == b + c) or (b == c + a) or (c == b + a):
    print('The triangle is rectangular')
else: 
	print('The triangle is not rectangular')

