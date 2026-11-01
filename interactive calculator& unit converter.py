print("INTERACTIVE CALCULATOR")

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. KM to Miles")
    print("6. Celsius to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "7":
        print("Thank you!")
        break

    if choice in ["1", "2", "3", "4"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Answer:", a + b)
        elif choice == "2":
            print("Answer:", a - b)
        elif choice == "3":
            print("Answer:", a * b)
        elif choice == "4":
            if b != 0:
                print("Answer:", a / b)
            else:
                print("Cannot divide by zero")

    elif choice == "5":
        km = float(input("Enter kilometers: "))
        print("Miles:", km * 0.621371)

    elif choice == "6":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", (c * 9/5) + 32)

    else:
        print("Invalid choice!")