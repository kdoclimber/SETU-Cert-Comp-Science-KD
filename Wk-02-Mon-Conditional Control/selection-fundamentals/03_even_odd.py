number = int(input('Enter a whole number: '))

if number % 2 == 0:
    #even number divided by 2 leaves no remainder
    print(f'Even: Remainder {number % 2}')
else:
    # odd number divided by two leaves a remainder
    print(f'Odd: Remainder {number % 2}')

# Mini exercise - Positive or negative
#using float. breaks if I try a decimal
number = float(input('Enter a number '))

if number >= 0:
    print('Zero or Positive')
else:
    print('Negative')