# All 4 values are displayed when the print function executes
# because data is the entire list of values.

data = [2.71, 3.14, 1.41, 1.62]
print(data)


# Notice that printing the element at index 1 displays the second
# element in the list because the first element in the list has index 0.

data = [2.71, 3.14, 1.41, 1.62]
print(data[1])


# It creates a list that contains four elements,
# and then it replaces the element at index 2 with 2.30
data = [2.71, 3.14, 1.41, 1.62]
data[2] = 2.30
print(data)
