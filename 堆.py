
class heapq(object):
	"""docstring for heapq"""
	def __init__(self):
		self.heaplist = []
		self.currentsize = 0
	#下降
	def percDown(self, i):
		while 2*(i+1) < self.currentsize:
			print(2*i)
			minindex = 2*i+1 if (2*i+1) < self.currentsize and self.heaplist[2*i+1] < self.heaplist[2*i] else 2*(i+1)
			print('minindex',minindex)
			print(self.heaplist[i], self.heaplist[minindex])
			if self.heaplist[i] > self.heaplist[minindex]:
				self.heaplist[i], self.heaplist[minindex] = self.heaplist[minindex], self.heaplist[i]
			print(self.heaplist[i], self.heaplist[minindex])
			i = minindex

	def percUp(self,i):
		while i//2:
			if self.heaplist[i//2] > self.heaplist[i]:
				self.heaplist[i], self.heaplist[i//2] = self.heaplist[i//2], self.heaplist[i]
			i = i//2 
	def build(self,alist):
		i = len(alist)//2 #从最后一个非叶子节点开始
		self.currentsize = len(alist)
		self.heaplist = alist[:]
		while i>-1:
			print('nuild', i)
			self.percDown(i)
			i = i - 1

he = heapq()
he.build([2,3,5,1,7])
print(he.currentsize)
print(he.heaplist)
