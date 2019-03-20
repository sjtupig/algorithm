def sortstack(stack):
	helps = []
	while stack:
		t = stack.pop()
		while helps and helps[-1] < t:
			stack.append(helps.pop())
		helps.append(t)
	while helps:
		stack.append(helps.pop())


'''def sortstack(stack):
	anstack = []
	while stack:
		while (not anstack) or (stack and stack[-1] >= anstack[-1]) :
			print(stack,anstack)
			anstack.append(stack.pop())
		if not stack:
			return anstack
		t = stack.pop()
		while anstack and anstack[-1] >= t:
			stack.append(anstack.pop())
		anstack.append(t)
	return anstack'''

stack = [4,2,6,9,2,2,3]
sortstack(stack)
print(stack)