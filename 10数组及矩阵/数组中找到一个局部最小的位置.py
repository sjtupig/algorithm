def getlessindex(nums):
	if not nums:return 
	if nums[0] < nums[1]:
		return 1
	if nums[-1] < nums[-2]:
		return len(nums)-1
	l = 1
	r = len(nums)-2
	while l < r:
		mid = (l+r)//2
		if nums[mid]>nums[mid-1]:
			r = mid-1
		elif nums[mid]>nums[mid+1]:
			l = mid+1
		else:
			return mid 
	return l 


nums = [2,1,3,2,4,7]
print(getlessindex(nums))