'''
Now, let us move on to some of the more advanced topics in object-oriented
programming. In this chapter, we’ll learn about inheritance, polymorphism and
overloading operators.


Inheritance is one of the key concepts of object-oriented programming. Simply
stated, inheritance allows us to create a new class from an existing class so
that we can effectively reuse existing code.

Writing the Child Class

To understand how inheritance works, let us expand on the Staff class that we
wrote earlier. To recap, our Staff class has the following
attributes.


The best way to do this is to create a sub class. A sub class is also known as a
derived class or a child class. The class from which it is derived is known as
a base class, a super class or a parent class.

The main feature of a sub class is that it inherits all the variables and methods
from the parent class. In other words, it can use those variables and methods as
if they are part of its own code without having to code them again. In addition,
a sub class can have additional variables and methods that do not exist in the
parent class. Let’s look at how this can be done.

'''

# Python Special Methods
# Now that we understand how inheritance and overriding works, let us move on
# to talk about special methods.
# Python comes with a large number
# of special methods. These methods are also known as magic methods and are
# always surrounded by double underscores. Two of the magic methods that we
# have encountered so far are __init__ and __str__.
# One of the magical properties of a special method is that you do not invoke it
# directly. For instance, when you wanted to print information about the instance
# officeStaff1 , you do not write

# print(officeStaff1.__str__())

# Instead, you simply write
# print(officeStaff1)

# Python will invoke the necessary special method behind the scene.
# Another property of special methods is that they can be overridden to suit our
# needs. The __str__ method is commonly overridden to provide a more human
#readable string representation of a class.#


class Staff:
    def __init__(self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print('Creating Staff object')

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" % (self._position, self.name, self.pay)

    def calculatePay(self):
        prompt = '\nEnter number of hours worked for %s: ' % (self.name)
        hours = input(prompt)
        prompt = 'Enter the hourly rate for %s: ' % (self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours)*int(hourlyRate)
        return self.pay

    @property
    def position(self):
        print("Getter Method")
        return self._position

    @position.setter
    def position(self, value):

        if value == 'Manager' or value == 'Basic':
            self._position = value
        else:
            print('Position is invalid. No changes made.')


class ManagementStaff(Staff):
    def __init__(self, pName, pPay, pAllowance, pBonus):
        super().__init__('Manager', pName, pPay)
        self.allowance = pAllowance
        self.bonus = pBonus
        Staff.__init__(self, 'Manager', pName, pPay)

    def calculatePay(self):
        basicPay = super().calculatePay()
        self.pay = basicPay + self.allowance
        return self.pay

    def calculatePerfBonus(self):
        prompt = 'Enter performance grade for %s: ' % (self.name)
        grade = input(prompt)
        if (grade == 'A'):
            self.bonus = 1000
        else:
            self.bonus = 0
        return self.bonus


class BasicStaff(Staff):
    def __init__(self, pName, pPay):
        super().__init__('Basic', pName, pPay)


officeStaff1 = Staff('Basic', 'Yvonne', 35)

print(officeStaff1.name)

print(officeStaff1.calculatePay())

print(officeStaff1.position)

officeStaff1.position = 'Manager'

print(officeStaff1.position)

officeStaff1.position = 'CEO'
