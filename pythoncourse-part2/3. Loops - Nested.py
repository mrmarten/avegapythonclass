'''
The statements inside the body of a loop can include another loop. When this happens,
the inner loop is said to be nested inside the outer loop. Any type of loop can be
nested inside of any other type of loop. For example, the following program uses a
for loop nested inside a while loop to repeat messages entered by the user until
the user enters a blank message.
'''

# Read the first message from the user
message = input("Enter a message (blank to quit): ")
# Loop until the message is a blank line
while message != "":
    # Read the number of times the message should be displayed
    n = int(input("How many times should it be repeated? "))
# Display the message the number of times requested
    for i in range(n):
        print(message)
# Read the next message from the user
message = input("Enter a message (blank to quit): ")
