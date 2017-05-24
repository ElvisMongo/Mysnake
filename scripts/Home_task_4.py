print('Enter string, please') # - задача про паллиндром
st = str(input(''))
st1 = st[::-1]

if st == st1:
    print('This string is pallindrom')
else:
    print('This string is not pallindrom')
