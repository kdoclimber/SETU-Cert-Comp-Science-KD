import json

with open("settings.json", "w") as file: 
    json.dump({"theme": "dark"}, file)