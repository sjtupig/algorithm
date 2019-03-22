'''
给定数组arr,arr中的所有的值都是正数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，给定一个
正数aim代表要找的钱数，求换钱有多少种方法。
'''
#以[5,10,25,1] aim=1000，看暴力解法
#0张5 ，剩下的[10,25,1]组成1000， res1
#1张5，剩下的[10,25,1]组成995，res2
#2张5, 剩下的[10,25,1]组成990，res3 .....
#pre(arr, index, aim)表示以arr[index:]来组成aim
def pre(arr, index, aim):
	res = 0 
	if index == len(arr):
		return 1 if not aim else 0 
	else:
		i = 0 
		while arr[index]*i <= aim:
			res += pre(arr, index+1,aim-arr[index]*i)
			i+=1 

def coins1(arr, aim):
	return pre(arr, 0, aim)
#这样有很多重复计算，用字典来记录已经计算过的值，记忆化搜索，分析递归函数的状态可以由哪些变量表示，做出相应维度和大写的字典来存即可。
#用动态规划来解
#dp[i][j]表示使用arr[0...i]来组成j一共有多少种
#dp[i][j] = dp[i-1][j-k*arr[i]] else 0 for k =0 to k*arr[i] <= j, k+=1
#dp[i-1][j-arr[i]]+...+dp[i-1][j-k*arr[i]] = dp[i][j-arr[i]]
#考虑边界,dp[0][0] = 1
def coins2(arr, aim):
	dp = [0]*(aim+1)
	for j in range(aim+1):
		if j%arr[0] == 0:
			dp[j] = 1 
	for i in range(1,len(arr)):
		for j in range(aim+1):
			if j >= arr[i]:
				dp[j] = dp[j] + dp[j-arr[i]]
			else:
				dp[j] = dp[j] 
	return dp[aim] 

print(coins2([5,10,25,1],0))
print(coins2([5,10,25,1],15))
print(coins2([3,5],2))