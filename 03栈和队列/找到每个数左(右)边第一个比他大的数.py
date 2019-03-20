'''

利用单调栈，从左至右依次压入数据，当数据出栈的时候，它的前面一个元素就是它左边第一个大于它的数

'''
def popStacksetMap(stack,lBigmap):
	t = stack.pop()
	if not stack:
		lBigmap[t] = None
	else:
		lBigmap[t] = stack[-1]
	return lBigmap,stack


def getleftbigger(nums):
	lBigmap = {}
	stack = []
	for i in nums:
		print(i, stack)
		while stack and stack[-1] < i:
			lBigmap,stack = popStacksetMap(stack, lBigmap)
		stack.append(i)
	while stack:
		lBigmap,stack = popStacksetMap(stack, lBigmap)

	return lBigmap 

def getrightbigger(nums):
	rBigmap = {}
	stack = []
	for i in nums[::-1]:
		while stack and stack[-1]<i:
			rBigmap, stack = popStacksetMap(stack, rBigmap)
		stack.append(i)
	while stack:
		rBigmap, stack = popStacksetMap(stack, rBigmap)
	return rBigmap

nums = [6,2,3,4,1,7,9]
print(getleftbigger(nums))
print(getrightbigger(nums))