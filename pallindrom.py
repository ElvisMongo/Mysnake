print('Enter string, please') # - задача про паллиндром
st = str(input(''))
def reverse_string(st):
	st1 = st[::-1]
	if st1 == str(st):
		return True
	else:
		return False
		
print(reverse_string(st))
		
