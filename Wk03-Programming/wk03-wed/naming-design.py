def square_root(x): ... 
def get_total(order): ... 
def update_total(order): ... 
def find_in_result(scores, flag): ... 
def is_upper_case(s): ... 
def calc_avg(marks): ... 
def print_average(average): ... 

def get_next_ticket():  # hint: look inside global 
    ticket_count = 0 #needs a value but is reset each time the function is called
    ticket_count += 1 
    return ticket_count

print(get_next_ticket()) #prints 1

"""ken version below. two versions, which is best?"""
ticket_count2 = 0 #global for get_next_ticket2()

def get_next_ticket1(ticket_count1):  # hint: look inside global 
    ticket_count1 # needs a value so I passed it in
    ticket_count1 += 1 
    return ticket_count1

def get_next_ticket2():  # hint: look inside global 
    global ticket_count2
    ticket_count2 += 1 
    return ticket_count2

print(get_next_ticket1(2))#prints 3
print(get_next_ticket2())#prints 1