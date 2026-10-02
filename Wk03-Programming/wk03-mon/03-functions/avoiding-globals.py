total = 0 # global scope

def add_to_total(value):
    global total # has to be made global for this function to find the variable total
    print(total)
    #print(f'inside add-to_total total = {total}')
    print(f'inside add-to_total value = {value}')
    total += value
    print(f'inside add-to_total NEW total = {total}')

add_to_total(10)
print(f' First print {total}')
#add_to_total(25)
print(f' Second print {total}')