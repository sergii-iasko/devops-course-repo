def add(num1, num2):
    return num1 + num2

def subt(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def divs(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    

print("Welcome to the Calculator Program!")

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

print('''
Please select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
''')

operation = int(input("Enter your choice (1-4): "))

funcDict = {
    1: [add(num1, num2), "addition"],
    2: [subt(num1, num2), "substraction"],
    3: [mult(num1, num2), "multiplication"],
    4: [divs(num1, num2), "division"]
}

while operation not in funcDict:
    print("Choose operation between 1-4: ")
    operation = int(input("Enter your choice (1-4): "))
else:
    print("The result of {} is: {}" .format(funcDict[operation][1], funcDict[operation][0]))