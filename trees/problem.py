class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_difference(arr):
    '''
    Complete the max_difference function
    In this problem, you will need to create the bst as you loop through the array.
    Feel free to use the problem solution if you get stuck.
    Remember that this function is supposed to find the maximum difference between any two items in the BST given one condition.
    A difference can only count if the larger number appears after the smaller number.
    '''
    bst = None
    max_diff = 0
    for i in range(len(arr)):
        if not bst:
            bst = Node(arr[i])
            min_value = arr[i]
        # CODE GOES HERE
    return arr

arr = [2, 7, 3, 1, 4, 6, 5]
result = max_difference(arr)
print(result)  # Output: 5