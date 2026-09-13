city = 'Waterford'
country = 'Ireland'
pop = 56000

print('City: ', city)
print('Country: ', country)
print('Population: ', pop)
print('2024' ,'06' ,'18' ,sep='-')
print('Mon' ,'Tue' ,'Wed' ,'Thu' ,'Fri' , sep=' | ')
print('Mon','Tue','Wed','Thu','Fri', sep=' | ')
print('Mon','Tue','Wed','Thu','Fri', sep='|')
print('Mon ','Tue ','Wed ','Thu ','Fri ', sep='|')
print('Start', end='..')
print('Middle', end='!!!')
print('End')

product = 'Coffee'
price = '3.5'
qty = 4
print(f'Item: {product}\nPrice: {price} \nQuantity: {qty} \nTotal: €{float(price) * qty}')
print(f'Item: {product}\nPrice: {price} \nQuantity: {qty} \nNew Total 1: €{float(price) * qty}')
print(f'Item: {product}\nPrice: {price} \nQuantity: {qty} \nNew Total 2: €{float(price):.2f} * {qty}')#* printed as a str
print(f'Item: {product}\nPrice: {price} \nQuantity: {qty} \nNew Total 3: €{float(price) * qty:.2f}')

product = 'Coffee'
price = 5.0
qty = 5
print(f'Item: {product}\nPrice: {price} \nQuantity: {qty} \nNew Total 5: €{price * qty}')
print(f'Item: {product}\nPrice: {price} \nQuantity: {qty} \nNew Total 6: €{price * qty:.2f}')
print(type(price))