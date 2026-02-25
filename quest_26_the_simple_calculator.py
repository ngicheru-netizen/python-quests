#!/usr/bin/env python3

#will create 4 variables for addition, subtraction, multiplication and division

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#user input

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operation = input("Please enter what operation you'd like to use(add, subtract, multiply, divide): ")

#call functions

if operation == "add":
    result = add(num1, num2)
elif operation == "subtract":
    result = subtract(num1, num2)
elif operation == "multiply":
    result = multiply(num1, num2)
elif operation == "divide":
    result = divide(num1, num2)
else:
    print("Invalid Operation")
    result = None

if result is not None:
    print (f"Result {result}")
