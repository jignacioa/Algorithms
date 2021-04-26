def isValidSubsequence(array, sequence):
    # Write your code here.
	index = 0
	for integer in array:
		if integer == sequence[index]:
			index+=1
		if index == len(sequence):
			return True
	return False 
	

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]))