# My First Calculator - Day 5 Menu Upgrade
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

# Menu-Driven Calculator
print("=== My Calculator - Day 5 ===")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("\nChoose operation (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
elif choice == "2":
    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
elif choice == "3":
    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
elif choice == "4":
    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid choice! Please choose 1-4")

print("\nBuilt by Chideraa-AI - FUASK")
