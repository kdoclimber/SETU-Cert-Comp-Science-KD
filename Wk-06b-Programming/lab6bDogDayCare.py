dogs = [
    {"id": 1, "name": "Buddy", "breed": "Retriever", "age": 4, "vaccinated": "No"},
    {"id": 2, "name": "Luna", "breed": "Labrador", "age": 2, "vaccinated": "No"},
    {"id": 3, "name": "Milo", "breed": "Spaniel", "age": 6, "vaccinated": "No"}
]

def display_dogs(dogs):
    for dog in dogs:
        print(f"ID: {dog["id"]}, Name: {dog["name"]}, Breed: {dog["breed"]}, Age: {dog["age"]}, Vaccinated: {dog['vaccinated']}")

def find_dog(dogs, dog_id):
    for dog in dogs:
        if dog["id"] == dog_id:
            return dog
    return None

#my version below
def check_dog_id(dogs, dog_id):
    id_match = False
    for dog in dogs:
        if dog_id == dog['id']:
            id_match = True
            return True
    return False   
#my version below
def add_dog_ken(dogs):
    dog_id = int(input("ID: "))
    while check_dog_id(dogs, dog_id) == True:
        print('That ID is taken')
        dog_id = int(input("Try again: ID: "))

    name = input("Name: ")
    breed = input("Breed: ")
    age = int(input("Age: "))
    vaccinated = input("Vaccinated-Y/N: ")
    dog = {
        "id": dog_id,
        "name": name,
        "breed": breed,
        "age": age,
        "vaccinated": vaccinated
    }
    dogs.append(dog)
    print("Dog added")

#uses find_dog...better...less code
def add_dog(dogs):
    dog_id = int(input("ID: "))
    while find_dog(dogs, dog_id) != None:
        print('That ID is taken')
        dog_id = int(input("Try again: ID: "))

    name = input("Name: ")
    breed = input("Breed: ")
    age = int(input("Age: "))
    vaccinated = input("Vaccinated-Y/N: ")

    dog = {
        "id": dog_id,
        "name": name,
        "breed": breed,
        "age": age,
        "vaccinated": vaccinated
    }

    dogs.append(dog)
    print("Dog added")


def delete_dog(dogs):
    dog_id = int(input("Delete Dog. Enter ID: "))
    
    found_dog = find_dog(dogs, dog_id)
    if found_dog['id'] == dog_id:
        dogs.remove(found_dog)
    else:
        print('That ID does not exist')
        #dog_id = int(input("Try again: ID: "))
    #pass Why the pass statement? 

def update_dog(dogs):#allows user to update any info on any dog based on id selection
    dog_id = int(input("Update which dog? ID "))#need to add error correction in case it is a string
    
    found_dog = find_dog(dogs, dog_id)
    if found_dog != None:
        change_dog_id(found_dog)
        change_dog_name(found_dog)
        change_dog_breed(found_dog)
        change_dog_age(found_dog)
        change_vaccinated(found_dog)
    else:
        print("ID not found")

def change_dog_id(found_dog):
    make_change = input((f"Update this dog ID? Y/N: {found_dog['id']} : "))
    if make_change.lower() == 'y':
        new_dog_id = int(input("Enter a new ID ")) 
        found_dog['id'] = new_dog_id
    else:
        exit# not sure if this is the best option

def change_dog_name(found_dog):
    make_change = input((f"Update this dog name? Y/N: {found_dog['name']} : "))
    if make_change.lower() == 'y':
        new_dog_name = (input("Enter a new name ")) 
        found_dog['name'] = new_dog_name
    else:
        exit# not sure if this is the best option

def change_dog_breed(found_dog):
    make_change = input((f"Update this dog breed? Y/N: {found_dog['breed']} : "))
    if make_change.lower() == 'y':
        new_dog_breed = (input("Enter a new breed ")) 
        found_dog['name'] = new_dog_breed
    else:
        exit# not sure if this is the best option

def change_dog_age(found_dog):
    make_change = input((f"Update this dog's age? Y/N: {found_dog['age']} : "))
    if make_change.lower() == 'y':
        new_dog_age = int((input("Enter a new age ")))
        found_dog['age'] = new_dog_age
    else:
        exit# not sure if this is the best option

def change_vaccinated(found_dog):
    make_change = input((f"Is this dog vaccinated? Y/N: "))
    if make_change.lower().strip() == 'y':
        found_dog['vaccinated'] = "Yes"
        print("Vaccinated in now: Yes")
    else:
        found_dog['vaccinated'] = "No"
        print("Vaccinated in now: No")

def search_by_id(dogs):
    search_dog_id = int(input("Search for a dog by ID: "))
    dog = find_dog(dogs, search_dog_id)
    print(f"ID: {dog["id"]}, Name: {dog["name"]}, Breed: {dog["breed"]}, Age: {dog["age"]}, Vaccinated: {dog['vaccinated']}")
    


choice = ""

while choice != "0":
    print()
    print("DOG DAY CARE MANAGER")
    print("1. Add dog")
    print("2. Display dogs")
    print("3. Update dog")
    print("4. Delete dog")
    print("5. Search by ID")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_dog(dogs)
    elif choice == "2":
        display_dogs(dogs)
    elif choice == "3":
        update_dog(dogs)
    elif choice == "4":
        delete_dog(dogs)
    elif choice == "5":
        search_by_id(dogs)
    elif choice != "0":
        print("Invalid option")


#add_dog(dogs)
#display_dogs(dogs)
#delete_dog(dogs)
#display_dogs(dogs)
