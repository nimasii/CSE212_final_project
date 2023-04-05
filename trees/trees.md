# Linked Lists In Python

## What Is A Tree?
A tree are somewhat similar to linked lists because nodes are linked together by pointers. They do have one main difference, however. Trees are able to connect to multiple different nodes, similar to a family tree where one person can be connected to multiple people.
  
There are three different types of trees; binary trees, binary search trees, and balanced binary search trees. In this tutorial, we will be working with Binary Search Trees. They are all created within a class, however.

Binary Search Trees (BST) function so that the values inputted follow a pattern. Look at this [image](BST_example.png) as an example where the node to the left of each value is less than the node above it and the nodes to the right are greater than the nodes above it. This makes a BST easily searchable as we know where to expect each value. In the image, the path for inserting the value 39 is shown in red. 39 is less than 50 so we go down the left side of the tree to the next node. 39 is greater than 34 for you follow the right node. Finally 39 is less than 42 and is inserted as the left node below 42.

## Inserting into a BST
In order to actually insert a value into a BST, we need to use recursion. Below is a sample of code that we could use to insert a value into a BST.
```
def insert(self, data):
	if self.root is None:
		self.root = BST.Node(data)
	else:
		self._insert(data, self.root)

def _insert(self, data, node):
	if data < node.data:
		if node.left is None:
			node.left = BST.Node(data)
		else:
			self._insert(data, node.left)
	elif data >= node.data:
		if node.right is None:
			node.right = BST.Node(data)
		else:
			self._insert(data, node.right)
```
This code would start with a call to the insert function. That function will check whether or not there is a root, if there is not, it will insert the value at the root. If there is a root, it will call _insert and pass the root in as the current node.  

After this point, everything else is done within the _insert function. First it will check if the value is less than the node. If it is, it will check if node.left exists. If it doesn't, the value is inserted in that place. If it does, we call _insert again with node.left as the new node.

The process is repeated with values greater than or equal to the node in the elif statement.

## Worked Example
In this example, we are trying to build a function that can take a BST and find the "k"th smallest item in a BST. For example, if we wanted k = 3, the function would traverse through the BST and find the 3rd smallest item.
```
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
```
[Full Example](example.py)  

## Problem To Solve
The problem we are going to try to solve is finding the max difference, where the larger number appears after the smaller number, between two items in a bst. The input is going to start as an array and you will have to put it into a bst in your code.
[Problem Code](problem.py)  
   
[Problem Solution](problem_solution.py)