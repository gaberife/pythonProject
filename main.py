from math import*

print('Hello World')
'''
testInstance = "Print Variable"
print( "\n" + 'Test Case - ' + testInstance)

testInstance = "Data Types in Variables"
print( "\n" + 'Test Case - ' + testInstance)
'''
string = "A string of characters"
number = 100
boolean = True
'''

print(string)
print(number)
print(boolean)
print( string , number , boolean)
#Comma instead of plus

testInstance = "String Variables"
print( "\n" + 'Test Case - ' + testInstance )

print(testInstance.isupper())
print(testInstance.index("i"))
print(testInstance.replace("String", "Number"))
#Doesn't actually mutate anything the original variable
print(testInstance)

testInstance = "Number Variables"
print( "\n" + 'Test Case - ' + testInstance)
print(str (number) + " is my favorite number")


print("Number Functions")
print("abs() is  Absolute Value. abs(number) = ", abs(number))
print("pow(x,y) is power of x to y. pow(2,2)) = ", pow(2,2))
print("After importing from math import*")
print("sqrt(X) is square root function. sqrt(100) =", sqrt(100))

testInstance = "User Input"
print( "\n" + 'Test Case - ' + testInstance)
name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
print("Hello " + name)

testInstance = "Calculator"
print( "\n" + 'Test Case - ' + testInstance)
num1 = input("Enter a number: ")
num2 = input("Enter Another number: ")
#int(x) to convert user string input into integer
#float(x) to convert user string to a float number
result = float(num1) + float(num2)
print(result)
'''
testInstance = "Lists"
print("\n" + 'Test Case - ' + testInstance)
