################# START WITH OPENING importclass.py - read through it


# Other way to do it comment out below
# from importclass import SomeClass, SomeOtherClass


import importclass

#In the code above, we instantiated the objects by prefixing the class name with
#the file name, such as myclass.SomeClass() so that the compiler knows that
#SomeClass is in the file importclass.py.


sc = importclass.SomeClass()
sc.someMethod(100)
soc = importclass.SomeOtherClass()

# Otherway comment out
# sc = SomeClass()
