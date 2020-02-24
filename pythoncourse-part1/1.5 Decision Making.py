'''

Operator   Meaning
<          Less than
<=         Less than or equal to
>          Greater than
>=         Greater than or equal to
==         Equal to
!=         Not equal to


The following program reads a number from the user, uses two if statements to
store a message describing the number into the result variable, and then displays
the message. Each if statement’s condition uses a relational operator to determine
whether or not its body, which is indented, will execute.Acolon immediately follows
each condition to separate the if statement’s condition from its body.
'''

# Read a number from the user
num = float(input("Enter a number: "))

# Store the appropriate message in result

if num == 0:
    result = "The number was zero"
if num != 0:
    result = "The number was not zero"

# Display the message
print(result)


'''
An if-else statement consists of an if part with a condition and a body, and an
else part with a body (but no condition). When the statement executes its condition
is evaluated. If the condition evaluates to True then the body of the if part executes
and the body of the else part is skipped.
'''

# Read a number from the user
num = float(input("Enter a number: "))

# Store the appropriate message in result
if num == 0:
    result = "The number was zero"
else:
    result = "The number was not zero"

# Display the message
print(result)


'''

Let’s extend the previous example so that one message is displayed for positive
numbers, a different message is displayed for negative numbers, and yet another
different message is displayed if the number is zero. While we could solve this
problem using a combination of if and/or if-else statements, this problem is well
suited to an if-elif-else statement because exactly one of three alternatives
must be executed.

'''

# Read a number from the user
num = float(input("Enter a number: "))

# Store the appropriate message in result

if num > 0:
    result = "That’s a positive number"
elif num < 0:
    result = "That’s a negative number"
else:
    result = "That’s zero"

# Display the message
print(result)


'''
The body of any if part, elif part or else part of any type of if statement can
contain (almost) any Python statement, including another if, if-else, if-elif
or if-elif-else statement. When one if statement (of any type) appears in the
body of another if statement (of any type) the if statements are said to be nested.
The following program includes a nested if statement.
'''
# Read a number from the user
num = float(input("Enter a number (statements): "))


if num > 0:
    adjective = " "
    if num >= 1000000:
        adjective = " really big "
    elif num >= 1000:
        adjective = " big "
    result = "That’s a" + adjective + "positive number"
    elif num < 0:
        result = "That’s a negative number"
    else:
        result = "That’s zero"

    print(result)


'''
The following Python program uses the or operator to determine whether or not
the value entered by the user is one of the first 5 prime numbers. The and and not
operators can be used in a similar manner when constructing a complex condition.
'''

# Read an integer from the user
x = int(input("Enter an integer: "))
# Determine if it is one of the first 5 primes and report the result
if x == 2 or x == 3 or x == 5 or x == 7 or x == 11:
    print("That’s one of the first 5 primes.")
else:
    print("That is not one of the first 5 primes.")
