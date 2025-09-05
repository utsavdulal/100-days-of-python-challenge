from art import calculator_art
from clear_function import clear

print(calculator_art)


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


operations = {"+": add, "-": subtract, "/": divide, "*": multiply}

num1 = int(input("Enter your first number : "))

for symbols in operations:
    print(symbols)
operataion_symbol = input("pick an operation : ")

num2 = int(input("Enter your second number : "))

answer = operations[operataion_symbol](num1, num2)

print(f"{num1} {operataion_symbol} {num2} = {answer}")
