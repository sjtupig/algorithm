def quicksort(nums):
	if len(nums) <= 1:
		return nums 
	else:
		return quicksort([i for i in nums if i < nums[0]]) + [i for i in nums if i == nums[0]] + quicksort([i for i in nums if i > nums[0]])

nums = [3,1,4,5,2,4]

print(quicksort(nums))



def partition(nums,l,r):
	pivot = nums[l]
	while l < r:#因为取的是最左边的节点，所以要从右边开始遍历
		while l < r and nums[r] >= pivot:
			r -= 1
		nums[l]=nums[r]
		while l < r and nums[l] <= pivot:
			l+=1
		nums[r]=nums[l]
		
	nums[l] = pivot
	return l 

def quicksort(nums, l, r):
	if l < r:
		pivot = partition(nums,l,r)
		quicksort(nums,l,pivot-1)
		quicksort(nums,pivot+1,r)
	return nums 

print(quicksort([2,1,23,2,4,5], 0, 5))
import random  

def quicksort(nums, l, r):
	if l < r:
		pivot = partition(nums, l, r)
		quicksort(nums,l,pivot-1)
		quicksort(nums,pivot+1,r)
	return nums 
def partition(nums,l,r):
	index = random.choice(range(l,r+1))
	nums[l], nums[index] = nums[index], nums[l] 
	pivot = nums[l]
	while l < r:
		while l < r and nums[r] >= pivot:
			r -= 1
		nums[l] = nums[r]
		while l < r and nums[l] <= pivot:
			l+=1
		nums[r]=nums[l]
	nums[l] = pivot 
	return l 
print(quicksort([5,2,3,25,89,-3,1,7],0,7))