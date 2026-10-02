x = 10

def double():
    x = 20
    print(f"Inside double should be the local value of x, set inside the function: {x}")

def triple():
    print(f"Inside triple, should be the global value of x: {x}")

double()
triple()
print(f"Global, print from outside the function finds the global value of x: {x}")

y ="Global string y"
def outer():
    y = 'Enclosing string y' # if this value for Y is not set here the functions and the print find the global value above
    print(f'From inside the outer function y = {y}')
    def inner():
        print(f'From inside the innner function y = {y}')#should be Enclosing Y
    inner()

outer()
print(f'from the print outside the function y = {y}') #should be Global Y
#inner()#cant call inner() from outside the enclosing function that encloses the function inner()
