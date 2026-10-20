def add(a,b):
    return a+b 

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return None
    else:
        return a/b

def show_all(x,y):#do I name the arguments the same or is it best to give them different names  o the functions above
    print(f'{x} + {y} = {add(x,y)}')
    print(f'{x} - {y} = {subtract(x,y)}')
    print(f'{x} * {y} = {multiply(x,y)}')
    if divide(x,y) == None:
        print("b = 0. You can't divide by 0. Try another number.")
    else:
        print(f'{x} / {y} = {divide(x,y)}')

show_all(10, 0)