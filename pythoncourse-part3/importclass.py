'''
We’ve covered quite a few object-oriented concepts in this chapter. Before we
end this chapter, let us learn how to import a class into an application.

A class can also be
created as a separate file and imported into an application. To do that, we need
to save the class as a separate file with the .py extension. 

We then import it using the file name.
'''

class SomeClass:
    def __init__(self):
        print('This is SomeClass')

    def someMethod(self, a):
        print('The value of a is', a)
        self.b = 5


class SomeOtherClass:
    def __init__(self):
        print('This is SomeOtherClass')

'''
This file consists of two classes: SomeClass and SomeOtherClass. We can
create another .py file and import these two classes using the file name
. We can then use this file name to access the classes inside the file.

Now run the callingclass.py file
'''