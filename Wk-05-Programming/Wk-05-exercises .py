print("\n")

#create a new list 
favourite_foods = ["beans", "rashers", "potatoes", "ham", "cheese", "caviar"]

for i in favourite_foods:
    print(f"Item in Favourite Foods list: {i}")

def create_names_list():
    name_list=[]
    count = 0
    while count <5:
        name= input("Please enter a name: ")
        name_list.append(name)
        count = count +1
    if count == 5:
        print("Thanks, that's enough")
    return name_list

name_list = create_names_list()

def strip_title_list(my_list):
    my_new_list =[]
    for i in my_list:
        strip_name = i.strip()
        final_name = strip_name.title()
        my_new_list.append(final_name)
    return my_new_list

print(f"New Stripped and Titled List: {strip_title_list(name_list)}")

def count_vowels():
    word = input("Please type a word!! ")
    vowel_list = ["a","e","i","o","u"]
    vowel_count = 0
    for vowel in vowel_list:
        for i in word:
            if i == vowel:
                vowel_count = vowel_count +1
    print(f"There are {vowel_count} vowels in the word {word}")
count_vowels()