#Customer
#Must be over 120cm
#Customer >= 120cm ride is true
#If ride is true
# - Age < 16 Price €12
# - 16 <= Age <= 64 Price €20: Student True or False. If True Price is €17
# - Age >= 65 Price €14
# I'm adding a leap year detector...everyone goes free

#define the variables
height = float(input('What is your height in cm?')) # get height
age = int(input('What is your age?')) # get age
is_student = input('Are you a student? "True" or "False":').lower()
tall_enough = False
#print (f"You are {height:.2f}cm")
#function to check if is a leap year returns True or False
import datetime
def is_it_a_leap_year():
    my_date = datetime.datetime.now()
    this_year_is = (my_date.year)
    if this_year_is % 4 == 0:
        if this_year_is % 100 == 0:
            if this_year_is % 400 == 0:
                print(f"{this_year_is} is a leap year")
                return True
    else: print(f"{this_year_is} is not a leap year")
    #return True # for testing
    return False

if height >= 120: 
    tall_enough = True
else:
    print (f"Sorry you are only {height:.2f}cm, you are too small")

if is_student == 'true':
    is_student = True # change to boolean..but I see every string is TRUE as there is something in it
else:
    is_student = False

if tall_enough == True: 
    if is_it_a_leap_year() ==True:
        print(f"this year is a leap year so all rides are free...Yahoo!!")
    elif age < 16:
        ticket_price = 12.00
        print(f"You are {age}: So your ticket price is €{ticket_price:.2f}")
    elif 16 <= age <= 64 and is_student == True:
        ticket_price = 17.00
        print(f'Age 16-64 Age = {age}: Ticket price = €{ticket_price:.2f} and is_student = {is_student}')
    elif age >= 65:
        ticket_price = 14.00
        print(f'Age = 65 or above Age = {age}: Ticket price = €{ticket_price:.2f}')
    else:
        ticket_price = 20.00
        print(f'Age 16-64 Age = {age}: Ticket price = €{ticket_price:.2f} and is_student = {is_student}')

              

