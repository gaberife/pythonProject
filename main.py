from math import*

testInstance = "Print Variable"

def main():

    print('Hello World')
    # Global Variables
    string = "A string of characters"
    number = 100
    boolean = True
    friends = ["Caleb", "Beck", "Eve", "Anthony", "Madison", "Reid", "Poly"]

    print(maxNum(190,45,67))
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

def maxNum (num1, num2, num3):
    #Comparison operators
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3





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
    function = input("Type a function: ")
    num2 = float(input("Type another number: "))
    if function == "-":
        result = num1 - num2
    elif function == "+":
        result = num1 + num2
    elif function == "*":
        result = num1 * num2
    elif function == "/":
        result = num1 / num2
    else:
        result = "You input the wrong function"

    print("The answer is: ", result)





if __name__ == "__main__":
    main()
