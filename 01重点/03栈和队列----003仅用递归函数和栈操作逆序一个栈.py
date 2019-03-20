def getandremovelast(stack):
	t = stack.pop()
	if not stack:
		return t 
	else:
		last = getandremovelast(stack)
		stack.append(t)
		return last 

def reversestack(stack):
	if not stack:return 
	t = getandremovelast(stack)#这里需要取得栈最下面的元素
	#t = stack.pop()
	print(stack)
	reversestack(stack)
	stack.append(t)
	return stack


nums = [1,2,3,4,5,8,9]
print(reversestack(nums))