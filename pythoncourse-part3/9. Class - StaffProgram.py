'''
Now that we have an understanding of how classes work, let’s explore the
meaning of self.

In order to explain self, we have to first discuss the concept of class vs
instance variables.

A class variable belongs to the class and is shared by all instances of that
class. It is defined outside any method in the class.

An instance variable, on the other hand, is defined inside a method and belongs
to an instance. It is always prefixed with the self keyword.

Let’s consider an example. Supposed Peter and John both work for a company
called ProgrammingLab. We can create a class called ProgStaff to store this
'''


class ProgStaff:
    companyName = 'ProgrammingLab'

    def __init__(self, pSalary):
        self.salary = pSalary

    def printInfo(self):
        print("Company name is", ProgStaff.companyName)
        print("Salary is", self.salary)


peter = ProgStaff(2500)
john = ProgStaff(2500)


print(peter.companyName)
print(john.companyName)

'''

The first few lines of the code above defines a class called ProgStaff.
This class has a variable called companyName that is not defined inside any
method.
Next, it has an __init__ method. Inside the __init__ method, it has a
variable called salary. This variable is prefixed with the self keyword.

'''

ProgStaff.companyName = 'ProgrammingSchool'

print(peter.companyName)
print(john.companyName)
print(peter.salary)
print(john.salary)

# Next, suppose the salary of peter is increased to 2700. We update it as follows:

peter.salary = 2700

# This change only affects the instance 'peter'. We can verify it by printing the
# salary of peter and john.

print(peter.salary)
print(john.salary)

'''

Finally, it also has a method called printInfo() that has self as a parameter.
This method simply prints the value of companyName and salary.
After defining the class, we created two instances of the ProgStaff class
called peter and john. We do not indent these two instantiation statements as
they are not part of the Staff class.
Now, let’s explore the difference between a class and instance variable.
Currently, the name of the company is ‘ProgrammingLab’. Suppose the name is
subsequently changed to ‘ProgrammingSchool’, we update it as follows:
'''

john.printInfo()

# When we call the instance method this way, Python passes in john to the self
# parameter implicitly for us. We do not have to do it ourselves.
# Alternatively, if we prefer, we can also use the class name to call the instance
# method. When we do it this way, we have to pass in the instance john
# ourselves as shown below:


ProgStaff.printInfo(john)

'''

In summary, the main differences between a class and instance variable are:
Class Variable

1. A class variable is defined outside any method in the class
2. It can be accessed outside the class using the class name
3. Changing it affects all instances of the class
Instance Variable

1. An instance variable is defined inside a method in the class and prefixed
with the self keyword.
2. It can be accessed outside the class using the name of the instance.
3. Changing it only affects the specific instance

In our example, companyName is a class variable while salary is an instance
variable.

Now that we understand what class and instance variables are, let us move on
to discuss the printInfo() method in the ProgStaff class.

This method is known as an instance method. An instance method is a method
that has self as one of its parameters. If the method has more than one
parameter, self must be the first parameter.

Inside the method, we use the class name to access the class variable
companyName. In contrast, we use the self keyword to access the instance
'''
