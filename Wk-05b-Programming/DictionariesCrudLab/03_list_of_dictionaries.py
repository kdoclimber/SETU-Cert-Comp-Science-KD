movies = [
    {"title": "Jaws", "year": 1975, "rating": 5},
    {"title": "Alien", "year": 1979, "rating": 5},
    {"title": "Shrek", "year": 2001, "rating": 4}
]
for movie in movies:
    print(movie["title"], movie["year"], movie["rating"])

for movie in movies:
    print(f"{movie['title']} ({movie['year']}) - {movie['rating']}/5")

students = [
    {"name": "Ken", "course": "programming", "mark": 99},
    {"name": "Bill", "course": "climbing", "mark": 50},
    {"name": "Mary", "course": "flying", "mark": 89}
]

for student in students:
    print(f"Student Name: {student["name"]}, Course: {student["course"]}, Mark: {student["mark"]}")
