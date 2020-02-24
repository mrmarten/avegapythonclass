'''
Like while loops, for loops cause statements that only appear in a program once
to execute several times when the program runs. However the mechanism used to
determine howmany times those statements will execute is rather different for a for
loop.
A for loop executes once for each item in a collection. The collection can be a
range of integers, the letters in a string, or as we’ll see in later chapters, the values
stored in a data structure, such as a list. The syntactic structure of a for loop is
shown below, where <variable>,<collection> and <body> are placeholders
that must be filled in appropriately.

The body of the loop consists of one or more Python statements that may be
executed multiple times. In particular, these statements will execute once for each
item in the collection. Like a while loop body, the body of a for loop is indented.
Each item in the collection is copied into <variable> before the loop body
executes for that item. This variable is created by the for loop when it executes. It
is not necessary to create it with an assignment statement, and any value that might
have been assigned to this variable previously is overwritten at the beginning of each
loop iteration. The variable can be used in the body of the loop in the same ways that
any other Python variable can be used.
A collection of integers can be constructed by calling Python’s range function.
Calling range with one argument returns a range that starts with 0 and increases up
to, but does not include, the value of the argument. For example, range(4) returns
a range consisting of 0, 1, 2 and 3.
'''

# for <variable> in <collection>:
# <body>


# Read the limit from the user
limit = int(input("Enter an integer: "))
# Display the positive multiples of 3 up to the limit
print("The multiples of 3 up to and including", limit, "are:")
for i in range(3, limit + 1, 3):
    print(i)
