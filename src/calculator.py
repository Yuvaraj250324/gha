"""
Simple calculator module 
Provides basic arithmetic operations.
"""

def add(a, b):
    """
    Function for Addition
    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b

def subtract(a, b):
    """
    Function for Subtraction
    :param a: First number
    :param b: Second number
    :return: Difference of a and b
    """
    return a - b

def multiply(a, b):
    """
    Function for Multiplication
    :param a: First number
    :param b: Second number
    :return: Product of a and b
    """
    return a * b

def divide(a, b):
    """
    Function for Division
    :param a: First number
    :param b: Second number
    :return: Quotient of a and b
    :raises ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
