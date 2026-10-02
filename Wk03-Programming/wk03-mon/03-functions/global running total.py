running_total = 0

def add(value):
    global running_total
    running_total += value

add(15)
add(30)
add(5)
print(running_total)
