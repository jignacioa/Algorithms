def findClosestValueInBst(tree, target):
    # Write your code here.
	tracker = tree
	closestValue = tracker.value
	while tracker is not None: 
		if abs(target-closestValue) > abs(target-tracker.value):
			closestValue = tracker.value 
		if target < tracker.value:
			tracker = tracker.left
		elif target > tracker.value:
			tracker = tracker.right
		else:
			break
	return closestValue 

class BST:
    def __init__(self, value):
    self.value = value
        self.left = None
        self.right = None