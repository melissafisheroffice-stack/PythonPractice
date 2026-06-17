on = True

def add():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print (a + b)

def subtraction():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print (a - b)

def multiplication():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print (a * b)

def divide():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print (a / b)

while on:
    operation = input("Please type +, -, *, or /, or q ")
    if operation == "+":
        add()
    elif operation == "-":
        subtraction()
    elif operation == "*":
        multiplication()
    elif operation == '/':
        divide()
    elif operation == "q":
        on = False
    else:
        print("That operation is not available. ")





