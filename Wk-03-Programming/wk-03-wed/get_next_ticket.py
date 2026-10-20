ticket_count2 = 0

def get_next_ticket1(ticket_count1):  # hint: look inside global 
    ticket_count1 # needs a value so I passed it in
    ticket_count1 += 1 
    return ticket_count1

def get_next_ticket2():  # hint: look inside global 
    global ticket_count2
    ticket_count2 += 1 
    return ticket_count2

print(get_next_ticket1(2))

print(get_next_ticket2())