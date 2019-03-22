'''
给定数组arr,arr中所有的值都是正数且不重复，每个值代表一种面值的货币，每种面值的货币可以使用任意张，
再给定一个正数aim代表要找的钱数，求组成aim的最少货币数（类似于背包问题)
另dp[i][j]表示使用到第i种货币，换j的数量
dp[0][j]:arr[0]的倍数做相应处理，别的都是max
dp[i][0]:都是0，不需要货币就可以换0块钱

补充问题：arr中每个都是一张货币，只可以用或者不用，问最少的钱数 0-1背包
'''
import math 
def minCoind(arr, aim):
	dp = [[math.inf for _ in range(aim+1)] for _ in range(len(arr))]
	for i in range(len(arr)):
		dp[i][0] = 0 
	for j in range(aim+1):
		if j >= arr[0] and dp[0][j-arr[0]] != math.inf:
			dp[0][j] = min(dp[0][j],dp[0][j-arr[0]]+1)
	for i in range(1,len(arr)):
		for j in range(1, aim+1):
			if j>= arr[i]:
				dp[i][j] = min(dp[i-1][j], dp[i][j-arr[i]]+1)
			else:
				dp[i][j] = dp[i-1][j]
	return dp[len(arr)-1][aim]

#空间优化，使用一维数组来滚动更新，压缩空间复杂度
def minCoind2(arr, aim):
	dp = [math.inf for _ in range(aim+1)]
	dp[0] = 0 
	for j in range(aim+1):
		if j >= arr[0] and dp[j-arr[0]] != math.inf:
			dp[j] = min(dp[j],dp[j-arr[0]]+1)
	for i in range(1,len(arr)):
		for j in range(0, aim+1):
			if j>= arr[i]:
				dp[j] = min(dp[j], dp[j-arr[i]]+1)
			else:
				dp[j] = dp[j]
	return dp[aim]


print(minCoind([5,2,3], 20))
print(minCoind2([5,2,3], 20))
print(minCoind([5,2,3], 0))
print(minCoind2([5,2,3], 0))
print(minCoind([5,3], 2))
print(minCoind2([5,3], 2))

#补充问题，对于dp[i][j],更新遍历，因为只能用或者不用
#dp[i][j] = min(dp[i-1][j], dp[i-1][j-arr[i]]+1),左边是不用第i张货币，右边是使用第i张货币
#注意这里和前面的区别，dp[i-1][j-arr[i]]前i-1次，然后加上第i次使用了arr[i],刚好变为dp[i][j]
#这里直接写空间压缩后的写法
#由于这里都是关于i只和i-1的状态有关，而且涉及到j-arr[i]，如果从前向后更新，i-1的状态会被覆盖，所以要从后向前更新
def minCoind3(arr, aim):
	dp = [math.inf for _ in range(aim+1)]
	dp[0] = 0 
	for j in range(aim+1):
		if j >= arr[0] and dp[j-arr[0]] != math.inf:
			dp[j] = min(dp[j],dp[j-arr[0]]+1)
			break #这个break不能少，不然会和可以使用无数张钱的结果一样
	for i in range(1,len(arr)):
		for j in range(aim,0,-1):
			if j>= arr[i]:
				dp[j] = min(dp[j], dp[j-arr[i]]+1)
			else:
				dp[j] = dp[j]
	return dp[aim]
print(minCoind3([5,2,3],20))
print(minCoind3([5,2,5,3],10))
print(minCoind3([5,2,5,3],15))
print(minCoind3([5,2,5,3],0))