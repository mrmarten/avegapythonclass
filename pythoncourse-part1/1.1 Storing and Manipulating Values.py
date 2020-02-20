# A variable is a named location in a computer’smemory that holds a value.
x = 5


# The right side of an assignment statement can be an arbitrarily complex calculation
# that includes parentheses, mathematical operators, numbers, and variables
y = 1 + x ** 2


print(x)
print(y)


# The same variable can appear on both sides of an assignment operator. For example:
y = y - 6.2

print(f'New value of y is: {y}')


# 1.2 Calling Functions

r = round(y)
print(r)


'''
Python programs can read input from the keyboard by calling the input function.
This function causes the program to stop and wait for the user to type something.
'''

name = input("Enter your name: ")
quantity = int(input("How many items? "))
price = float(input("Cost per item? "))

total = quantity * price

print(f'total price is {total}')

print(1)
print("Hello!")
print(x)
# Multiple values can be printed with one function call by providing several arguments
# to the print function. The additional arguments are separated by commas.
# For example:
print("When x is", x, "the value of y is", y)
print("The product of", x, "and", y, "is", x * y)
