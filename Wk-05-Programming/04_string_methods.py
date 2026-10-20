name = "  siobhan roche  "

print(f"name.strip() : {name.strip()}")
print(f"name.upper() : {name.upper()}")
print(f"name.title() : {name.title()}")
print("\n")
name = input("Enter your name: ")
name = name.strip().title()
print("Hello", name)

print("\n")

sentence = "Python is a useful language"
words = sentence.split()
print(words)
print(f"len(words) {len(words)}")
print(f"words[3] {words[3]}")

new_sentence = "-".join(words)
print(new_sentence)
print("\n")

#task
sentence = input("Please enter a sentence ")
#uppercase
print(f"sentence.upper(): {sentence.upper()}")
print("\n")
#the number of characters
print(f"Counts the spaces and letters: len(sentence): {len(sentence)}")
new_sentence = sentence.replace(" ","")
print(f"new_sentence no spaces sentence.replace : {new_sentence}")
print(f"Counts the letters: len(new_sentence): {len(new_sentence)}")

#Could use a loop in a function
def count_letters(your_sentence):
    count = 0
    for char in your_sentence:
        if char != " ":
            count += 1
    return count

print(f"Using a function: count_letters(sentence) : {count_letters(sentence)}")
print("\n")

#list of words
print(f"list of words sentence.split() : {sentence.split()}")
print("\n")

#the number of words
print(f"the number of words len(sentence.split()) : {len(sentence.split())}")
print("\n")
