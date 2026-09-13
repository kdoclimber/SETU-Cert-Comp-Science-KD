numOne = float(input("Enter first number: "))#input is a string, so we need to convert it to a float so we can do math with it
numTwo = float(input("Enter second number: "))
total = numOne + numTwo #two floats can be added together, but a float and a string cannot be added together
print("Sum:",total)# comma automatically puts space between the string and the variable
print("Sum: " + str(total) + " Thanks for doing that!")#str() converts the variable to a string so it can be concatenated with other strings
print(type(total))
firstName = input("First name: ")
lastName = input("Last name: ")
print("Welcome,", firstName, lastName)
print(f"Hello, {firstName} {lastName}!")#f-string allows us

