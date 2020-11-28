from math import*

testInstance = "Print Variable"

def main():

    print('Hello World')
    # Global Variables
    string = "A string of characters"
    number = 100
    boolean = True
    friends = ["Caleb", "Beck", "Eve", "Anthony", "Madison", "Reid", "Poly"]
    #print(translator())
    print()
    #nestedForLoop(twoDLists())
    #maxNum(190,45,67)
    #monthConvert("test")
    #monthConvert("Apr")
    #exponentFunct(2,5)
    #loop()
    #forLoop(friends)
    #PrintVar()
    #stringVar()
    #userInput()
    #Lists(friends)
    #ListFunctions(friends)
    #functions(string, number, boolean, friends)
    #tuple()
    #result = returnInfo(number)
    #print(result)
    #calculator()

def translator():
    phrase = input("Type your secret message: ")
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "*"
        else:
            translation = translation + letter
    return translation


def twoDLists():
    numberGrid = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0]
    ]
    print("Number at Coordinate 2,1: ", numberGrid[2][1])
    #print(numberGrid[row][column])
    return numberGrid

def nestedForLoop(numberGrid):
    print("The Numbers in the Array")
    for row in numberGrid:
        for col in row:
            print(col, end = ' ')
        print()

def exponentFunct(base, power):
    result = 1
    for index in range(power):
        result = result * base
    print(result)

def forLoop(list):
    print("Letters: ")
    for letter in "Gabrielle":
        print(letter)
        #for every letter in Gabrielle print letter
    print("Friends: ")
    for friend in list:
        print(friend)
    print("Index: ")
    for index in range(3,6):
        print(index)
    print("Index of Friends")
    for index in range(2):
        print(list[index])


def loop():
    i = 1
    while i <= 10:
        print(i)
        i += 1
    print("Loop is over")


def monthConvert(month):
    #dictionary test that Convert 3 digit month name into full month name
    conversions = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December",
    }
    #implement except error catch in case program breaks
    print(conversions.get(month, "Not a valid value"))
    try:
        print(conversions[month])
    except:
        print("Not a valid value (alternate)")


def maxNum (num1, num2, num3):
    #Comparison operators
    if num1 >= num2 and num1 >= num3:
        print(num1)
    elif num2 >= num1 and num2 >= num3:
        print(num2)
    else:
        print(num3)

def PrintVar():
    print( "\n" + 'Test Case - ' + testInstance)

def dataTypesInVar(string, number, boolean):
    testInstance = "Data Types in Variables"
    print( "\n" + 'Test Case - ' + testInstance)
    print(string)
    print(number)
    print(boolean)
    print( string , number , boolean)
    #Comma instead of plus


def stringVar():
    testInstance = "String Variables"
    print( "\n" + 'Test Case - ' + testInstance )
    print(testInstance.isupper())
    print(testInstance.index("i"))
    print(testInstance.replace("String", "Number"))
    #Doesn't actually mutate anything the original variable
    print(testInstance)

def numVar(number):
    testInstance = "Number Variables"
    print("\n" + 'Test Case - ' + testInstance)
    print(str(number) + " is my favorite number")
    print("Number Functions")
    print("abs() is  Absolute Value. abs(number) = ", abs(number))
    print("pow(x,y) is power of x to y. pow(2,2)) = ", pow(2, 2))
    print("After importing from math import*")
    print("sqrt(X) is square root function. sqrt(100) =", sqrt(100))


def userInput():
    testInstance = "User Input"
    print("\n" + 'Test Case - ' + testInstance)
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    age = int(age)
    print("Hello " + name)

def Lists(list):
    testInstance = "Lists"
    print("\n" + 'Test Case - ' + testInstance)
    # Can have a list that consist of different data types
    print(list)  # All friends in list
    print(list[0])  # first friend in list
    print(list[1:6])

def ListFunctions(list):
    testInstance = "List Functions"
    print("\n" + 'Test Case - ' + testInstance)
    extra = ["Angel", "Marko", "Christian"]
    plusOne = "Dinora"
    # friends.extend(extra) #concats 2 lists
    list.append(plusOne)
    list.insert(3, "Dakota")
    list.remove("Madison")
    list.pop()  # removes last item
    list.sort()  # sorts in alphabetical (or ascending if numeric values)
    list.reverse()
    print(list)

def tuple():
    testInstance = "Tuple"
    print("\n" + 'Test Case - ' + testInstance)

    '''Data Structure where you can store different values and they are IMMUTABLE
    ***List are mutable, tuples are not*** '''

    coordinates = (4, 5)
    print(coordinates[0])

def functions(string, number, boolean, friends):
    testInstance = "Functions"
    print("\n" + 'Test Case - ' + testInstance)
    dataTypesInVar(string, number, boolean)  # calling a function that passes parameters (3)
    ListFunctions(friends)

def returnInfo(num):
    return num - 12

def calculator():
    testInstance = "ifStatements"
    print("\n" + 'Test Case - ' + testInstance)
    num1 = float(input("Type a number: "))
    operator = input("Type a function: ")
    num2 = float(input("Type another number: "))
    result = "null"
    if operator == "-":
        result = num1 - num2
    elif operator == "+":
        result = num1 + num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Divided by Zero")
    else:
        result = "You input the wrong function"

    print("The answer is: ", result)





if __name__ == "__main__":
    main()
