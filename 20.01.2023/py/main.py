# Given a mathematical expression as a string you must return the result as a number.
# Number may be both whole numbers and/or decimal numbers. The same goes for the returned result.
# Need to support the following mathematical operators:
##    Multiplication *
##    Division / (as floating point division)
##    Addition +
##    Subtraction -
# Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -.
# Need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6
# An addition to this rule is that the minus sign (-) used for negating numbers and parentheses 
# will never be separated by whitespace.


class WrongType(Exception):
    pass

# Solution one
def calc(expression):
    # Initialize the stack and output list
    stack = []
    output = []
    # Define the precedence of operators
    precedence = {'+':1,'-':1,'*':2,'/':2}
    # Iterate through each character in the expression
    for char in expression:
        # If the character is a digit, add it to the output list
        if char.isdigit() or char == '.':
            output.append(char)
        # If the character is an operator
        elif char in '+-*/':
            # Pop operators from the stack and add them to the output list
            # until the stack is empty or the top operator has lower precedence
            while stack and precedence.get(char,0) <= precedence.get(stack[-1],0):
                output.append(stack.pop())
            # Push the current operator onto the stack
            stack.append(char)
        # If the character is an open parenthesis, push it onto the stack
        elif char == '(':
            stack.append(char)
        # If the character is a close parenthesis
        elif char == ')':
            # Pop operators from the stack and add them to the output list
            # until an open parenthesis is found
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            # Pop the open parenthesis from the stack
            stack.pop()
    # After iterating through all characters in the expression,
    # pop any remaining operators from the stack and add them to the output list
    while stack:
        output.append(stack.pop())
    # Iterate through the output list and use a stack to evaluate the postfix notation
    for char in output:
        if char.isdigit() or char == '.':
            stack.append(float(char) if '.' in char else int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
    # Return the final value on the stack as the result
    return stack[0]

import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('')

    start_time = time.time()
    end_time = time.time()
    print('first approach timestamp', end_time - start_time)
