def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Choose an operation.")
print("Add, Subtract, Multiply, or Divide?")

while True:
    choice = input("Enter choice(Add/Subtract/Multiply/Divide): ")

    if choice in ('Add', 'Subtract', 'Multiply', 'Division'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'Add':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'Subtract':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'Multiply':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'Divide':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid, try again.")