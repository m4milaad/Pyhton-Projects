from random import choice

import art


def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def sub(n1, n2):
    return n1 - n2


def calculator():
    print(art.logo)
    num1 = float(input("Enter number 1: "))
    cal = True
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }
    while cal:
        operation_symbol = input("Enter operator('+', '-', '*', '/'): ")
        if operation_symbol not in operations:
            print("Invalid operator")
            calculator()
        num2 = float(input("Enter number 2: "))
        result = operations.get(operation_symbol)(num1, num2)
        print(result)
        decision = input(
            'Enter "y" to work on previous result\nEnter "n" to start new calculations\nEnter "e" to exit: ').lower()
        if decision == "y":
            num1 = result
        elif decision == "n":
            calculator()
        else:
            cal = False


calculator()
