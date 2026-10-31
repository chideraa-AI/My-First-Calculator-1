# My First Calculator - Day 6 Final Pro Version
# FUASK AI Student - Chideraa-AI - Complete App!

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

# Final Boss - Loop Calculator
print("=== Chideraa's Pro Calculator - Day 6 ===")

while True:
    print("\n--- MENU ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("\nChoose (1-5): ")

    if choice == "5":
        print("Thanks for using my calculator!")
        print("Bye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid! Choose 1-5")
        continue

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

print("\nBuilt by Chideraa-AI - FUASK - Pro Level!")
