'''
While Loops
A while loop causes one or more statements to execute as long as, or while, a
condition evaluates to True. Like an if statement, a while loop has a condition
that is followed by a body which is indented. If the while loop’s condition evaluates
to True then the body of the loop is executed. When the bottom of the loop body is
reached, execution returns to the top of the loop, and the loop condition is evaluated
again. If the condition still evaluates to True then the body of the loop executes
for a second time. Once the bottom of the loop body is reached for the second time,
execution once again returns to the top of the loop. The loop’s body continues to
execute until the while loop condition evaluates to False. When this occurs, the
loop’s body is skipped, and execution continues at the first statement after the body
of the while loop.
Many while loop conditions
'''

# Read the first value from the user
x = int(input("Enter an integer (0 to quit): "))
# Keep looping while the user enters a non-zero number
while x != 0:
    # Report the nature of the number
    if x > 0:
        print("That’s a positive number.")
    else:
        print("That’s a negative number.")
# Read the next value from the user
    x = int(input("Enter an integer (0 to quit): "))
