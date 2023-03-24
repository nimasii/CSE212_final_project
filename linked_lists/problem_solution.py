class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)

        if not self.head:
            # If the list is empty, the new node becomes the head
            self.head = new_node
            return

        # Find the last node in the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # Insert the new node after the last node
        last_node.next = new_node

    def remove_head(self):
        if not self.head:
            # If the list is empty, there is nothing to remove
            return

        # Remove the head node and update the head pointer
        self.head = self.head.next

    def remove_tail(self):
        if not self.head:
            # If the list is empty, there is nothing to remove
            return

        # If there is only one node in the list, remove it
        if not self.head.next:
            self.head = None
            return

        # Find the second-to-last node in the list
        second_to_last_node = self.head
        while second_to_last_node.next.next:
            second_to_last_node = second_to_last_node.next

        # Remove the last node in the list
        second_to_last_node.next = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

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


# Test Case
# Create a new linked list
my_list = LinkedList()

# Append some values to the list
my_list.insert_tail(1)
my_list.insert_tail(2)
my_list.insert_tail(3)

my_list.insert_head(4)
my_list.insert_head(5)
my_list.insert_head(6)

my_list.remove_tail()

my_list.remove_head()

# Print the original list
print("Original list:")
my_list.print_list()

# Reverse the list
my_list.reverse()

# Print the reversed list
print("Reversed list:")
my_list.print_list()
