# Linked Lists In Python

## What Is A Linked List?
A tree are somewhat similar to linked lists because nodes are linked together by pointers. They do have one main difference, however. Trees are able to connect to multiple different nodes, similar to a family tree where one person can be connected to multiple people.
  
There are three different types of trees; binary trees, binary search trees, and balanced binary search trees. They are all created within a class.

## Inserting into a BST


## Traversing a BST


## Worked Example
Suppose you have a program that needs to reverse the order of a list of items. We could achieve this using a linked list with the following code.
```
class LinkedList:
    def reverse(self):
        # Set the previous node to None, and the current node to the head of the list
        previous_node = None
        current_node = self.head

        # Loop through the list, reversing the direction of each node's pointer
        while current_node:
            # Set the next node to the next node after the current node
            next_node = current_node.next

            # Reverse the direction of the current node's pointer to point to the previous node
            current_node.next = previous_node

            # Update the previous and current nodes to point to the next nodes in the list
            previous_node = current_node
            current_node = next_node

        # Update the head pointer to point to the last node we processed, which is now the first node in the reversed list
        self.head = previous_node
```
[Full Example](example.py)  
This code creates a class for both node and linked list. It will then tak a linked list and reverse the order of the items in the list. For example, if we had a list that was in the order of 1, 2, 3, 4, 5. The code would reverse it to 5, 4, 3, 2, 1.

## Problem To Solve
The problem that you will need to solve will be adding some extra functions to the linked_list class. The functions that you will need to add are: insert_head, remove_tail, remove_head. After adding these function, test that everything is working as expected.
[Problem Code](problem.py)  
  
Once you are finished, check the solution and compare your code  
[Problem Solution](problem_solution.py)