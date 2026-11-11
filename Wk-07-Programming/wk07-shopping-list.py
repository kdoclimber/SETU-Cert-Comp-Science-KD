with open("shopping_list.txt", "a", encoding = "utf-8") as file:
    file.write("Shopping List\n")

def read_print(file):
    with open("shopping_list.txt", "r", encoding = "utf-8") as file:
        print(file.read())

def add_item():
    item = input("Please enter a shopping list item: ")
    num_of_items = input("Please enter the number of items: ")

    with open("shopping_list.txt", "a", encoding = "utf-8") as file:
        file.write("Item: ")
        file.write(item)
        file.write(" - Number of Items: ")
        file.write(num_of_items)
        file.write("\n")
        file.write("read print file from inside add item")
        read_print(file)# last item hasn't been saved/written so wont be printed

add_item()

read_print(file)# last item has been saved/written so will be printed



