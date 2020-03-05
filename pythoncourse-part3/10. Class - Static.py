'''
Now that we understand what self means, let us move on to discuss class and
static methods.

In the previous section, we mentioned that an instance method is a method that
has self as a parameter. This is the most common type of method and is the
only type of method that we’ve been using so far.

In addition to instance methods, Python also has class and static methods.
These types of methods are rarely used. Hence, we’ll only do a brief
discussion of them here.
'''


class MethodDemo:
    a = 1
    @classmethod
    def classM(cls):
        print("Class Method. cls.a = ", cls.a)

    @staticmethod
    def staticM():
        print("Static method")


'''
This class has a class variable a and two methods – classM() and
staticM().

The first method, classM(), is a class method.

To define a class method, we need to use the @classmethod decorator to
inform Python that what follows is a class method.

A class method is a method that has a class object (instead of self) as the first
parameter. cls is commonly used to represent that class object.
cls is sort of similar to self. 

The main difference is self refers to an
instance while cls refers to a class. As cls refers to the class itself, we can
use it to access our class variables. In our example, we used it to access the
class variable a.

To call a class method, we can either use the class name or the instance name.
In both cases, Python automatically passes in the class as the first argument to
the method.
'''
# For instance, to call classM() in the example above, we can write
MethodDemo.classM()

# Alternatively, we can instantiate a MethodDemo object and use it to call the
# method as shown below:

md1 = MethodDemo()
md1.classM()
md1.staticM()

'''
Besides instance and class methods, Python also has static methods. A static
method is a method that is not passed an instance or a class. It does not have
self or cls as the first parameter. To define a static method, we use the
@staticmethod decorator. To call a static method, we can either use the class
name or the instance name. For instance, to call staticM() in the example
above, we can write
'''

MethodDemo.staticM()

# Class and static methods are not very commonly used. In most cases, instance
# methods are all that is required in a Python class.
