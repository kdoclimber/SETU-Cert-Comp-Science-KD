import os #checking if the json file exists
import json

"""book_list.json is where the list of books will be held, I don't want to overwrite it all the time
so check if the book_list.json file exists in the path (keeping it simple in the same folder)
pass the path(filename)to the function"""
# credit: https://www.geeksforgeeks.org/python/python-check-if-a-file-or-directory-exists/

def create_book_list():
    path = 'book_list.json' #this is really just the filename rather than a true path
    isExist = os.path.exists(path) 
    print(isExist)
    if isExist == False:
        book_list=[]#create the list to add to the json file 
        #book_list is then loaded from the json file for the functions below to populate
        # create and then close the book_list.json file, it has an empty book_list[]
        with open('book_list.json', "w", encoding = "utf-8") as file:
            json.dump(book_list, file, indent=4)
    return

def load_book_list():
    with open("book_list.json", "r", encoding="utf-8") as file:
        return json.load(file)


def save_book_list(books):
    with open("book_list.json", "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)

def display_books(books):
    for book in books:
        print(f"display 1 Title: {book['title']} Author: {book['author']} Year: {book['year']}")

def display_books_from_json():
    with open("book_list.json", "r", encoding="utf-8") as file:
           books = json.load(file)
    for book in books:
        print(f"Json Title: {book['title']} Author: {book['author']} Year: {book['year']}")

def add_one_book(books):
    title = input("Book Title: ")
    author = input("Book Author: ")
    year = int(input("Book Year: "))
    books.append({"title": title, "author": author, "year": year})
    #return book_list

# have to add three books first then add to JSON
def add_books(number,books):
    count = 0
    while count < number:
        add_one_book(books)
        count = count + 1
   

create_book_list()#create the book_list.json file if it is not there
books = load_book_list()# first time it's an empyy list created in create_book_list
#print (f"BOOKS: {books}")
#for item in books:
    #print (f"item: {item}")
add_books(3,books)# calls add_one_book() number of times
save_book_list(books)#save to the book_list.json file
display_books(books)# display from Python not the json file
display_books_from_json()# loads the book_list.json file and displays the content

#for book in books:
    #print(f"Title: {book['title']} Author: {book['author']} Year: {book['year']}")
