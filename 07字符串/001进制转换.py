from string import digits, ascii_lowercase, ascii_uppercase


def tentoany(n, base):
	chars = digits+ascii_lowercase+ascii_uppercase
	a,b = divmod(n,base)
	if a:
		return tentoany(a,base)+chars[b]
	else:
		return chars[b]

def anytoten(n, base):
	chars = digits+ascii_lowercase+ascii_uppercase
	if not n:
		return 0
	else:
		return base*(anytoten(n[:-1],base))+chars.index(n[-1])
def anytoten2(n, base):
    chars = digits+ascii_lowercase+ascii_uppercase
    res = 0
    for i,v in enumerate(n[::-1]):
    	 res += pow(base,i)*chars.index(v)
    return res





print(tentoany(10,2))
print(tentoany(10,8))
print(anytoten('1010',2))
print(anytoten2('1010',2))
print(tentoany(200,16))
print(anytoten2('c8',16))
print(anytoten('c8',16))