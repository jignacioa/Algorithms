def twoNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	left = 0
	right = len(array)-1
	while left < right:
		if array[left] + array[right] == targetSum:
			return [array[left], array[right]]
		if array[left] + array[right] < targetSum:
			left+=1
		if array[left] + array[right] > targetSum:
			right-=1
	return []


print(twoNumberSum([5,6,3,4,8,9], 14))