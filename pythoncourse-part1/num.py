# Read a number from the user
num = float(input("Enter a number (statements): "))


if num > 0:
    adjective = " "
    if num >= 1000000:
        adjective = " really big "
    elif num >= 1000:
        adjective = " big "

    elif num < 0:
        result = "That’s a negative number"
    else:
        result = "That’s zero"
    result = "That’s a" + adjective + "positive number"
    print(result)
