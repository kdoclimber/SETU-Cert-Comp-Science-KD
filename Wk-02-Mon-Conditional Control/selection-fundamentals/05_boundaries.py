height = int(input('Enter height in cm: '))
if height >= 120:
    print('You may go on the ride')
else:
    print('Sorry, you are not tall enough')


# above does not work with input 120.0 fixed using float and convert to int below
height = float(input ('Enter height in cm: '))
newHeight = int(height)
if newHeight >= 120:
    print('You may go on the ride')
else:
    print('Sorry, you are not tall enough')

