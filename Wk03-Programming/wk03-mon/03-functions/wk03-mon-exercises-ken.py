def print_stars(num_stars):
    print('*' * num_stars)

def print_dashes(num_dashes):
    print('-' * num_dashes)

def print_banner(title, num_stars, num_dashes):#takes a string
    print_stars(num_stars)
    print(f'{title:^50}')
    print_dashes(num_dashes)

print_banner('Python Rocks!', 50, 20)
