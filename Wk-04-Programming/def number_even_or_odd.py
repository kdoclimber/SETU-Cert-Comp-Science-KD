def number_even_or_odd():
    your_number = int(input("Please enter a number "))
    #print(f"Your number is {your_number}")
    #print(f"Your number is {your_number %2 }")
    if your_number %2 == 0:
         print(f"Your number is {your_number} is even")
    else:
          print(f"Your number is {your_number} is odd")

number_even_or_odd()