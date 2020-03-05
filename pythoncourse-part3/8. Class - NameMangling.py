'''
Previously we mentioned that if we do not want other
programmers to access a certain variable directly, we indicate that by adding a
single underscore in front. We then code properties to control their access.
However, even if we do so, other programmers can still access that variable if
they want to. In the previous example, they can simply type

officeStaff1._position

In Python, there is no way to really hide a variable and prevent other users
from accessing it. However, if you really want to send a strong signal to other
programmers that a certain variable should not be modified, you can add
double underscores to the front of the variable name.

'''


class A:
    def __init__(self):
        self.__x = 5
        self._y = 6

# The code above defines a class called A. This class has two variables __x
# (with double underscores) and _y (with single underscore)


# Next, we instantiate a class A object
varA = A()


print(varA._y)
# you’ll get:6
# as the output. However, if you uncomment the line below you get


# varA.__x
# After error is displayed please but back the # to comment out the Error to proceed.

'''
You’ll get an error.

Why is that so? This is because when you add double underscores in front,
Python does what is known as name mangling.

Essentially, when the Python
compiler encounters a variable with two leading underscores, it transforms the
name by adding a single underscore and the class name in front of the variable
name. 

In other words, when it sees __x, it changes the name to _A__x.
This means that when we add a double underscore in front of a variable name,
other programmers cannot access the variable by simply typing the variable
name (__x in this case). This makes it harder for them to access the variable.

However, if they so desire, they can still access it by typing
'''
print(varA._A__x)

'''
They’ll get 5 as the output.

In other words, there is no way to absolutely restrict access to a variable in
Python. You can use underscores to make it more difficult to access, but a
determined programmer can still access it. As we mentioned earlier, in Python,
we are all consenting adults. Hence, we are expected to behave responsibly
and not modify variables that we are told not to.
'''
