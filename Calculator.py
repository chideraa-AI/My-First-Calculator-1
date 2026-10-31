# My First Python Calculator
# Built by Chideraa - FUASK - Day 1

# My First Calculator - Day 4 Upgrade
# FUASK AI Student - Chideraa-AI

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero"
    return a / b

# Real Calculator - Asks User!
print("=== My Calculator ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nResults:")
print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")

print("\nCalculator built by Chideraa-AI - FUASK")
