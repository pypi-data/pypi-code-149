result = 0
# input validation
def get_numbers():
    while True:
        try:
            num1 = input("Enter first number: ")
            if not num1.isdigit():
                raise ValueError("Invalid input. Only numbers are allowed.")
            num1 = float(num1)
            break
        except ValueError as error:
            print(error)
    while True:
        try:
            num2 = input("Enter second number: ")
            if not num2.isdigit():
                raise ValueError("Invalid input. Only numbers are allowed.")
            num2 = float(num2)
            break
        except ValueError as error:
            print(error)
    return num1, num2
# add calculation
def add(x, y):
    return x + y
# subtract calculation
def subtract(x, y):
    return x - y
# multiply calculation
def multiply(x, y):
    return x * y
# devide calculation with validation
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
        result = 0
    return result
# power calculation with validation
def power(x, y):
    try:
        result = x ** y
    except OverflowError:
        print("Result is to big")
        result = 0
    return result
# root calculation with validation
def n_root(x, y):
    if x < 0 and y % 2 == 0:
        raise ValueError("Can't find even root of negative number")
    return x ** (1/y)
# reset memory
def reset():
    global memory
    memory = 0
    print("Memory reset.")
