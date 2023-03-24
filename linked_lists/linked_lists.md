# Linked Lists In Python

## What Is A Linked List?
A linked list is a little different than other forms of memory because of the fact that it is not contiguous memory. Instead, it is stored in a "random" way. Each element in a linked list contains two values; the actual value of the node, and the link to the next node. In a linked list, the first node is called the "head". If you know where the head is, you will be able to access all the nodes in the list.  
  
Many linked lists also contain pointers back to the previous node, as well as pointer to the next node. This is called bi-directional linking. A linked list is created within a class.

## Inserting Into A Linked List
When inserting into a linked list, we have to consider the location we will be inserting into. Specifically, there are three different location we need to worry about. Inserting at the head, at the tail, or in the middle.

### Inserting At The Head
When inserting at the head, we take the following steps:
* Create a new node (example: new_node)
* Set the value of new_node.next = self.head
* Set the value of new_node.prev = new_node
* Set the value of self.head = new_node

### Inserting At The Tail
Inserting at the tail is very similar to inserting at the head. We just need to swap head for tail and next for prev.
* Create a new_node
* Set the value of new_node.prev = self.tail
* Set the value of new_node.next = new_node
* Set the value of self.tail = new_node

### Inserting In The Middle
Inserting in the middle is a little more complicated, but follows the same basic rules.
* Create a new_node
* Set new_node.prev = current
* Set new_node.next = current.next
* Set current.next.prev = new_node
* Set current.next = new_node 

## Removing From A Linked List
The process for removing from a linked list, similar to inserting, has different processes depending on if we are at the head, tail, or middle of the link.

### Removing From The Head
* Set the self.head.next.prev = none
* Set the self.head = self.head.next

### Removing From The Tail
* Set the self.tail.prev.next = none
* Set the self.tail = self.tail.prev

### Removing From The Middle
* Set the current.next.prev = current.prev
* Set the current.prev.next = current.next

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