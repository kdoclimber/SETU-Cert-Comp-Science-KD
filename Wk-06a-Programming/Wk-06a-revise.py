dog = ["Buddy", "Labrador", 4] 
print(dog[0])

dog = {"name": "Buddy", "breed": "Labrador", "age": 4} 
print(dog["name"])

student = { 
    "name": "Aoife", 
    "student_id": 12345, 
    "course": "Computing", 
    "mark": 72 
}
print(student['mark'])
print(student.get("email"))
print(student.get("email", "No email recorded"))
student["year"] = 2026
print(student)

dog = { "name": "Buddy", "breed": "Labrador", "age": 4 } 
removed_age = dog.pop("age") 
print(removed_age) 
print(dog)
dog["teeth"] = 500
print(dog)
print(dog.pop("vaccinated", None))
print(dog)
#dog.pop("vaccinated")

dog = {"name": "Buddy", "breed": "Labrador", "age": 4} 
for keyx in dog: 
    print(f"keyx, dog[keyx] {keyx, dog[keyx]}")
    print(f"keyx {keyx}")
    print(f"dog[keyx] {dog[keyx]}")

for key, valuex in dog.items(): 
    print(key, ":", valuex)

for i, o in dog.items(): 
    print(i, ":", o)

scores = {"Aoife": 70, "Ben": 35, "Cara": 62} 
scores["Ben"] = 45 
scores["Dara"] = 81 
for name, mark in scores.items(): 
    if mark >= 40: 
        print(name, "passed")

for key, value in scores.items(): 
    if value >= 40: 
        print(key, "passed")

dogs = [ 
    {"id": 1, "name": "Buddy", "age": 4}, 
    {"id": 2, "name": "Luna", "age": 2}, 
    {"id": 3, "name": "Milo", "age": 6} 
]
for dog in dogs: 
    print(dog["name"], dog["age"])

for dog in dogs: 
    if dog["id"] == 2: 
        print("Found:", dog["name"])

def find_dog(dogs, dog_id): 
    for dog in dogs: 
        if dog["id"] == dog_id: 
            return dog 
        return None
    
found_dog = (find_dog(dogs, 1))
print(f"Found dog name: {found_dog['name']}")

computer = { "device": "Laptop", "brand": "Dell", "power_on": False }
computer2 = [{ "device": "Laptop", "brand": "Dell", "power_on": False }]

print(computer['brand'])
#print(computer2.item('brand'))
#print(computer2[('brand')])
for record in computer2:# do I habve to loop through this? is this the only way
    print(record["brand"])

computer ["wifi_connected"] = False
print(computer)
computer ["power_on"] = True #TURN THE POWER ON: TEST BELOW
print(computer)

if computer["power_on"] == True:
    print("Computer Power On")
else:
    print("Computer Power Off")

for record in computer2:
    if record["power_on"] == True:
        print("Computer2 Power On")
    else:
        print("Computer2 Power Off")

for key, value in computer.items():
    print(f"key is: '{key}' and value is: '{value}'")

for record in computer2:
    for key, value in record.items():
        print(f"key is: '{key}' and value is: '{value}'")