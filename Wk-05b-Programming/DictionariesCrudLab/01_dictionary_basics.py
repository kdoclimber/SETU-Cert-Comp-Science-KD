"""
movie = {
    "title": "Jaws",
    "year": 1975,
    "rating": 5
}

print(movie)
print(movie["title"])
print(movie["year"])

movie["genre"] = "Thriller"
print(movie)

movie["rating"] = 4
print(movie)
"""
student = {
    "name": "Ken",
    "age": 70,
    "course": "Programming",
    "year": 2026
}
print("\n")
print(student)
print("\n")
#for values in student:
#print (values)

#for values in student:
print (f"values: {student.values()}")
print("\n")
#for keys in student:
print (f"keys: {student.keys()}")
print("\n")
#for items in student:
print (f"items: {student.items()}")
print("\n")


for key, value in student.items():
    print(key, value) 

