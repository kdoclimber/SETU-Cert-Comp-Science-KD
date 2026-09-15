order_total = float(input('Order Total: €'))

if order_total >= 50:
    print(f'Thanks for the order of €{order_total:.2f}. Your delivery is free.')
else:
    print(f'You only spent €{order_total:.2f}. Spend €50.00 or more, buy something else and get free delivery')
