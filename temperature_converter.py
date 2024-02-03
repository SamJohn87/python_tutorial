#This Python program facilitates the conversion of temperatures between Celsius and Fahrenheit.
#The user is invited to choose whether to convert from Celsius to Fahrenheit or from Fahrenheit to Celsius.
#After the conversion, the program will show the formula used.


print(' TTTTT  EEEEE  M   M  PPPP   EEEEE  RRRR     A   TTTTT  U   U  RRRR  EEEEE')
print('   T    E      MM MM  P   P  E      R   R   A A    T    U   U  R   R E')
print('   T    EEEE   M M M  PPPP   EEEE   RRRR   AAAAA   T    U   U  RRRR  EEEE')
print('   T    E      M   M  P      E      R  R  A     A  T    U   U  R  R  E')
print('   T    EEEEE  M   M  P      EEEEE  R   R A     A  T     UUU   R   R EEEEE')
print(' ')
print(' CCCCC  OOOOO  N   N  V       V  EEEEE  RRRR   TTTTT  EEEEE  RRRR')
print(' C      O   O  NN  N   V     V   E      R   R    T    E      R   R')
print(' C      O   O  N N N    V   V    EEEE   RRRR     T    EEEE   RRRR')
print(' C      O   O  N  NN     V V     E      R  R     T    E      R  R')
print(' CCCCC  OOOOO  N   N      V      EEEEE  R   R    T    EEEEE  R   R')
print('\nWelcome to my user-friendly Temperature Converter!')
print('This tool is designed to effortlessly convert temperatures between Celsius and Fahrenheit.')
print('This is a quick and convenient solution for your temperature conversion needs.')

while True:
    print('\033[34m\nWhich type of conversion are you looking to perform?')
    print('Enter F to convert from Fahrenheit to Celsius')
    print('Enter C to convert from Celsius to Fahrenheit')
    conversion_type = input()

    while conversion_type.lower() != 'c' and conversion_type.lower() != 'f':
        print('Enter F to convert from Fahrenheit to Celsius')
        print('Enter C to convert from Celsius to Fahrenheit')
        conversion_type = input()

    print('\nWhich temperature would you like to convert?')
    number_to_convert = input()

    while not number_to_convert.lstrip('-').isdigit():
        print('Which temperature would you like to convert?')
        number_to_convert = input()

    if conversion_type == 'c':
        conversion_value = int(number_to_convert) * 9/5 + 32
        print(f'\n{number_to_convert}°C is equal to {int(conversion_value)}°F' )
        print(f'\nThe formula used to get this value is {number_to_convert} x 9/5 + 32')
    else:
        print(f'\n{number_to_convert}°F is equal to {int(conversion_value)}°C' )
        print(f'\nThe formula used to get this value is ({number_to_convert} - 32) x 5/9')

    print('\nWould you like to perform another conversion?')
    print('Enter Y for yes')
    print('Enter N for no')
    convert_again = input()

    while convert_again.lower() != 'y' and convert_again.lower() != 'n':
        print('Would you like to perform another conversion?')
        print('Enter Y for yes')
        print('Enter N for no')
        convert_again = input()

    if convert_again.lower() == 'n':
        print('Thank you for using my Temperature Converter.')
        print('I hope you found it useful!')
        break