class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_bst(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    elif value > root.value:
        root.right = insert_bst(root.right, value)
    return root

def kth_smallest_element(root, k):
    if not root:
        return None
    stack = []
    current = root
    count = 0

    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            node = stack.pop()
            count += 1
            if count == k:
                return node.value
            current = node.right
        else:
            break
    return None

# Example usage:
root = None
root = insert_bst(root, 5)
root = insert_bst(root, 3)
root = insert_bst(root, 6)
root = insert_bst(root, 2)
root = insert_bst(root, 4)
root = insert_bst(root, 7)
k = 3
result = kth_smallest_element(root, k)
print(f"The {k}th smallest element in the binary search tree is: {result}")
