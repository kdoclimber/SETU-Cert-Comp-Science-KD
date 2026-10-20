def print_menu():
    print("")
    print("1. Welcome")
    print("2. Number by 2")
    print("3. Number. Is it even or odd?")
    print("4. Exit")
    print("")

#menu 1 and 4
def print_message(message):
    print(message)

#menu 2
def double_your_number(selection):
    num = int(input(f"You have selected {selection}. Enter your number: "))
    print(f"Your Number Doubled is {num * 2}")
    #return num * 2 
#menu 3
def number_even_or_odd(selection):
    your_number = int(input(f"You have selected {selection}. Please enter a number "))
    #print(f"Your number is {your_number}")
    #print(f"Your number is {your_number %2 }")
    if your_number %2 == 0:
         print(f"Your number is {your_number} is even")
    else:
          print(f"Your number is {your_number} is odd")
   


def while_function():
    choice = ""
    #print(f"choice = {choice}")
    while choice != "4":
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print_message("You have selected 1: Welcome!!")
        elif choice == "2":
            double_your_number("2")
        elif choice == "3":
            number_even_or_odd("3")
        elif choice == "4":
            print_message("You have selected 4: Goodbye!!")
        else:
            print_message("You have made an Invalid Selection")

while_function()
