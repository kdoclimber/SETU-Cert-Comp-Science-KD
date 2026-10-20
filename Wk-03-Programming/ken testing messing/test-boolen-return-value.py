
def is_lead_climber():
    is_leader = input('Have you lead a trad climb before? Y/N:').upper()
    print(f'is leader from function: {is_leader}')
    if is_leader == "Y":
        is_leader = True
        print(f'is leader from function TRUE: {is_leader}')
        print(f'is leader from function TRUE TYPE: {type(is_leader)}')
    else:
        is_leader = False
        print(f'is leader from function FALSE: {is_leader}')
        print(f'is leader from function FALSE TYPE: {type(is_leader)}')
    return is_leader

def continue_questions():
    print(f'Thanks, please answer the following questions' )  
    is_leader = is_lead_climber()
    print(f'is leader from continue questions TYPE: {type(is_leader)}')
   
    print(f'continue questions: is_leader: {is_leader}, is_multipitch: {is_multipitch}, is_abseiler: {is_abseiler}, hours: {hours}, rope_length: {rope_length}')
    access_answers(is_leader)

def access_answers(is_leader, is_multipitch, is_abseiler, hours, rope_length):  
    #Rule 1 Age is dealt with at the welcome stage
    print(f'access_answers: is_leader: {is_leader}, is_multipitch: {is_multipitch}, is_abseiler: {is_abseiler}, hours: {hours}, rope_length: {rope_length}')
    print(f'is leader from acess_answers: {type(is_leader)}')
    #Rule 2
    if is_leader and is_multipitch and is_abseiler and hours >=8 and rope_length >=60:
        print("Rule 2 Glendalough")
        rule_2 = True
  
