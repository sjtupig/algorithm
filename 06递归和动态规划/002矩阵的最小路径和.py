'''
给定一个矩阵，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有数字累加起来就是路径和，返回最小路径和

dp[i][j]只能是从dp[i-1][j]或者dp[i][j-1]走来的
dp[i][j] = min(dp[i-1][j],dp[i][j-1])+p[i][j]
这里ij状态只和i-1,j-1有关，可以空间压缩
dp[j] = min(dp[j],dp[j-1])+p[i][j]
这是在行方向上压缩，还可以在列方向上压缩。最优做法是选择行/列数较小值来做压缩

通过一维数组滚动更新来减小二位动态规划的空间复杂度，并且由两次寻址变成一次寻址，也缩减了常数时间
'''
#原始解法：略过。
#这是在列上压缩
def minpathsum(p):
	if not p:return 
	m,n = len(p), len(p[0])
	dp = [0]*n
	dp[0] = p[0][0]
	for j in range(n):
		dp[j] = dp[j-1]+p[0][j]
	for i in range(1,m):
		dp[0] = dp[0]+p[i][0]
		for j in range(1,n):
			dp[j] = min(dp[j],dp[j-1])+p[i][j]
	return dp[n-1]

#空间最优解法
def minpaths(p):
	if not p:return 
	more,less = max(len(p), len(p[0])), min(len(p), len(p[0]))
	rowmore = more == len(p)
	dp = [0]*less 
	dp[0] == p[0][0] 
	for j in range(less):
		dp[j] = dp[j-1] + p[0][j] if rowmore else p[j][0]
	for i in range(1,more):
		dp[0] = dp[0]+p[i][0] if rowmore else p[0][i]
		for j in range(1,less):
			dp[j] = min(dp[j],dp[j-1])+p[i][j] if rowmore else p[j][i]
	return dp[less-1]

p = [[1,3,5,9],
	 [8,1,3,4],
	 [5,0,6,1],
	 [8,8,4,0]]
print(minpathsum(p))
print(minpaths(p))
