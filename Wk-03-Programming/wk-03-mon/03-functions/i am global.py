message = "I am global"

def show_message():
    local_message = "I am local"
    print(message)
    print(local_message)

show_message()
print(f'outside function {message}' )
print(f'outside Function {local_message}')