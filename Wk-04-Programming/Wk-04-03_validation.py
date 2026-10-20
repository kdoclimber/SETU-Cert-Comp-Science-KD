def get_valid_age():
    age = int(input("First-Please enter your age: "))
    print(type(age))
    while age < 1 or age > 120:
        print("Invalid age")
        age = int(input("Enter your age: "))

    print("Age accepted:", age)
    return age

your_age = get_valid_age()
print("Your age is: ", your_age)