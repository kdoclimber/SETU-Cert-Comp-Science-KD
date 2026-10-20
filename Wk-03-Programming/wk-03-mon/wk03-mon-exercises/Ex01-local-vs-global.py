x = 10 # global
# below prints the local x value 20
def double():
    x = 20
    print(f"Inside double should print local: {x}")
# below prints the global x value 10
def triple():
    print(f"Inside triple should print global: {x}")

double()
triple()
# below prints the Global x value 10
print(f"Global: {x}")
# 20, 10, 10
