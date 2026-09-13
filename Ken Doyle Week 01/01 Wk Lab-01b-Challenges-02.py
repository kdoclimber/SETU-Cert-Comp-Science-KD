dash = ("-" * 21)
doubleDash = ("=" * 21)
title = 'RECEIPT'
item = 'Coffee'
price = float(3.5)
qty = int(4)

print(f'{doubleDash} \n{title.center(21)} \n{doubleDash}')
print(f'Item: \t{item} \nPrice: \t€{price:.2f} \nQuantity: \t{qty} \n{dash} \nTotal: \t€{float(price * qty):.2f}')
print(f'{doubleDash}')

print(f'{doubleDash} \n{title.center(21)} \n{doubleDash}')
print(f'Item: {item:>10}')
print('Price' + '€'+ str(price))
print(f'Total: €{float(price * qty):>10.2f}')
print(f'{doubleDash}')

#trying to format the space below
s = "Hello"
print(f'{s:<10}World')
print(f'{s:>10}World')
print(f'{s:^10}World')

print('World' + f'{s:<10}')
print('World' + f'{s:>10}')
print('World' + f'{s:>10}')
print('World' + f'{s:^10}')