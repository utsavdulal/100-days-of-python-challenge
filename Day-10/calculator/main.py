# calculator
from art import calculator_art
from clear_function import clear

# printing caclulator logo from art.py file
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


# operatios
operations = {"+": add, "-": subtract, "/": divide, "*": multiply}


def calculator():
    print(calculator_art)
    num1 = float(input("Enter your first number : "))

    for symbols in operations:  # for loop to print all the operation symbols
        print(symbols)
    should_continue = True

    while should_continue:
        operataion_symbol = input("pick an operation : ")
        num2 = float(input("Enter the next number : "))
        calculation_function = operations[operataion_symbol]
        first_answer = operations[operataion_symbol](num1, num2)

        print(f"{num1} {operataion_symbol} {num2} = {first_answer}")

        operataion_symbol = input("pick another operation : ")
        num3 = int(input("Enter the next number : "))
        calculation_function = operations[operataion_symbol]
        second_answer = calculation_function(first_answer, num3)

        print(f"{first_answer} {operataion_symbol} {num3} = {second_answer}")

        should_continue = input(
            f"Type 'y' to continue calculating with {second_answer}, or type 'n' to exit. :"
        ).lower()

        if should_continue == "y":
            num1 = second_answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()  # re call the function for fresh start
