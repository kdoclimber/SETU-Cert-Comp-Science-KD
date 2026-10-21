movies = []

def show_menu():
    print("Movie Manager")
    print("1. Add movie")
    print("2. View movies")
    print("3. Search movie")
    print("4. Update rating")
    print("5. Delete movie")
    print("6. Exit")

def add_movie():
    movie = {
        "title": input("Title: "),
        "year": int(input("Year: ")),
        "rating": int(input("Rating: "))
    }
    movies.append(movie)
    print("Movie added") 

def view_movies():
    if len(movies) == 0:
        print("No movies stored")
    else:
        for movie in movies:
            print(f"{movie['title']} ({movie['year']}) - {movie['rating']}/5")

def search_movie():
    search_title = input("Enter a search title: ").lower()
    if len(movies) == 0:
        print("No movies stored")
    else:
        for movie in movies:
            if search_title == movie['title'].lower():
                print(f"We found your movie: {movie['title']} ({movie['year']}) - {movie['rating']}/5")
            else:
                print("Sorry, there is no matching title")

def update_rating():#could adapt the serch function
    search_title = input("Change the rating of which title: ").lower()
    if len(movies) == 0:
        print("No title stored")
    else:
        for movie in movies:
            if search_title == movie['title'].lower():
                print(f"We found your movie: {movie['title']} has a rating of - {movie['rating']}/5")
                new_rating = int(input(f"Enter your new rating for {movie['title']}: "))
                movie['rating'] = new_rating
                print(f"Movie Title: {movie['title']} New Rating - {movie['rating']}/5")
            else:
                print("Sorry, there is no matching title")

def delete_movie():#could adapt the serch function
    search_title = input("Delete which movie: ").lower()
    if len(movies) == 0:
        print("No title stored")
    else:
        for movie in movies:
            if search_title == movie['title'].lower():
                print(f"We found your movie title: {movie['title']}:")
                               
                confirm = input("Are you sure you want to delete this title? Y/N ").lower()
                if confirm == "y":
                    movies.remove(movie)
                    print(f"Movies after delete: {movies}")      
            else:
                break

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