from collections import deque 
def getmaxwindow(nums, k):
	maxqueue = deque() #用一个双端队列来维护当前最大值的下标,以及后面可能成为最大值的下标
	res = []
	for i,v in enumerate(nums):
		while maxqueue and v > nums[maxqueue[-1]]:
			maxqueue.pop()
		maxqueue.append(i)
		print(maxqueue)
		if maxqueue[0] == i-k:
			maxqueue.popleft()
		if i >= k-1:
			res.append(nums[maxqueue[0]])
	return res 
	
print(getmaxwindow([1,1,3,2,5,6],3))


