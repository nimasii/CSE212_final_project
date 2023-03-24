class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

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

# Print the original list
print("Original list:")
my_list.print_list()

# Reverse the list
my_list.reverse()

# Print the reversed list
print("Reversed list:")
my_list.print_list()
