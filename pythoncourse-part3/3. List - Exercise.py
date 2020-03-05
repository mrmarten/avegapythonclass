# Exercise: Sorted Order

# Write a program that reads integers from the user and stores them in a list. Your
# program should continue reading values until the number you entered is reached. Then it should display
# all of the values entered by the user in ascending order, with one
# value appearing on each line. Use either the sort method or the sorted function
# to sort the list.
# Start coding from this line below:


'''
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'
'

# Solution to Exercise: Sorted Order
##
# Display a list of integers entered by the user in ascending order.
#
# Start with an empty list


NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " % i))
    NumList.append(value)

NumList.sort()

print("Element After Sorting List in Ascending Order is : ", NumList)

'''
