message = "I am global"    # global scope
def show_message():
    #local_msg = "I am local"   # local scope
    print(message)             # functions can read globals
    #print(local_msg)
show_message()
print(message)      # OK — message is global
#print(local_msg)    # NameError — local_msg doesn't exist here

message2 = "I am global 2"    # global scope
def show_message2(value):
    global message2
    print(message)             # functions can read globals
    print(f'message2 = {message2}')  
    print(f'value = {value}')
    print(f'message 2 + value = {message2+value}') 
    message2 += value
    print(f'message2 after adding value = {message2}')  
    # 

    #print(local_msg)
show_message2("Kens Message")
print(message2)      # OK — message is global
#print(local_msg)    # NameError — local_msg doesn't exist here

# Bad — hidden global state
total1 = 0
def add_to_total1(value):
    #comment out the line below it breaks!why?
   # global total1  #declares intent to modify the global same structure as show_message above
    print (f' total1 = {total1}') 
    print (f' value = {value}') 
   # total1 += value #is it because I'm adding a value to a local variable (created in the function)
    print (total1) # 

#if I change the function to not have to take a value to match the show message function
# I dont need to declare total a global within the function
# what effect is value bringing that I don't under stand?
total2 = 0
def add_to_total2():
    print (total2) # this is available outside the funcion
add_to_total2()
add_to_total1(10)
