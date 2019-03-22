'''
返回两个字符串str1和str2，返回两个字符串的最长公共子序列
先求最长公共子序列的长度
dp[i][j]表示以str1[0...i]和str[0...j]的最长公共子序列的长度
dp[i][j] = max(dp[i-1][j],dp[i][j-1],if str1[i]==str2[j] dp[i-1][j-1]+1)
初始状态dp[0][j] == 1 if str1[0]==str2[j] else 0 
	   dp[j][0] == 1 if str1[j]==str2[0] else 0 
'''
def lcs(str1, str2):
	dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
	for i in range(len(str1)):
		if str1[i] == str2[0]:
			dp[i][0] = 1 
	for j in range(len(str2)):
		if str1[0] == str2[j]:
			dp[0][j] = 1 
	for i in range(1,len(str1)):
		for j in range(1,len(str2)):
			dp[i][j] = max(max(dp[i-1][j],dp[i][j-1]), dp[i-1][j-1]+(1 if str1[i]==str2[j] else 0))
	return dp

'''
1：这个里的空间复杂度同样可以通过滚动数组来减小
2：怎么获得字符串序列呢，和找递增序列一样，从后往前 
'''
def getlcs(dp, str1, str2):
	m,n = len(str1)-1, len(str2)-1
	nowmax = dp[m][n]-1
	res = []
	while nowmax >= 0:
		if m > 0 and dp[m][n] == dp[m-1][n]:
			m = m-1
		elif n > 0 and dp[m][n] == dp[m][n-1]:
			n = n-1
		elif dp[m][n] == dp[m-1][n-1]+1:
			res.append(str1[m])
			m = m-1
			n = n-1
			nowmax -= 1
	return ''.join(res[::-1])




str1 = '1A2C3D4B56'
str2 = 'B1D23CA45B6A'
print(lcs(str1,str2)[len(str1)-1][len(str2)-1])
print(getlcs(lcs(str1,str2), str1, str2))