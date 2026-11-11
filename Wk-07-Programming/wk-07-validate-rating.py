rating = int(input("Choose a rating between 1 and 5: "))

while rating < 1 or rating > 5:
    print("Choose a rating between 1 and 5 ")
    rating  = int(input("Choose 1, 2, 3, 4 or 5 "))

print("Thanks for your rating of ", rating)

#method 2
ratingx = input("Choose a rating between 1 and 5: ")

while ratingx not in ["1","2","3","4","5"]:
    print("Choose a rating between 1 and 5 ")
    ratingx  = int(input("Choose 1, 2, 3, 4 or 5 "))

print("Thanks for your rating of ", ratingx)