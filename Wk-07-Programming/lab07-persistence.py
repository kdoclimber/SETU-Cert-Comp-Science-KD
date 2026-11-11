with open("notes.txt", "w", encoding="utf-8") as file: 
    file.write("First note\n")

with open("notes.txt", "a", encoding="utf-8") as file: 
    file.write("Another note\n")

with open("notes.txt", "r", encoding="utf-8") as file: 
    for line in file: 
        print(line.strip())

with open("notes-kd.txt", "a", encoding="utf-8") as file: 
    file.write("Another note\n")

note = input("Enter a journal note: ")
with open("journal.txt", "a", encoding="utf-8") as file:
    file.write(note + "\n kkkk") 
    print("\nYour journal:") 
    with open("journal.txt", "r", encoding="utf-8") as file: 
        print("journal.txt file contents:")
        print(file.read())

        