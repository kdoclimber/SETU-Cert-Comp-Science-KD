

age = int(input("Age (0 to 25): "))

if 0 <= age <= 25:
    print("Age accepted")
else:
    print("Age must be between 0 and 25")


age2 = int(input("Age2 (0 to 25): "))

while age2 < 0 or age2 > 25:
    print("Please enter an age2 from 0 to 25")
    age2 = int(input("Age2 (0 to 25): "))

print("Accepted: Age2", age2)


test_num = int(input("Please enter a number "))

while test_num < 10 or test_num > 15:
    print("Guess again:")
    test_num = int(input("Please enter a number "))
print("Good Guess")

choice = input("Choose A V or Q: ").strip().upper()

while choice not in ["A","V","Q"]:
    print("Invalid choice")
    choice  = input("choose  a, b or q ").strip().upper()

print("you selected", choice)
