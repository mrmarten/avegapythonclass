# FIRST OPEN importedstaffclass.py FILE AND LOOK THROUGH IT

# Instantiating a Child Object
# Now that we have coded our child classes, let us create a separate .py file to
# make use of these classes.

import importedstaffclass
peter = importedstaffclass.BasicStaff('Peter', 0)

john = importedstaffclass.ManagementStaff('John', 0, 1000, 0)
print(peter)
print(john)
print('Peter\'s Pay = ', peter.calculatePay())
print('John\'s Pay = ', john.calculatePay())
print('John\'s Performance Bonus = ', john.calculatePerfBonus())

'''
Notice that this method uses the super() function again to call the
calculatePay() method in the base class. After calling the base class
method, we assign the result to the variable basicPay. basicPay is a local
variable that only exists within the calculatePay() method. Hence, you do
not need to prefix it with the keyword self.

Next, we add the value of basicPay to the instance variable allowance to
calculate the total pay of the management staff. We then assign it to the instance
variable pay and return this value in the next statement.
That concludes the calculatePay() method in the sub class.

Recall that we mentioned earlier that a sub class inherits all the variables and
methods from its base class? This means that we do not need to code a new
calculatePay() method for the subclass; it already exists. However, if we
choose to code a new version for the subclass, this new version replaces the
version that the sub class inherited. This is known as overriding, which is
what we did in this example.

Now, let us add a new method to the subclass. Suppose a management staff is
also entitled to performance bonus if his/her performance grade is an ‘A’. To
calculate the performance bonus of a management staff, we can add a new
method to the ManagementStaff class.

'''
