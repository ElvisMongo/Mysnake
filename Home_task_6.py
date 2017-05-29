def sort(x, l): # - сортировка элементов списка
    q = int()
    F = bool()
    for k in range(1,l):
        F = False
        for i in range(l-k):
            if x[i+1] < x[i]:
                q = x[i]
                x[i] = x[i+1]
                x[i+1] = q
                F = True
        if F == False:
            break
    return x


x = []
l = int()
x = list(map(int, input('Input elements: ').split( )))
l = len(x)

sort(x, l)
print(x)
