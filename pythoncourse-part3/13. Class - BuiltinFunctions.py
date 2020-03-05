'''
Python Built-in Functions for Objects

We’ve covered most of the topics in object-oriented programming. Before we
end this chapter, let’s look at some special built in functions that Python has for
objects. To explore some of these functions, let’s consider the two classes
below. 
'''


class ParentClass:
    def __init__(self):
        self.a = 1
        print("Parent Class Object Created")

    def someMethod(self):
        print("Hello")


class ChildClass(ParentClass):
    def __init__(self):
        print("Child Class Object Created")


parent = ParentClass()
child = ChildClass()

'''

Now, we are ready to test some of the built-in Python functions below. Run the
file to try the following commands in Python Shell.
isinstance()

This function takes in two arguments. It checks if the first argument is an
instance of the second argument (or an instance of a sub class of the second
argument). 
The second argument can be a class or a built-in type in Python. It
can also be a tuple consisting of more than one class or type.

If the second argument is not a valid class or type (or a tuple of classes or
types), an exception is raised.
'''

print(isinstance(parent, ParentClass))
# You’ll get True as parent is an instance of ParentClass

print(isinstance(5, int))
# You’ll get True as 5 is an instance of int. (int is a built-in type in Python for integers.)

print(isinstance(child, ParentClass))
# You’ll get True as child is an instance of ChildClass, which is a subclass of ParentClass.

print(isinstance(parent, (ParentClass, int)))
# You’ll get True as parent is an instance of ParentClass, which is one of the types in the tuple (ParentClass, int).

print(isinstance(parent, ChildClass))
# You’ll get False as an instance of the parent class is not considered an
# instance of the child class.

try:
    isinstance(parent, MyClass)
except NameError:
    print("No such class")

# You’ll get
# No such class
# as the output.
