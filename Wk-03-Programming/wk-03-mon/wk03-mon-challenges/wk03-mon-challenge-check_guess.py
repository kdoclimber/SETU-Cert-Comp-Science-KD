import random

def make_secret_number():
    secret_num = random.randint(1, 100)
    print(f' 14 make_secret_number() secret_num = {secret_num}')
    return secret_num

def get_guess_num():
    guess_num = int(input(" get_guess_num Guess the secret number (1-100): "))
    print(f' 13 get_guess_num guess_num = {guess_num}')
    return guess_num

def check_guess(secret_num, guess_num):
    print(" 10 inside check guess")
    print(f' 11 secret_num = {secret_num}')
    print(f' 12 guess_num = {guess_num}')
    if guess_num == secret_num:
        print("Correct")
        return True
    elif guess_num > secret_num:
        print ("Too High")
        return False
    elif guess_num < secret_num:
        print ("Too Low")
        return False
        
def track_guesses(guess_count, value):
    print(f' 8 guess_count = {guess_count}')
    print(f' 9 guess_count +1 = {guess_count + value}')
    return guess_count + value

guess_total = 0

def invite_guess():
    #guess_total = guess_total
    print(f' 1 invite_guess INSIDE')
    print(f' 2 invite_guess guess_total= {guess_total}')
    print(f' 2x invite_guess guess_total TYPE= {type(guess_total)}')
    if guess_total == 0:
        print(f' 3 invite_guess guess_total= {guess_total}')
        secret_num = make_secret_number()
        print(f' 4 invite_guess secret_num = {secret_num}')
        guess_num = get_guess_num() #ask the user to guess
       
        print(f' 5 invite_guess guess_num = {guess_num}')
        print(f' 6 invite_guess guess_total = {guess_total}')
        if check_guess(secret_num, guess_num) == False:
            print(f' 7 invite_guess guess_total= {guess_total}')
            #guess_total = track_guesses(guess_total, 1)#increment the guess count
            print("Wrong try again")
    else:
        print ("after else")
       # secret_num = get_secret_number()
   

invite_guess()
