"""
number = int(input("Enter a number (-1 to stop): "))

while number != -1:
    print("You entered:", number)
    number = int(input("Enter a number (-1 to stop): "))

print("Finished")
"""
"""
total = 0

number = int(input("Enter a number (-1 to stop): "))
while number != -1:
    total = total + number
    number = int(input("Enter a number (-1 to stop): "))

print("Total:", total)"""

"""
total = 0
count = 0

number = int(input("Enter a number (-1 to stop): "))

while number != -1:
    total = total + number
    count = count + 1
    number = int(input("Enter a number (-1 to stop): "))

print("Total:", total)
print("Numbers entered:", count)
"""
# Task Name Count
name_total = 0

name = input("Please enter as many names as you like, one at a time. Type 'stop' when you are finished ")

while name !='stop':
    name_total = name_total + 1
    name = input("Please enter as many names as you like, one at a time. Type 'stop' when you are finished ")

print(f"Total number of names: {name_total}")
