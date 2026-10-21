books = []
book = {
    "title": input("Title: "),
    "year": int(input("Year: ")),
    "rating": int(input("Rating: "))
}

books.append(book)
print(books)

while True:
    title = input("Title, or blank to stop: ")
    if title == "":
        break
    book = {
        "title": title,
        "year": int(input("Year: ")),
        "rating": int(input("Rating: "))
    }
    books.append(book)

print(books)