def split_string(my_string):
     return my_string.split()
    
def get_initials(full_name, separator):
    n = len(full_name)# items in the list
    count = 0 #used to track the loop and change items in the list
    initials_list = full_name # duplicate the original list so I can change it and return it
    #print(f"initials_list = {initials_list}")
    for i in full_name:
        n = n-1
        #print(f"4a i[0] in full_name = {i[0]}")
        initials_list[count]=(i[0].upper())
        #print(f"3b initials_list = {initials_list}")
        count += 1
        if n == 0:
            initials_list = separator.join(initials_list)  
            #print(f"3d initials_list = {initials_list}")
            return initials_list
        

def send_name(first_string):
    my_split_string = split_string(first_string)
    new_list = get_initials(my_split_string, '.')
    return new_list

print(send_name("alice mary smith"))
print(send_name("John Doe"))
print(send_name("  mary "))


def word_count(text):
    split_words = (text).split()
    word_count = len(split_words)
    unique_words_count = 0
    letter_count = 0
    for i in split_words:
        word_count = word_count - 1
        current_letter_count = len(i)
        if current_letter_count > letter_count:
            letter_count = current_letter_count
            longest_word = i
            #print(f"longest_word = {longest_word}")
        if split_words.count(i) == 1:
            unique_words_count += 1
            if word_count == 0:
                return len(split_words), unique_words_count,longest_word


total_word_count,unique_words,longest_word = word_count("Test with A a a a sentencexxx of of your choice.")

print(f'Total word count: {total_word_count}')
print(f'Unique Words: {unique_words}')
print(f'Longest Word: {longest_word}')