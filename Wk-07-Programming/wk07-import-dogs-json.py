import json
"""
dogs= [ 
    {"name": "Buddy", "age": 4}, 
    {"name": "Luna", "age": 2}, 
    {"name": "Lunasss", "age": 23}, 
    {"name": "Lunasss3", "age": 243} 
]
"""

def save_dogs(dogs):
    with open("dogs.json", "w", encoding="utf-8") as file:
        json.dump(dogs, file, indent=4)

def load_dogs():
    with open("dogs.json", "r", encoding="utf-8") as file:
        return json.load(file)

#save_dogs(dogs)

def add_dog(dogs):
    name = input("Enter the dog's name: ").strip()
    while name == "":
        name = input("Name can't be blank. Please try again: ").strip()

    age = int(input("Enter the dog's age, must be between 0 and 25: "))
    while age < 0 or age > 25:
        age = int(input("Plese enter an age between 0 and 25: "))
    dogs.append({"name": name, "age": age})

dogs = load_dogs()
add_dog(dogs)
#save_dogs(dogs)

for dog in dogs:
    print(f"Dog Name: {dog['name']} Dog Age: {dog['age']}")