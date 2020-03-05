'''
Now we’ll learn what object-oriented programming is and how we
can write our own classes and create objects from them. 
We also discuss inheritance and cover some other advanced topics in objectoriented programming.
Let’s get started!

What is Object-Oriented Programming?

Simply stated, object-oriented programming is an approach to programming
that breaks a programming problem into objects that interact with each other.
Objects are created from templates known as classes. You can think of a class
as the blueprint of a building. An object is the actual “building” that we build
based on the blueprint.


To understand how object-oriented programming works, let’s start by coding a
simple class together.
'''


class Staff:
    def __init__(self, pPosition, pName, pPay):
        self.position = pPosition
        self.name = pName
        self.pay = pPay
        print('Creating Staff object')

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" % (self.position, self.name, self.pay)

    def calculatePay(self):
        prompt = '\nEnter number of hours worked for %s: ' % (self.name)
        hours = input(prompt)
        prompt = 'Enter the hourly rate for %s: ' % (self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours)*int(hourlyRate)
        return self.pay


officeStaff1 = Staff('Basic', 'Yvonne', 35)

print(officeStaff1.name)

print(officeStaff1.calculatePay())

print(officeStaff1.position)
