'''


Exercise 1: Print Game Instructions

The first function is called printInstructions(). It has one parameter
called instruction and simply uses the built-in print() function to print the
value of instruction onto the display. Try coding this function yourself.

Exercise 2: Getting the User’s Score

The second function is called getUserScore(). This function accepts one
parameter, userName.
The function first opens a file called userScores.txt in 'r' mode.
userScores.txt looks something like this:

Ann, 100
Benny, 102
Carol, 214
Darren, 129

Each line records the information of one user. The first value is the user’s
username and the second is the user’s score.
Next, the function reads the file line by line using a for loop.

Within the for loop, each line is split using the split() function (refer to
Appendix A for an example on using the split() function) and the results of
the split() function is stored in a list called content. Try coding this first.
Next, still within the for loop, the function checks if any of the lines has the
same username as the value that is passed in as the parameter. If there is, the
function closes the file and returns the score beside that username.

After looping through the file, if the function does not find a match for the
username, it exits the for loop, closes the file and returns the string “-1”.

Clear so far? Try coding this function.
Done?

Now we need to make some modifications to our code. When opening our file
previously, we used the 'r' mode. This helps to prevent any accidental
changes to the file. However, when opening a file in 'r' mode, an IOError
occurs if the file does not already exist. Hence when we run the program for
the first time, we’ll end up with an error since the file userScores.txt does not
exist previously. To prevent this error, we can do either of the following:
Instead of opening the file in 'r' mode, we can open it in 'w' mode. When
opening in 'w' mode, a new file will be created if the file does not exist
previously. The risk with this method is we may accidentally write to the file,
which results in all previous content being erased. However, since our
program is a small program, we can check through our code carefully to
prevent any accidental writing.

The second method is to use a try, except statement to handle the IOError.
To do that, we need to put all our previous codes in the try block, then use
except IOError: to handle the ‘File not found’ error. In the except block,
we’ll inform users that the file is not found and then proceed to create the file.
We’ll use the open() function with 'w' mode to create it. The difference here
is we use the 'w' mode only when the file is not found. Since the file does not
exist initially, there is no risk of erasing any previous content. After creating
the file, we close the file and return the string “-1”.

Try doing this yourself. You can choose either of the above methods to
complete this exercise. The answer provided uses the second method. Once
you are done, we can move on to Exercise 1.3.

Exercise 3: Updating the User’s Score

In this exercise, we’ll define another function called updateUserScore().
This function requires us to use two built-in functions from the os module: the
remove() and rename() functions.

Try importing these two functions yourself.
Done? Let’s move on.

The updateUserScore() function has three parameters: newUser, userName
and score. Let’s add these parameters to the function definition.
newUser can either be True or False.

If newUser is True, the function will open the file userScores.txt in append
mode and add the user’s userName and score to the file using the write()
function. After that, it’ll close the file. Try coding this if block yourself.
Else, if newUser is False, the function will update the user’s score in the file.
However, there is no function in Python (or most programming languages for
that matter) that allows us to update a text file. We can only write or append to
it, but we cannot update it.

Hence, we need to create a temporary file. This is a fairly common practice in
programming. Let’s call this file userScores.tmp. Recall that we can create a
new file by opening it in 'w' mode. Let’s create the file now. We need to
create it inside the else block.

mode as we will only be reading from it. Next, we need to loop through
userScores.txt line by line using a for loop and split the line using the
split() function. We assign the result of the split() function to a list called
content.

For each line, we check if the username on that line is the same as the one
provided by the parameter userName. If it is, we'll change the score to the new
score provided by the parameter score and write this updated line to the
userScores.tmp file.

If it is not the same, we'll simply write the original line to the temporary file
userScores.tmp.

For instance, if the arguments provided to the function are False, 'Benny' and
'158' (i.e. updateUserScore(False, 'Benny', '158')), the table below
shows the difference between the original userScores.txt and the new

userScores.tmp file.
userScores.txt

Ann, 100
Benny, 102
Carol, 214
Darren, 129
userScores.tmp
Ann, 100
Benny, 158
Carol, 214
Darren, 129

Try doing this step yourself.
Once we are done with that, we exit the for loop and close both files. We then
delete userScores.txt. Finally, we rename userScores.tmp to userScores.txt.

Clear? Try coding the else block yourself.

Code the solution below this line:

'''


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
''
def printInstructions(instruction):
    print(instruction)


def getUserScore(userName):
    try:
        input = open('userScores.txt', 'r')
        for line in input:
            content = line.split(', ')
            if content[0] == userName:
                input.close()
                return content[1]
        input.close()
        return '-1'
    except IOError:
        print("File not found. A new file will be created.")
        input = open('userScores.txt', 'w')
        input.close()
        return '-1'


def updateUserScore(newUser: int, userName, score):
    from os import remove, rename
    if newUser == True:
        input = open('userScores.txt', 'a')
        input.write(userName + ', ' + score + '\n')
        input.close()
    else:
        temp = open('userScores.tmp', 'w')
        input = open('userScores.txt', 'r')
        for line in input:
            content = line.split(', ')
            if content[0] == userName:
                temp.write(userName + ', ' + score + '\n')
            else:
                temp.write(line)
                input.close()
                temp.close()
                remove('userScores.txt')
                rename('userScores.tmp', 'userScores.txt')


print(printInstructions("This is how you do it! 1... first 2... then this 3... finally"))

print(getUserScore("Ann"))

updateUserScore(1, "Marty", "200")

# print(getUserScore("Marten"))

'''
