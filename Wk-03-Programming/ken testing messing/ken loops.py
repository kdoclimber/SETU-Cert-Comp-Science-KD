"""for number in range(5, 51,5):
    print(number)

for number in range(1, 20, 2):
    print(number)

for number in range(0, 20):
    if number % 2 == 1:
        print(number)

        def ken_average(my_range):
    total = 0
    for i in range(my_range):
        mark = int(input("Enter mark: "))
        total += mark
    average = total / my_range
    print("Range:", my_range)
    print("Total:", total)
    print("Average:", average)

ken_average(5)


for letter in "python":
    print(letter)

word = input("Enter word:")
vowles = 0
for letter in word:
    if letter in "aeiouAEIOU":
        vowles += 1
print("Vowles:", vowles)
"""
def print_seating(my_row, my_seat):
    for row in range(my_row):
        for seat in range(my_seat):
            print(f"ROW {row} : SEAT {seat}", end='')

print_seating(5, 6)

for row in range(1,5):
    print("\nROW", row, end="")
    for seat in range(1,7):
        print("Seat", seat, end="")
    print()
