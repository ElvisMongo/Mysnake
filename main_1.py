import count_systems
from count_systems import convert

print('choose action','\n','\n'
'1 - conversion a number from binary system','\n' 
'2 - conversion a number from octal number system','\n'
'3 - conversion a number from hexadecimal number system','\n'
)
 
a = int(input('enter the number of operation: '))
 
if a == 1:
	y = int(input('Enter the number in the binary system: '))
	n = 2 # - основание конвертируемой системы исчисления

if a == 2:
	y = int(input('enter a number in octal number system: '))
	n = 8

if a == 3:
	y = str(input('enter a number in hexadecimal number system: '))
	n = 16	

print(convert(y, n))
