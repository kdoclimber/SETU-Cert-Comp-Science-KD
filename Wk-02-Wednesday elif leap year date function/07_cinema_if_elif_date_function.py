#Customer
#Age under 12 Too Young
#Age 12 Rating 12 Child Price €7.00
#Age 15 Rating 15 Child Price €7.00
#Age 16 Rating 15 Student Yes Price €10.00
#Age 16 to 64 Price €12.00
#Age 65 and over Rating 15 Price €8.00
#Age 65 and over Rating 18 Price €9.00
#Age between inclusive 16 and 64 and Student price €10.00
#Add new age range Age < 12
#Add new age range Age 12 to 15
#Add new age range Age = 16 -17(and Rating is 15 and student)

#function to get the day of the week
from datetime import date
import calendar
def what_day_is_it():
    my_date = date.today()
    day_of_the_week = calendar.day_name[my_date.weekday()]
    #day_of_the_week = 'Tuesday'# testing on a Friday 
    return day_of_the_week

#define the variables
ask = False #if they are between 16 and 65 ask are you a student other wise False
ticket_price = 12.00 #give it a value
age = int(input('What is your age?')) # get age
film_rating = (int(input('Enter a film rating 12, 15 or 18 ' ))) # get desired rating


if age < film_rating:
    print('Sorry you are too young to see a film with that rating')
elif age >= film_rating and what_day_is_it() == 'Tuesday': # if it's Tuesday do this
         ticket_price = 6.00
         print(f"It's Tuesday and the ticket price is €{ticket_price:.2f}")
elif 12 <= age <= 15 and film_rating == 12:
        ticket_price = 7.00
        print(f'age 12-15 and rating == 12: Age = {age} ticket price = €{ticket_price:.2f}')
elif age == 15 and film_rating == 15:
        ticket_price = 7.50
        print(f'age = 15 rating == 15: Age = {age} ticket price = €{ticket_price:.2f}')
elif 16 <= age <= 17 and film_rating == 12 or film_rating == 15:
        ask = True #ask are you a student for the discount
        print(f'Age 16 - 17 rating 12 0r 15:  Age = {age} Ask = {ask}')
        #ticket_price is set below
elif 18 <= age <= 64 and film_rating ==18:
        ask = True #ask are you a student for the discount
        print(f'Age 18 - 64 rating 18 age = {age} Ask = {ask}')
        #ticket_price is set below
elif age >= 65 and film_rating == 15:
        ticket_price =8.00
        print(f'age >= 65 and rating == 15: Age = {age} ticket price = €{ticket_price:.2f}')
elif age >= 65 and film_rating == 18:
        ticket_price =9.00
        print(f'age >= 65 and rating == 18: Age = {age} ticket price = €{ticket_price:.2f}')
elif ask == False:      
        print(f'Ask is False-no a student: Age = {age} Ticket Price is €{ticket_price:.2f}')
        

if ask == True:# age between  16 and 64 Rating 15 or 16-64 Raing 18
    is_student = input('Are you a student? Y or N ').lower()
    if is_student == 'y':
        if 16 <= age <= 64 and film_rating ==15:
              ticket_price = 9.50
              print(f'Is a Student Age 16 - 64 rating 15 age = {age} ticket price = €{ticket_price:.2f}')
        if 18 <= age <= 64 and film_rating ==18:
            ticket_price = 10.50
            print(f'Is a Student Age 18 - 64 rating 18 age = {age} ticket price = €{ticket_price:.2f}')

        if 16 <= age <= 17 and film_rating == 12 or film_rating == 15:
                 ticket_price = 9.50
                 print(f'Age 16 - 17 rating 12 0r 15:  Ticket Price = {ticket_price:.2f}')
    elif is_student == 'n':
        ticket_price = 30.00
        print(f'Ticket Price = {ticket_price:.2f}')