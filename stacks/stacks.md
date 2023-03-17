# Stacks In Python

## What Is A Stack?
A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle, which means that the last element added to the stack will be the first one to be removed. For example, when using a stack, if we had a stack of numbers (1, 2, 3, 4) and we added 5 to the back of the stack, it would then contain (1, 2, 3, 4, 5). Since 5 was the "last in", when we remove a value, it would be the "first out" and the stack would contain (1, 2, 3, 4).

A stack is implemented using a list in Python.

## The "Undo" Function Of A Stack
Stacks have many uses, but one of the most common is that of being able to "undo" and action. Because of LIFO property of the stack, it is perfect for performing these undo operations. For example, if we were working with a dataset and created a new row that contained an error. We could use a stack that stored each row of the dataset to remove that error. Since it was the last inputted information into the stack, using the .pop() function would remove the incorrect row.

## Operations On A Stack
Along with the .pop() function, there are several other useful operations we can perform on stacks. If we had a stack that was named "stack", we could perform the following operations.  

### Pop
The "pop" operation will remove the item at the back of the stack (LIFO) from the stack and can even return it as a variable.  
```
stack = [1, 2, 3, 4, 5]  
removed = stack.pop()
``` 
After these operations:
- stack == [1, 2, 3, 4]
- removed == 5

### Append
The "append" operation will add an item to the back of the stack.
```
stack = [1, 2, 3, 4]
stack.append(5)
```
After this operation:
- stack == [1, 2, 3, 4, 5]

### Length
The "len" operation will return the amount of items in the stack
```
stack = [1, 2, 3, 4, 5]
length = len(stack)
```
After this operation:
- length == 5

## Worked Example
Suppose you have a program that needs to reverse the order of a string using a stack. Here's how you could use a stack to do that:
```
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
```
[Full Example](example.py)  
In this example we have a function that takes in a string variable (string) and appends each character of the string to a stack. Once the stack is completed, we loop through it and add pop each character off the stack and add it to a new string variable. This will reverse the string.   
For example, if we passed "hello" into the function, it would return "olleh".  

## Problem To Solve
Let's say you have a list of numbers, and you want to find the first number that is divisible by 3. You can use a stack to store the numbers as you iterate through the list, and pop the numbers off the stack until you find the first one that is divisible by 3. Follow the link to a python file with some starter code. You should complete the code and test the program.  
[Problem Code](problem.py)  
  
Once you are finished, check the solution and compare your code  
[Problem Solution](problem_solution.py)