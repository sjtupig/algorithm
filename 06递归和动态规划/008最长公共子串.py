'''
给定两个字符串，返回两个字符串的最长公共子串
经典解法和最长公共序列类似dp[i][j] = dp[i-1][j-1]+1 if str1[i]==str2[j],不再赘述
			注意这里最长公共子串的长度是max(dp),找到所在的index处，一直向前反走max(dp)步即可

空间复杂度降低方法：斜线计算，因为是公共子串，所以计算方向只能是按照斜线来，一共有m+n-1个起始位置，
				  可以从(0,n-1)开始往左，到达(0,0)后再向下计算
'''
#这是优化后的方法
def getlsct(str1,str2):
	m,n = len(str1)-1,len(str2)-1
	row , col = 0, n #从(0,n)开始
	maxlen = 0 
	end = 0 #记录最长子串在str1的end
	while row <= m:
		i,j = row, col 
		tlen = 0 #当前计算的值
		while i <= m and j <= n:
			#想右下方走
			if str1[i] == str2[j]:
				tlen += 1
			else:
				tlen = 0 
			if tlen > maxlen:
				maxlen = tlen
				end = i 
			i += 1 
			j += 1
		if col > 0:
			col -= 1
		else:
			row += 1 
	return str1[end-maxlen+1:end+1]
str1 = '1AB2345CD'
str2 = '12345EF'
print(getlsct(str1,str2))
