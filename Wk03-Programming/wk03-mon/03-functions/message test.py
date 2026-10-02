message = "I am global"    # global scope

def show_message():
    local_msg = "I am local"   # local scope
    print(message)             # functions can read globals
    print(local_msg)

show_message()
print(message)      # OK — message is global
#print(local_msg)    # NameError — local_msg doesn't exist here