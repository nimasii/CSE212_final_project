class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_difference(arr):
    bst = None
    max_diff = 0
    for i in range(len(arr)):
        if not bst:
            bst = Node(arr[i])
            min_value = arr[i]
        else:
            node = bst
            while True:
                if arr[i] < node.value:
                    if not node.left:
                        node.left = Node(arr[i])
                        min_value = min(min_value, arr[i])
                        break
                    node = node.left
                else:
                    if not node.right:
                        node.right = Node(arr[i])
                        max_diff = max(max_diff, arr[i] - min_value)
                        break
                    node = node.right
    return max_diff

arr = [2, 7, 3, 1, 4, 6, 5]
result = max_difference(arr)
print(result)  # Output: 5
