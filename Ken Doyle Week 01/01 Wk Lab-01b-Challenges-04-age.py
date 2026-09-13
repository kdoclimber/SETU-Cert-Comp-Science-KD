firstName = input('First Name: ')
lastName = input('Last Name: ')
yob = int(input('Year of Birth '))
#import datetime
from datetime import datetime
current_time = datetime.now()
currentYear = current_time.year

#print('Current Year')
#print(currentYear)
#print(f'Current Year = {currentYear}')

print('-' * 21)
#print (f'AGE = {currentYear - yob}')
print(f'Full Name = {firstName} {lastName}\nInitials: {firstName[0]}.{lastName[0]}.\nAge = {currentYear - yob}')