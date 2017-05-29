def Function(x, y, q): # - определение номера координатной четверти
    q = ''
    print('Enter coordinate x')
    x = int(input(''))
    print('Enter coordinate y')
    y = int(input(''))
    if (x>0) and (y>0):
        q = 'Point is located in the first quarter'
        return q
    elif (x<0) and (y>0):
        q = 'Point is located in the second quarter'
        return q
    elif (x<0) and (y<0):
        q = 'Point is located in the third quarter'
        return q
    elif (x>0) and (y<0):
        q = 'Point is located in the fourth quarter'
        return q
    elif (x==0) and (y==0):
        q = 'Point is located in the origin of the coordinates'
        return q
    else:
        q = 'Point is located on the one of the axes'
        return q

x = int()
y = int()
q = str()

print(Function(x, y, q))
