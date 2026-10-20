
def start_process():
    score_total = 0 #set once at the start
    score_count = 0 #set once at the start
    """everything else handled in the for statement below
    otherwise the above are reset each time"""

    for i in range(3): # this is called 3 times
        #print(f'i = {i}')
        #print(f'type i = {type(i)}')
        score = get_input()
        score_total = score_total + score
        #print(f'score_count = {score_count}')
        score_count = score_count + 1 #tried  score_count = i  won't work cant figure why
        score_average = get_average(score_total, score_count )
        #print(f"Running average: {score_total / score_count:.1f}")
        show_running_average(score_average)
        if i == 3-1:
            show_final_average(score_average)
            show_total_score(score_total)
        #print(f'score_average = {score_average}')

def get_input():#gets the user input score called total of 'i' times
    user_score = input("Enter score: ")
    score = float(user_score)
    return score

def get_average(score_total, score_count): #does the maths
    #print(f'score_total = : {score_total}')
    #print(f'from get_average score_count = : {score_count}')
    #print(f"Running average: {score_total / score_count:.1f}")
    #score_average = score_total / score_count #dont need the wrapper
    #return score_average
    return score_total / score_count

def show_running_average(score_average):
    print(f"Running average: {score_average:.1f}")

def show_final_average(score_average):
    print(f'Final average of scores: {score_average}') 
    
def show_total_score(score_total):
    print(f'Total score: {score_total}') 

start_process()