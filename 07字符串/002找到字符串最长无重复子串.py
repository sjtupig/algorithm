
def getMaxUniqueSubString(s):
	dicts = {}
	l,r = 0, 0 #用左右指针来指示符合条件的子串的左右端
	maxlen = 0
	i= 0
	while r < len(s):
		if s[r] not in dicts:
			dicts[s[r]] = r
		else:
			l = max(l,dicts[s[r]]+1)
			dicts[s[r]] = r
		maxlen = max(maxlen,r-l+1)
		r+=1
	return maxlen

print(getMaxUniqueSubString('aabcb'))

print(getMaxUniqueSubString('aabccdefgbb'))