
def fi(n):
	if n < 1:
		return 0
	elif n == 1 or n == 2:
		return 1
	a1 = 1
	a2 = 1
	for i in range(3,n+1):
		now = a1+a2 
		a1 = a2
		a2 = now 
	return now 

print(fi(6))
'''
奶牛生牛：每头成熟的牛一年生一次，新出生的牛三年后成熟，
那么f(n)由两部分组成，f(n)=老牛+新牛 ,老牛=f(n-1),新牛是刚出生的牛，三年前的牛可以生新牛，新牛=f(n-3)
所以f(n)=f(n-1)+f(n-3)
'''
def getcow(n):
	if n < 1:
		return 0
	elif n in [1,2,3]:
		return n 
	else:
		a1 = 1
		a2 = 2
		a3 = 3 
		for i in range(4,n+1):
			now = a3+a1 
			a1 = a2 
			a2 = a3 
			a3 = now
		return now  
print(getcow(10))
'''
走台阶：一次可以走1或者2步，等价于斐波那契数列
一次可以走1-n步，2^n
f(n) = f(n-1)+...+f(0)
f(n-1) = f(n-2)+...+f(0)
so:f(n)=2f(n-1) = ...= 2^nf(0) = 2^n
'''