password = input("Enter password: ").lower()
attempts = 1

while password != "setu" and attempts < 5:
    print(f"Attempt {attempts}: Incorrect password")
    password = input("Try again. Please enter password: ").lower()
    attempts = attempts + 1

if password == "setu":
    print("Welcome!! Access granted")
else:
    print(f"Account Locked: you have taken {attempts} attempts")