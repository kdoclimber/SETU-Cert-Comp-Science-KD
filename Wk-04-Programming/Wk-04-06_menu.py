choice = ""

while choice != "4":
    print("1. Say hello")
    print("2. Add two numbers")
    print("3. Print a message")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Hello")
    elif choice == "2":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Total:", num1 + num2)
    elif choice == "3":
        print("Python is fun")
    elif choice == "4":
        print("Goodbye")
    else:
        print("Invalid choice")