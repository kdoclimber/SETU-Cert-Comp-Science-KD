def print_menu():
    print("1. Say hello")
    print("2. Add two numbers")
    print("3. Print a message")
    print("4. Exit")
    print("5. Hal. Exit")
    print("6. Square Your Number. Exit")

def say_hello():
    print("Hello")

def add_two_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Total:", num1 + num2)
    return num1, num2 # ken changed this, need it for hal()

def print_message(message):# ken changed this
    print(message)

def hal():
    hal1, hal2, = add_two_numbers()
    hal_message = f"Thanks, you added {hal1} and  {hal2}"
    print_message(hal_message)

def square_number():
    your_number = int(input("Please enter a number "))
    print(f"Your number is {your_number}")
    print(f"Your number squared is {your_number * your_number}")


def while_function():# I'm getting a red warning on line 56, still works ???
    choice = ""
    #print(f"choice = {choice}")
    while choice != "4":
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            say_hello()
        elif choice == "2":
            add_two_numbers()
        elif choice == "3":
            print_message("Your choice was 3")
        elif choice == "4":
            print("Goodbye")
        elif choice == "5":#ken
            hal()
            choice = "4"# stops the program
        elif choice == "6":#ken
            square_number()
            choice = "4"# stops the program
        else:
            print("Invalid choice")

while_function()
