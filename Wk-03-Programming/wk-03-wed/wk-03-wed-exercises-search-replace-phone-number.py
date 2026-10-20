def clean_phone(number, old_item, new_item):
    new_number = number.replace(old_item, new_item)
    return new_number

#clean_list = ["(", ")", " ", "-"] # list of items to remove, this worked but was clunky

def search_number(phone_number, clean_list):# this calls clean_phone function in a loop based on items to remove
    original_number = phone_number
    #print(f"len = {len(clean_list)}")
    #print(f"original_number = {original_number}")
    n = len(clean_list)# n is used to track the number of loops and then return the stripped down number
    for i in clean_list: # i is (,),- etc
        n = n-1
        #print(f"n = {n}")
        new_number = clean_phone(original_number, i, "")
        #print(f"new_number, = {new_number}")
        original_number = new_number
        if n == 0:
            return new_number

stripped_number1 = search_number("(01) 234-5678", "()- ") # sends the number and what to strip out
print(f"stripped_number1 = {stripped_number1}")

stripped_number2 = search_number("+353 86 123 4567", "()- ") # can strip + if you want just add to the list
print(f"stripped_number2 = {stripped_number2}")

stripped_number3 = search_number("086-555-1234", "()- ")
print(f"stripped_number3 = {stripped_number3}")