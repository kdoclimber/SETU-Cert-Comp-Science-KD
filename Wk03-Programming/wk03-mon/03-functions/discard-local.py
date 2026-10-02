def count_up(start):
    step = 1
    print(f'inside function {start + step}')

count_up(10)
count_up(20)

greeting = 'Hello' # this is global, can be found by the function

def greet(name):
    print(f'Inside function {greeting}, {name}!')

greet("Alice")
greet("Bob")