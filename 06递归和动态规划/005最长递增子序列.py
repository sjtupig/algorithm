'''
给定arr,返回arr的最长递增子序列
'''
#dp[i]表示以arr[i]结尾的最长子序列的长度
def Lis1(arr):
	dp = [1 for _ in range(len(arr))] 
	for i in range(1,len(arr)):
		for j in range(i):
			if arr[i] > arr[j]:
				dp[i] = max(dp[i], dp[j]+1)
	return dp
#得到递增子序列
def getlis(arr, dp):
	res = []
	index = dp.index(max(dp))#得到最大值可以在o(n)里取得
	res.append(arr[index])
	i = index 
	while i >= 0:
		if arr[i] < arr[index] and dp[i]+1== dp[index]:
			res.append(arr[i])
			index = i 
		else:
			i -= 1 
	return res[::-1]


arr = [2,1,5,3,6,4,8,9,7]
print(getlis(arr, Lis1(arr)))
#优化，以一个ends数组来记录,ends[i]表示长度为i+1的递增序列的最小的尾巴,ends[0...right]表示有效区
#初始时，right=0,ends[0] = arr[0],dp[0] = 1,要找到最左边的大于等于arr[i]的数
def Lis2(arr):
	ends = [0]*len(arr)
	ends[0] = arr[0]
	right = 0 
	dp = [1]*len(arr)
	for i in range(1,len(arr)):
		l = 0 
		r = right 
		while l <= r:
			mid = (l+r)//2 
			if arr[i] > ends[mid]:
				l = l+1
			else:
				r = r-1 #因为要找到最左边的，所以==的时候也r-1
		right = max(right,l)
		ends[l] = arr[i]
		dp[i] = l+1
	return dp  
print(getlis(arr, Lis2(arr)))