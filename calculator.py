# Simple calculator module
def add(a, b):
    # Function for Addition
    return a + b

def subtract(a, b):
    # Function for Substraction
    return a - b

def multiply(a, b):
    # Function for Multiplication
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
