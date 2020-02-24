'''
As the programs that we write grow, we need to take steps to make them easier to
develop and debug. One way that we can do this is by breaking the program’s code
into sections called functions.
Functions serve several important purposes: They let us write code once and then
call it from many locations, they allow us to test different parts of our solution
individually, and they allow us to hide (or at least set aside) the details once we
have completed part of our program. Functions achieve these goals by allowing the
programmer to name and set aside a collection of Python statements for later use.
Then our program can cause those statements to execute whenever they are needed.
The statements are named by defining a function. The statements are executed by
calling a function. When the statements in a function finish executing, control returns
to the location where the function was called and the program continues to execute
from that location
'''

# Let's define a function called drawBox. That prints out four lines to form a box.


def drawBox():

    print("**********")
    print("*        *")
    print("*        *")
    print("**********")


# With this line we execute the function. We must call the function before the Python interpeter prints out the lines.
drawBox()
