import os 
import json

def create_movie_list():
    path = 'movie_list.json' 
    isExist = os.path.exists(path) 
    print(isExist)
    if isExist == False:
        movie_list = [] #create the list to add to the json file 
        with open('movie_list.json', "w", encoding = "utf-8") as file:
                json.dump(movie_list, file, indent=4)
        return

def load_movie_list():
    with open("movie_list.json", "r", encoding="utf-8") as file:
        return json.load(file)

def save_movie_list(movies):
    with open("movie_list.json", "w", encoding="utf-8") as file:
        json.dump(movies, file, indent=4) 
     
# Choice 1
def add_movie():
    movies = load_movie_list()
    movie = {
        "title": input("Movie Title: "),
        "year": int(input("Year: ")),
        "rating": int(input("Rating 1-5: "))
    }
    movies.append(movie)
    save_movie_list(movies)

# Choice 2
def view_movies():
    movies = load_movie_list()
    if len(movies) == 0:
           print("No movies stored")
    else:
        for movie in movies:
            print(f"{movie['title']} ({movie['year']}) - {movie['rating']}/5")

# Choice 3       
def search_movie():
    movie_found = False
    movies = load_movie_list()
    search_title = input("Enter a search Movie Title: ").lower()
    if len(movies) == 0:
        print("No movies stored")
    else:
        for movie in movies:
            if search_title == movie['title'].lower():
                movie_found = True
                print(f"We found your movie: {movie['title']} ({movie['year']}) - {movie['rating']}/5")
                break
        if movie_found == False:
            print("Sorry, there is no matching title")

# Choice 4
def update_rating():
    movie_found = False
    movies = load_movie_list()
    search_title = input("Change the rating of which title: ").lower()
    if len(movies) == 0:
        print("No Movie titles stored")
    else:
        for movie in movies:
            if search_title == movie['title'].lower():
                movie_found = True
                print(f"We found your movie: {movie['title']} has a rating of - {movie['rating']}/5")
                new_rating = int(input(f"Enter your new rating for {movie['title']}: "))
                movie['rating'] = new_rating
                print(f"Movie Title: {movie['title']} New Rating - {movie['rating']}/5")
                save_movie_list(movies)
                break
           
        if movie_found == False:
            print("Sorry, there is no matching title")

# Choice 5
def delete_movie():#could adapt the serch function
    movie_found = False
    movies = load_movie_list()
    search_title = input("Delete which movie: ").lower()
    if len(movies) == 0:
        print("No Movie title stored")
    else:
        for movie in movies:
            if search_title == movie['title'].lower():
                movie_found = True
                print(f"We found your movie title: {movie['title']}:")
                               
                confirm = input("Are you sure you want to delete this title? Y/N ").lower()
                if confirm == "y":
                    movies.remove(movie)
                    save_movie_list(movies)
                    print(f"Movies after delete: {movies}")
                    break      
           
        if movie_found == False:
            print("Sorry, there is no matching movie title")

def show_menu():
    print("Movie Manager")
    print("1. Add movie")
    print("2. View movies")
    print("3. Search movie")
    print("4. Update rating")
    print("5. Delete movie")
    print("6. Exit")

create_movie_list()#create the movie_list.json file if it is not there
#movies = load_movie_list()# first time it's an empyy list created in create_movie_list  
#add_movie() 
#save_movie_list(movies)#save to the movie_list.json file
#view_movies()# loads the movie_list.json file and displays the content


while True:
    show_menu()
    choice = input("Choose: ")
    if choice == "1":
        add_movie()
    elif choice == "2":
        view_movies()
    elif choice == "3":
        search_movie()
    elif choice == "4":
        update_rating()
    elif choice == "5":
        delete_movie()
    elif choice == "6":
        break
    else:
        print("Invalid choice")