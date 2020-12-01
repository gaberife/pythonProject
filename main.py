from math import*
import csv

#Modules Practice
import tools

testInstance = "Print Variable"

def main():

    print('Hello World')
    # Global Variables
    print()
    #writeFiles()
    #readFile()
    #print(translator())
    #nestedForLoop(twoDLists())
    #maxNum(190,45,67)
    #monthConvert("test")
    #monthConvert("Apr")
    #exponentFunct(2,5)
    #loop()
    #forLoop(tools.friends)
    #PrintVar()
    #stringVar()
    #userInput()
    #Lists(tools.friends)
    #ListFunctions(tools.friends)
    #functions(tools.string, tools.number, tools.boolean, tools.friends)
    #tuple()
    #result = returnInfo(tools.number)
    #print(result)
    #calculator()




def writeFiles():
    testInstance = "Writing Files"
    print( "\n" + 'Test Case - ' + testInstance)

    charactersLOTR = open("LOTR Characters.txt", "w") # "a" = appends
    test = open("Test.txt", "r")
    for character in test.readlines(): #puts file in an array
        charactersLOTR.write(character) #reads lines from array
    charactersLOTR.close()

def readFile():
    testInstance = "Reading Files"
    print( "\n" + 'Test Case - ' + testInstance)
    charactersLOTR = open("test.txt", "r") #"r" = read
    print(charactersLOTR.readable())

    arrayLOTR = charactersLOTR.readlines() #creates an array of characters
    print("Test again: ", arrayLOTR[3])

    for character in arrayLOTR: #puts file in an array
        print(character) #reads lines from array

    #print(charactersLOTR) #all contents
    charactersLOTR.close()


def translator():
    testInstance = "Translating secret messages"
    print( "\n" + 'Test Case - ' + testInstance)
    phrase = input("Type your secret message: ")
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "*"
        else:
            translation = translation + letter
    return translation


def twoDLists():
    testInstance = "2D Lists"
    print( "\n" + 'Test Case - ' + testInstance)
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
    testInstance = "Nested For Loop"
    print( "\n" + 'Test Case - ' + testInstance)
    print("The Numbers in the Array")
    for row in numberGrid:
        for col in row:
            print(col, end = ' ')
        print()

def exponentFunct(base, power):
    testInstance = "Exponent Function"
    print( "\n" + 'Test Case - ' + testInstance)
    result = 1
    for index in range(power):
        result = result * base
    print(result)

def forLoop(list):
    testInstance = "For Loop"
    print( "\n" + 'Test Case - ' + testInstance)
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
    testInstance = "Loops"
    print( "\n" + 'Test Case - ' + testInstance)
    i = 1
    while i <= 10:
        print(i)
        i += 1
    print("Loop is over")


def monthConvert(month):
    testInstance = "Keys"
    print( "\n" + 'Test Case - ' + testInstance)
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
    testInstance = "Comparison"
    print( "\n" + 'Test Case - ' + testInstance)
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
