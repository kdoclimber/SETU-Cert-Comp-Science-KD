name = "Alice"
age = 25
score = 87.654

print(f"Name: {name}, Age: {age}")
print(f"Next year I'll be {age + 1}")
print(f"Score: {score:.2f}")

price = 1234567.89
ratio = 0.756
print(f"€{price:,.2f}")
print(f"{ratio:.3%}")
print(f"{42:05d}")

print(f"{'Left':<30}| more right")
print(f"{'Right':>10}|")
print(f"{'Centre':^20}|")


def print_header(word_1, word_2, space_1, space_2):
    print(f"{word_1:<{space_1}} {word_2:>{space_2}}")

def print_symbol_line(symbol, num):
    print(symbol * num)

def print_item_info(item, price, space):
     print(f"{item:<{space}} €{price:>7.2f}")#7 seems to space the €

print_header("item", "Price", 12, 10)
print_symbol_line("+" , 21)
print_item_info("Milk", 1.29, 12)
print_item_info("Bread", 2.49, 12)
print_item_info("Eggs", 3.99, 12)

print("\n")#space between examples

def print_item_info1(item, price, space):# no 7- no space on the euro
    print(f"{item:<{space}} €{price:>.2f}")

print_header("item", "Price", 12, 5)#the use of 'space' is absolute, or accumalates?
print_symbol_line("-" , 21)
print_item_info1("Milk", 1.29, 12)
print_item_info1("Bread", 2.49, 12)
print_item_info1("Eggs", 3.99, 12)