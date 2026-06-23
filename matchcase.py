print("Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

match choice:
    case 1:
        print("Result =", a + b)

    case 2:
        print("Result =", a - b)

    case 3:
        print("Result =", a * b)

    case 4:
        if b != 0:
            print("Result =", a / b)
        else:
            print("Division by zero is not allowed")

    case _:
        print("Invalid Choice")