'''

Next, let’s learn how to use this class.

In order to use the class, we have to create an object from it. This is known as
instantiating an object. An object is also known as an instance. Although there
are some differences between an object and an instance, these are more
semantic differences and the two words are frequently used interchangeably.

'''


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


'''
In Python programming, there is a commonly used phrase that says "we're all
consenting adults here". We are all expected to behave like an adult. Adding a
single underscore in front of a variable tells other programmers that you're
trusting them to behave responsibly and not access that variable directly unless
they have a compelling reason to. However technically, there is nothing
stopping them from accessing the variable. If they so desire, they can still
access it by writing
'''
# Now we are ready to instantiate a Staff object.
officeStaff1 = Staff('Basic', 'Yvonne', 35)

# For instance, to access the instance variable name, we type
print(officeStaff1.name)

print(officeStaff1.calculatePay())

# To access the variable pay
officeStaff1.pay

print(officeStaff1.position)

# To change variable position and print it again
# change variable position
officeStaff1.position = 'Manager'

print(officeStaff1.position)


# Next, let’s try to change the position to ‘CEO’. Type the following into Shell
officeStaff1.position = 'CEO'
'''
You’ll get
Position is invalid. No changes made.
as the output.
This demonstrates that the setter method has prevented us from changing the
position of a staff to an invalid value. You can verify that position is not
changed by typing
'''
