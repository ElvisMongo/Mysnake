def convert(y, n):
	k = 0	
	s = str(y)
	pow = lambda x,z: x**z
	m = len(s) 
	d = {
			'A': 10,
			'B': 11,
			'C': 12,
			'D': 13,
			'E': 14,
			'F': 15
		}
	
	if (n == 2) or (n == 8):
		for i in range(m):
			k += int(s[i])*pow(n, m-i-1)
			
	else:
		k = 0
		i = 0
		
		for i in range(m): # - происходит итерирование строки (аргумента y), сравнение текущего символа строки с буквой (A, B, C, D, E, F)
			if s[i] in d.keys():
				f = d[s[i]]
				k += pow(n, m-1-i)*int(f)	
			
			else:
				k += pow(n, m-1-i)*int(s[i])
	
	return k
	
	
