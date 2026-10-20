
def hello_name():
    count = 1
    your_name = input("Please enter your Name ")
    your_number = int(input("Please enter a Number "))

    while count <= your_number:
        print(f"{count} Your Name is {your_name}")
        count = count + 1
#hello_name()

def get_positive_number():

    user_num = int(input("Enter a positive number "))

    while user_num <= 0:
        print(f"{user_num} is not Positive ")
        user_num = int(input("The number should be Postive: Try again "))

    return user_num
#positive_user_num = get_positive_number()
#print (f"Thanks {positive_user_num} is positive")

def get_valid_mark():
    user_mark = int(input("1 Please enter a mark between 0-100 "))

    while user_mark >=0 and user_mark <=100:
        #user_mark = int(input("2 Please enter a mark "))
        print(f"user_mark = {user_mark}")
        if user_mark >=40:
            print ("Pass")
            return user_mark
            
        elif user_mark <40:
            print("Fail")
            return user_mark

    print("Your mark must be between 0 and 100, Please try again")
    user_mark = int(input("3 Please enter a mark between 0-100 ")) # doesn't loop back from here..see version 2 below
    return user_mark
#get_valid_mark()


def get_valid_mark2():
    user_mark = int(input("A Please enter a mark between 0-100 "))

    while user_mark <0 or user_mark >100: # easier to test what it is not
        print("Your mark must be between 0 and 100, Please try again")
        user_mark = int(input("B Please enter a mark between 0-100 ")) 

    if user_mark >=40:
        print ("Pass")  
    elif user_mark <40:
        print("Fail")
#get_valid_mark2()
      
    #return user_mark
def count_spaces():
    sentence = input("Please type a sentence ")
    char_total = 0
    space_count= 0
    #print("  ".isspace()) # could use this
    #print(sentence.count(" ")) # could use this
    for t in sentence: # trying this
        char_total = char_total + 1
        #print (t)

    index = 0
    while index < char_total:
        if sentence[index] == " ":
            space_count = space_count + 1
        index = index + 1

total_spaces = count_spaces()
print(f"Total Spaces = {total_spaces}")


def count_spaces2():
    sentence = input("Please type a sentence ")
    space_count= 0
    index = 0
    while index < len(sentence):
        if sentence[index] == " ":
            space_count = space_count + 1
        index = index + 1
        #print (f"W space_count: {space_count}" )
    return space_count
#total_spaces = count_spaces2()
#print(f"Total Spaces = {total_spaces}")

def total_until_stop():
    user_number = int(input("1 Please entrer a number: 0 to Stop "))
    number_sum = 0

    while user_number != 0:
        number_sum = number_sum + user_number
        #print(f"Running total: {number_sum}")
        #print("Number Total: {number_sum}")
        user_number = int(input("Please entrer a number: 0 to Stop "))
    return number_sum
        

#sum_total = total_until_stop()
#print(f"Total of number is: {sum_total}")
