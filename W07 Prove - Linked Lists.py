"""
CSE212 
(c) BYU-Idaho
07-Prove - Problems

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class LinkedList:
    """
    Implement the LinkedList data structure.  The Node class below is an 
    inner class.  An inner class means that its real name is related to 
    the outer class.  To create a Node object, we will need to 
    specify LinkedList.Node
    """

    class Node:
        """
        Each node of the linked list will have data and links to the 
        previous and next node. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """
        Insert a new node at the front (i.e. the head) of the
        linked list.
        """
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node

    ###################
    # Start Problem 1 #
    ###################
    def insert_tail(self, value):
        """
        Insert a new node at the back (i.e. the tail) of the 
        linked list.
        """
        # Creates the new node to insert
        new_node = LinkedList.Node(value)

        # Check to see if the list is empty, if it is, inserts the node as the head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If there are already items in the list. Insert the new node at the end
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    #################
    # End Problem 1 #
    #################

    def remove_head(self):
        """ 
        Remove the first node (i.e. the head) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

    ###################
    # Start Problem 2 #
    ###################
    def remove_tail(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """
        # Checks to see if there is only one item in the list
        # If true, removes that item as head and tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If there are more than one item, remove only the last item
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    #################
    # End Problem 2 #
    #################

    def insert_after(self, value, new_value):
        """
        Insert 'new_value' after the first occurrence of 'value' in
        the linked list.
        """
        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.data == value:
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'
                if curr == self.tail:
                    self.insert_tail(new_value)
                # For any other location of 'value', need to create a 
                # new node and reconnect the links to insert.
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr       # Connect new node to the node containing 'value'
                    new_node.next = curr.next  # Connect new node to the node after 'value'
                    curr.next.prev = new_node  # Connect node after 'value' to the new node
                    curr.next = new_node       # Connect the node containing 'value' to the new node
                return # We can exit the function after we insert
            curr = curr.next # Go to the next node to search for 'value'

    ###################
    # Start Problem 3 #
    ###################
    def remove(self, value):
        """
        Remove the first node that contains 'value'.
        """
        # Creates a variable to use in th loop and sets it equal to the head
        current = self.head
        # Starts a loop that will end when current is equal to none
        while current is not None:
            # Checks to see if the input value is equal to the current item
            if current.data == value:
                # Checks to see if the current item is the head
                # If true, run the remove head function
                if current == self.head:
                    self.remove_head()
                # Checks to see if the current item is the tail
                # If true, run the remove tail function
                elif current == self.tail:
                    self.remove_tail()
                # If the item is in the middle of the list, remove it from the list
                else:
                    current.next.prev = current.prev
                    current.prev.next = current.next
                # Return after the item has been found and removed
                return
            # If the current item is not correct, continue the loop
            current = current.next

    #################
    # End Problem 3 #
    #################

    ###################
    # Start Problem 4 #
    ###################
    def replace(self, old_value, new_value):
        """
        Search for all instances of 'old_value' and replace the value 
        to 'new_value'.
        """
        # Creates a variable to use in the loop and sets it equal to the head
        current = self.head
        # Starts a loop that will end when current is equal to none
        while current is not None:
            # Check to see if the current value is equal to the target value
            # If true, set that value to the new_value
            if current.data == old_value:
                current.data = new_value
            # Continue the loop
            current = current.next

    #################
    # End Problem 4 #
    #################

    def __iter__(self):
        """
        Iterate forward through the Linked List
        """
        curr = self.head  # Start at the beginning since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    ###################
    # Start Problem 5 #
    ###################
    def __reversed__(self):
        """
        Iterate backward through the Linked List
        """
        # Set the value used in the loop to the tail since we are starting at the back
        current = self.tail
        # Loops through the list
        while current is not None:
            # Send back each item to the user
            yield current.data
            # Continue backwards through the list
            current = current.prev

    #################
    # End Problem 5 #
    #################

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

    
# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 1 TESTS ===========")
ll = LinkedList()
ll.insert_tail(1)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.insert_head(5)
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1]
ll.insert_tail(0)
ll.insert_tail(-1)
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1, 0, -1]

print("\n=========== PROBLEM 2 TESTS ===========")
ll.remove_tail()
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1, 0]
ll.remove_tail()
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1]
ll.remove_tail()
ll.remove_tail()
ll.remove_tail()
ll.remove_tail()
ll.remove_tail()
ll.remove_tail()
print(ll) # linkedlist[5]
ll.remove_tail()
print(ll) # linkedlist[]

ll.insert_tail(1)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.insert_head(5)

print("\n=========== PROBLEM 3 TESTS ===========")
ll.insert_after(3, 3.5)
ll.insert_after(5, 6)
print(ll) # linkedlist[5, 6, 4, 3, 3.5, 2, 2, 2, 1]
ll.remove(-1)
print(ll) # linkedlist[5, 6, 4, 3, 3.5, 2, 2, 2, 1]
ll.remove(3)
print(ll) # linkedlist[5, 6, 4, 3.5, 2, 2, 2, 1]
ll.remove(6)
print(ll) # linkedlist[5, 4, 3.5, 2, 2, 2, 1]
ll.remove(1)
print(ll) # linkedlist[5, 4, 3.5, 2, 2, 2]
ll.remove(7)
print(ll) # linkedlist[5, 4, 3.5, 2, 2, 2]
ll.remove(5)
print(ll) # linkedlist[4, 3.5, 2, 2, 2]
ll.remove(2)
print(ll) # linkedlist[4, 3.5, 2, 2]

print("\n=========== PROBLEM 4 TESTS ===========")
ll.replace(2, 10)
print(ll) # linkedlist[4, 3.5, 10, 10]
ll.replace(7, 5)
print(ll) # linkedlist[4, 3.5, 10, 10]
ll.replace(4, 100)
print(ll) # linkedlist[100, 3.5, 10, 10]


print("\n=========== PROBLEM 5 TESTS ===========")
print(list(reversed(ll)))  # [10, 10, 3.5, 100]