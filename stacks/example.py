def reverse_string(string):
    stack = []
    reversed_string = ""

    # push each character of the string onto the stack
    for char in string:
        stack.append(char)

    # pop each character off the stack and add it to the reversed string
    while len(stack) != 0:
        reversed_string += stack.pop()

    return reversed_string

# Test Case
string = "hello"
print(reverse_string(string))
string = "The Big Brown Bear"
print(reverse_string(string))