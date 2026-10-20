    
def draw_line():
    print("-" * 30)# 30 hyphens

def print_header(title):
    draw_line()
    print(title)
    draw_line() 

print_header("Student Report") # prints ---- Student Report ---


def greet(name): 
    print(f"Hello, {name}!") 

result = greet("Alice")#prints Hello, Alice! This is the line I see
print(result) # None: No Value
print(type(result))# <class 'NoneType'> not a string, not a space, not Zero


def celsius_to_fahrenheit(celsius): 
    """Convert Celsius to Fahrenheit.""" 
    return (celsius * 9 / 5) + 32 

def fahrenheit_to_celsius(fahrenheit): 
    """Convert Fahrenheit to Celsius.""" 
    return (fahrenheit - 32) * 5 / 9

print(celsius_to_fahrenheit(600))
print(fahrenheit_to_celsius(600))

def add(a, b):
    #print(f"from inside the funcion 'add' a+b = {a + b}")   # prints the result but does NOT return it
    return a+b # return stops everything

result = add(3, 4)      # prints 7
doubled = result * 2    # FIXED by adding return TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
print(f'doubled = {doubled}')

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def show_all(x,y):
    print(add(x,y))
    print(subtract(x,y))
    print(multiply(x,y))
    print(divide(x,y))
