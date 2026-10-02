
#def print_header1(word_1, word_2, space_1, space_2): # space etc used to format
    #print(f"{word_1:<{space_1}} {word_2:>{space_2}}")
#def format_item1(name, qty, price, space1, space2, space3):
    # print(f"{name:<{space1}} {qty:>{space2}} €{price:>{space3}.2f}")

def print_header(word_1, word_2, word_3, space_1, space_2,  space_3):
    print(f"{word_1:<{space_1}} {word_2:^{space_2}} {word_3:>{space_3}}")

def print_symbol_line(symbol, num):
    print(symbol * num)

def format_item(name, qty, price):
     return(f"{name:<15} {qty:^5} €{qty * price:>.2f}")

def print_receipt(title, name1,qty1, price1, name2, qty2, price2, name3, qty3, price3):
    print_symbol_line("=" , 40)
    print(f"{title.center(40)}")
    print_symbol_line("=" , 40)
    print_header("Item", "Qty", "Price", 15, 5, 0)
    print_symbol_line("-" , 40)
    print(format_item(name1, qty1, price1))
    print(format_item(name2, qty2, price2))
    print(format_item(name3, qty3, price3))
    total = (qty1 * price1) + (qty2 * price2) + (qty3 * price3)
    
    print_symbol_line("-" , 40)
    print(f"{'Total':<30} €{total}")
    print_symbol_line("=" , 40)

print_receipt("Cafe Receipt", "Coffee", 2, 3.50, "Cake", 1, 4.75, "Tea", 3, 2.00 )

