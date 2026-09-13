
s = "Hello"
print(f'{s:<10}World')
print(f'{s:>10}World')
print(f'{s:^10}World')

print('World' + f'{s:<10}')
print('World' + f'{s:>10}')
print('Wo' + f'{s:>10}')
print('World' + f'{s:^10}')
