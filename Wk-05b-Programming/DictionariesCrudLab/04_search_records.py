movies = [
    {"title": "Jaws", "year": 1975, "rating": 5},
    {"title": "Alien", "year": 1979, "rating": 5},
    {"title": "Shrek", "year": 2001, "rating": 4},
    {"title": "Ken", "year": 2026, "rating": 2},
    {"title": "Raiders", "year": 2000, "rating": 3}
]
#comment out below so my other code runs without fuss
"""
search_rating = int(input("Enter rating: "))
found = False

for movie in movies:
    if movie["rating"] == search_rating:
        print("Found:", movie['title'])
        found = True

if not found:
    print("Movie with that rating not found")
"""
minimum_rating = int(input("Enter a minimum rating: "))
minimum_list=[]
for movie in movies:
    if movie["rating"] >= minimum_rating:
        minimum_list.append(movie["title"])
print(f"Movies with a rating of {minimum_rating} or more, {minimum_list}")

