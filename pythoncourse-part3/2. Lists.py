
## Loops and Lists

# Initialize data and total
data = [2.71, 3.14, 1.41, 1.62]
total = 0
# Total the values in data
for value in data:
    total = total + value
# Display the total
print("The total is", total)


# Initialize data
data = [0, -1, 4, 1, 0]
# Loop while i is a valid index and the value at index i is not a positive value
i = 0
while i < len(data) and data[i] <= 0:
    i = i + 1
# If i is less than the length of data then the loop terminated because a positive number was
# found. Otherwise i will be equal to the length of data, indicating that a positive number
# was not found.
if i < len(data):
    print("The first positive number is at index", i)
else:
    print("The list does not contain a positive number")


# Adding Elements to a List

# Elements can be added to the end of an existing list by calling the append method. It
# takes one argument, which is the el

data = [2.71, 3.14, 1.41, 1.62]
data.append(2.30)
print(data)


# Elements can be inserted at any location in a list using the insert method. It
# requires two arguments, which are the index at which the element will be inserted
# and its value.

data = [2.71, 3.14, 1.41, 1.62]
data.insert(2, 2.30)
print(data)

# Removing Elements froma List

data = [2.71, 3.14, 1.41, 1.62]
data.remove(1.62)  # Remove 1.62 from the list
last = data.pop()  # Remove the last element from the list
print(data)
print(last)

# Rearranging the Elements in a List

# Create a list
data = [2.71, 3.14, 1.41, 1.62]
# Swap the element at index 1 with the element at index 3
temp = data[1]
data[1] = data[3]
data[3] = temp
# Display the modified list
print(data)

# Searching a List

# Read integers from the user until a blank line is entered and store them all in data
data = []
line = input("Enter an integer (blank line to finish): ")
while line != "":
    n = int(line)
    data.append(n)
    line = input("Enter an integer (blank line to finish): ")
# Read an additional integer from the user
x = int(input("Enter one additional integer: "))
# Display the index of the first occurrence of x (if it is present in the list)
if x in data:
    print("The first", x, "is at index", data.index(x))
else:
    print(x, "is not in the list")
