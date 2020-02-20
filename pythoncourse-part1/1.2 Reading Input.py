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
# print(x)
# Multiple values can be printed with one function call by providing several arguments
# to the print function. The additional arguments are separated by commas.
# For example:
print(f"When x is", x, "the value of y is", y)
print("The product of", x, "and", y, "is", x * y)
