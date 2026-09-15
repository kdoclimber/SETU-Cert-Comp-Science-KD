age = int(input('Age: '))

if age < 16 and age >0:
    ticket_price = 8
    print(f'Age is under 16 so you get a ticket for €{ticket_price} ')
else:
    ticket_price = 12
    print (f'You are 16 or over so your ticket price is €{ticket_price}')