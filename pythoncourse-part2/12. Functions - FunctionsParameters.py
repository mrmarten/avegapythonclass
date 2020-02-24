'''
The drawBox function works correctly. It draws the particular box that it was
intended to draw, but it is not flexible, and as a result, it is not as useful as it could be.
In particular, our function would be more flexible and useful if it could draw boxes
of many different sizes.
Many functions take arguments which are values provided inside the parentheses
when the function is called. The function receives these argument values in parameter
variables that are included inside the parentheses when the function is defined. The
number of parameter variables in a function’s definition indicates the number of
arguments that must be supplied when the function is called.
'''

# Draw a box outlined with asterisks and filled with spaces.
# @param width the width of the box
# @param height the height of the box


def drawBox(width, height):
    # A box that is smaller than 2x2 cannot be drawn by this function
    if width < 2 or height < 2:
        print("Error: The width or height is too small.")
        quit()
# Draw the top of the box
    print("*" * width)
# Draw the sides of the box
    for i in range(height - 2):
        print("*" + " " * (width - 2) + "*")
# Draw the bottom of the box
    print("*" * width)


# For example, the following function call draws a box with a width of 15 characters and a
# height of 4 characters. Additional boxes can be drawn with different sizes by calling
# the function again with different arguments. Then we draw one sligtly bigger.

drawBox(15, 4)
drawBox(25, 8)
