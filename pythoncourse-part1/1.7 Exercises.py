'''
Exercise 1: Mailing Address
(Solved, 6 Lines)
Create a program that displays your name and complete mailing address. The address
should be printed in the format that is normally used in the area where you live. Your
program does not need to read any input from the user.


Start coding below this line:'''


'''
Exercise 2: Hello Person
(2 Lines)
Write a program that asks the user to enter his or her name. The program should
respond with a message that says hello to the user, using his or her name
Start coding below this line:'''


'''
Exercise 3: Area of a Room
(Solved, 4 Lines)
Write a program that asks the user to enter the width and length of a room. Once
these values have been read, your program should compute and display the area of
the room. The length and the width will be entered as floating-point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
Start coding below this line:'''


'''
Exercise 4: Area of a Field
(Solved, 5 Lines)
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.
Start coding below this line:'''


'''
Exercise 5: Bottle Deposits
(Solved, 6 Lines)
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and two digits to the right of the decimal point.
Start coding below this line:'''

'''
Exercise 6: Tax and Tip
(Solved, 8 Lines)
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
Start coding below this line:'''

'''
Exercise 7: Even or Odd?
(Solved, 14 Lines)
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.
Start coding below this line:'''


'''
Exercise 8:Vowel or Consonant
(Solved, 9 Lines)
In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.
Start coding below this line:'''


'''
Exercise 9:Month Name to Number of Days
(Solved, 7 Lines)
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.
Start coding below this line:'''


'''
Exercise 10: Season from Month and Day
(Solved, 31 Lines)
The year is divided into four seasons: spring, summer, fall (or autumn) and winter.
While the exact dates that the seasons change vary a little bit from year to year
Start coding below this line:'''



































'''

# Exercise 1: Mailing Address
##
# Display a person’s complete mailing address.
#
print("Ben Stephenson")
print("Department of Computer Science")
print("University of Calgary")
print("2500 University Drive NW")
print("Calgary, Alberta T2N 1N4")
print("Canada")


# Exercise 2: User's Name
##
# Ask the users name and greets the user by its name.
#
name = input("Enter your name: ")
print(f'Hello {name}')

# Solution to Exercise 3:Area of a Room
##
# Compute the area of a room.
#
# The float function is used to convert the
# user’s input into a number.
# Read the dimensions from the user
length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))
# In Python, multiplication is performed using
# the operator.
# Compute the area of the room
area = length * width
# Display the result
print("The area of the room is", area, "square feet")


# Solution to Exercise 4:Area of a Field
##
# Compute the area of a field, reporting the result in acres.
#
SQFT_PER_ACRE = 43560
# Read the dimensions from the user
length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))
# Compute the area in acres
acres = length * width / SQFT_PER_ACRE
# Display the result
print("The area of the field is", acres, "acres")


# Solution to Exercise 5: Bottle Deposits
##
# Compute the refund amount for a collection of bottles.
#
LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25
# Read the number of containers of each size from the user
less = int(input("How many containers 1 litre or less? "))
more = int(input("How many containers more than 1 litre? "))
# Compute the refund amount
refund = less * LESS_DEPOSIT + more * MORE_DEPOSIT
# Display the result
print("Your total refund will be $%.2f." % refund)
# The %.2f format specifier indicates that a value should be formatted as a floating-point
# number with 2 digits to the right of the decimal point.


# Solution to Exercise 6:Tax and Tip
##
# Compute the tax and tip for a restaurant meal.
#
TAX_RATE = 0.05
TIP_RATE = 0.18
# My local tax rate is 5 % . In Python we represent 5 % and 18 % as 0.05 and 0.18 respectively.
# Read the cost of the meal from the user
cost = float(input("Enter the cost of the meal: "))
# Compute the tax and the tip
tax = cost * TAX_RATE
tip = cost * TIP_RATE
total = cost + tax + tip
# Display the result
print("The tax is %.2f and the tip is %.2f, making the total % .2f" %
      (tax, tip, total))
# The \ at the end of the line is called the line continuation character. It tells Python that the
# statement continues on the next line. Do not include any spaces or tabs after the \ character.


# Solution to Exercise 7: Even or Odd?
##
# Determine and display whether an integer entered by the user is even or odd.
#
# Read the integer from the user
num = int(input("Enter an integer: "))
# Dividing an even number by 2 always results in a remainder of 0. Dividing an odd number by 2 always results in a remainder of 1.
# Determine whether it is even or odd by using the
# modulus (remainder) operator
if num % 2 == 1:
    print(num, "is odd.")
else:
    print(num, "is even.")


# Solution to Exercise 8:Vowel or Consonant
##
# Determine if a letter is a vowel or a consonant.
#
# Read a letter from the user
letter = input("Enter a letter: ")
# This version of the program only works for lowercase letters. You can add support for uppercase letters by including additional comparisons that follow the same pattern.
# Classify the letter and report the result
if letter == "a" or letter == "e" or \
        letter == "i" or letter == "o" or \
        letter == "u":
    print("It’s a vowel.")
elif letter == "y":
    print("Sometimes it’s a vowel... Sometimes it’s a consonant.")
else:
    print("It’s a consonant.")


# Solution to Exercise 9:Month Name to Number of Days
##
# Display the number of days in a month.
#
# Read the month name from the user
month = input("Enter the name of a month: ")
# Compute the number of days in the month
days = 31
# Start by assuming that the number of days is 31. Then update the number of days if necessary.
if month == "April" or month == "June" or \
        month == "September" or month == "November":
    days = 30
elif month == "February":
    days = "28 or 29"
# When month is February, the value assigned to days is a string. This allows us to indicate that February can have either 28 or 29 days


# Solution to Exercise 10: Season from Month and Day
##
# Determine and display the season associated with a date.
#
# Read the date from the user
month = input("Enter the name of the month: ")
day = int(input("Enter the day number: "))
# This solution to the season identification problem uses several elif parts so that the conditions remain as simple as possible.
# Another way of approaching this problem is to minimize the number of elif parts by making the conditions more complex.
# Determine the season
if month == "January" or month == "February":
    season = "Winter"
elif month == "March":
    if day < 20:
        season = "Winter"
    else:
        season = "Spring"
elif month == "April" or month == "May":
    season = "Spring"
elif month == "June":
    if day < 21:
        season = "Spring"
    else:
        season = "Summer"
elif month == "July" or month == "August":
    season = "Summer"
elif month == "September":
    if day < 22:
        season = "Summer"
    else:
        season = "Fall"
elif month == "October" or month == "November":
    season = "Fall"
elif month == "December":
    if day < 21:
        season = "Fall"
    else:
        season = "Winter"
# Display the result
print(month, day, "is in", season)


'''