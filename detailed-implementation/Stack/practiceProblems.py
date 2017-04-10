#importing code that contains linked list implementation of a stack
from stack_LinkedList import *


#checks whether a string has a balanced set of opening and closing parenthesis.
#for example: is_Balanced('([()])') = True and is_Balanced('([)])') = False
def is_Balanced(str):
    stack = StackLinkedList()
    for char in str:
        if char == '(' or char == '[':
            stack.push(char)
        else:
            if stack.empty() == True:
                return False
            else:
                top = stack.pop()
                if (top == ']' and char == '(') or (top == ')' and char == '['):
                    return False
    return stack.empty()

print(is_Balanced(''))
print(is_Balanced('((('))
print(is_Balanced('[([])]'))
