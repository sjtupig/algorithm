def partition(nums):
	left = -1
	index = 0
	right = len(nums)
	while index < right:
		if nums[index] == 0:
			left += 1
			nums[left] ,nums[index]= nums[index],nums[left]
			index+=1
		elif nums[index] == 2:
			right -= 1
			nums[right], nums[index] = nums[index], nums[right]
		else:
			index += 1
	return nums 

nums = [2,0,1,1,0,0,2,1,2,1]
print(partition(nums))