running_total = 0

def add(value):
    global running_total
    running_total += value

add(15)
add(30)
add(5)
print(running_total)


def add(my_total,value):
    return my_total + value

running_total2 = 0
running_total2 = add(running_total2, 1)
print(f'running_total2 = {running_total2}')