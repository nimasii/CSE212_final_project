'''
This is the function you will use. It should loop through the list of numbers passed in and return
a stack with all numbers in the list divisible by 3
'''
def find_divisible_by_three(numbers):
    # Create an empty stack to use for the problem
    stack = []

    # Loop through numbers while it is not empty
    while len(numbers) > 0:
        # Pop off the last value and assign it to a variable
        value = numbers.pop()
        # Check if the popped value is divisible by three
        if value % 3 == 0:
            # If the value is divisible by three, append it to the new stack
            stack.append(value)

    # Return our stack
    return stack

# Test cases for the problem
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #[9, 6, 3]
print(find_divisible_by_three(numbers))
numbers = [5, 10, 14, 19, 28, 54, 120, 200] #[120, 54]
print(find_divisible_by_three(numbers))
numbers = [5, 7, 8, 10, 11] #[]
print(find_divisible_by_three(numbers)) 