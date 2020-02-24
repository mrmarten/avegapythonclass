'''
Our box-drawing function prints characters on the screen. While it takes arguments
that specify how the box will be drawn, the function does not compute
a result that needs to be stored in a variable and used later in the program. But
many functions do compute such a value. For example, the sqrt function in the
math module computes the square root of its argument and returns this value
so that it can be used in subsequent calculations. Similarly, the input function
reads a value typed by the user and then returns it so that it can be used later
in the program. Some of the functions that you write will also need to return
values.
A function returns a value using the return keyword, followed by the value
that will be returned. When the return executes the function ends immediately
and control returns to the location where the function was called.
'''

# Compute the sum of the first n terms of a geometric sequence.
# @param a the first term in the sequence
# @param r the common ratio for the sequence
# @param n the number of terms to include in the sum
# @return the sum of the first n term of the sequence


def sumGeometric(a, r, n):
    # Compute and return the sum when the common ratio is 1
    if r == 1:
        return a * n
# Compute and return the sum when the common ratio is not 1
    s = a * (1 - r ** n) / (1 - r)
    return s


print("Result of sum Geometric is {}".format(sumGeometric(4, 1, 5)))
