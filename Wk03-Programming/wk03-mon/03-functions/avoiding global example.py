# Bad — hidden global state
total = 0

def add_to_total(value):
    global total        # declares intent to modify the global
    total += value

add_to_total(10)
add_to_total(25)
print(total)    # 35