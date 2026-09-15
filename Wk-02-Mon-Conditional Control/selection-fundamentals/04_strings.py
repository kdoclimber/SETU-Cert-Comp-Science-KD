
# using y or Y
answer = input('Continue? y/n: ')
if answer == 'y' or answer == 'Y':
    print('Continue: using  "or')
else:
    print('Stop: using "or"')

# using .lower() and elif to make sure y or n is used. try using another letter 
answer = input('Continue? y/n: ').lower()
if answer == 'y':
    print('Continue')
elif answer != 'y' or  answer != 'n':
    print ('Please use "y" or "n"')
else:
    print('Stop')

#SECRET WORD using .lower
secretWord = input('Enter your "Secret" word ').lower()

if secretWord == 'blue':
    print(f'Correct: Your Secret word is {secretWord} ')
else:
    print('Try again')

#SECRET WORD not using .lower till later
secretWord = input('Enter your "Secret" word ')
secretWordLower = secretWord.lower()
if secretWordLower == 'blue':#tested for lower case
    print(f'Correct: Your Secret word is {secretWord} ')#displays the origiinal user secret word to the user
else:
    print('Try again')