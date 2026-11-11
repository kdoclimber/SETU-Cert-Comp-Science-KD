
dogsx= [ 
    {"name": "Buddy", "age": 4}, 
    {"name": "Luna", "age": 2}, 
    {"name": "Lunasss", "age": 23}, 
    {"name": "Lunasss3", "age": 243} 
]

import json 
"""with open("dogs.json", "w", encoding="utf-8") as file: 
    json.dump(dogs, file, indent=4)"""

with open("dogs.json", "r", encoding="utf-8") as file: 
    dogs = json.load(file) 
    print(dogs[2]["name"])
    print(dogs[3]["name"])



    