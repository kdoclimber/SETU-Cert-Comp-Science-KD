student = {
    "name": "Ava",
    "age": 19,
    "course": "Computing"
}

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)


book = {
    "title": "A4 Refill Pad",
    "author": "Premier",
    "year": 2026,
    "available": "yes"
}

for key, value in book.items():
    print(key, value)