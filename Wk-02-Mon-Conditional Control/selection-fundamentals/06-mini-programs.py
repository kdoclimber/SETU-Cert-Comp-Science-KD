# Cinema Entry
age = int(input('Age: '))
if age >= 16:
    print('Cinema Entry Allowed')
else:
    print('Sorry, you are not old enough')

# Temperature Warning
temperature = int(input('Todays Temperature is? '))
if temperature < 0:
    print('Warning: Icy Conditions')
else:
    print('No ice warning')

# Larger number
firstNum = int(input('First number '))
secondNum = int(input('Second number '))
if firstNum > secondNum:
    print(f'The firs number, {firstNum} is larger')
else:
    print (f'The second number, {secondNum} is larger')

# Discount
orderCost = float(input('Please enter a cost in €'))
if orderCost >= 100:
    print(f'you get a 10% discount of €{orderCost * 0.10:.2f}. Your final cost is €{orderCost - orderCost * 0.10:.2f}')
else:
    print(f"You didn't order enough, you get no discount. Your final cost is €{orderCost}") # changed quotes to deal with didn't

#Unknow User
userName = input('Enter your User Name: ')
if userName == 'student': #case sensitive
    print('Welcome')
else:
    print('Unknown User')

# Number detective
userNum = int(input('Enter a whole number: '))
if userNum <0:
    print(f'{userNum} is negative')
elif userNum >0:
     print(f'{userNum} is positive')

if userNum %2 == 0:
    print(f'{userNum} is even')
elif userNum %2 != 0:
     print(f'{userNum} is odd')
