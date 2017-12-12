import random

def display_menu():

    menu = [
        '1> Lowercase letters only',
        '2> Lowercase and numbers',
        '3> Uppercase only',
        '4> Uppercase and numbers',
        '5> Uppercase and lowercase',
        '6> Uppercase, lowercase, and numbers'
    ]
    menu_length = len(menu)

    for menu_item in menu:
        print(menu_item)

    choice = input('Choose an option: ')
    try:
        choice = int(choice)
    except ValueError:
        print('Please choose a valid option')
        exit()

    if choice in range(1, menu_length + 1):                
        symbols = []

        symbols_choice = input('Do you want to include symbols (;^!,etc)? [Yes/No] ')
        if symbols_choice.lower() == 'yes':
            symbols = get_symbols()

        if choice == 1:
            return get_lowercase_letters() + symbols
        elif choice == 2:
            return get_lowercase_letters() + get_numbers() + symbols
        elif choice == 3:
            return get_uppercase_letters() + symbols
        elif choice == 4:
            return get_uppercase_letters() + get_numbers() + symbols
        elif choice == 5:
            return get_uppercase_letters() + get_lowercase_letters() + symbols
        elif choice == 6:
            return get_uppercase_letters() + get_lowercase_letters() + get_numbers() + symbols
    else:
        print('Please choose a valid option.')

def get_ascii_list(start, stop):        
    #this handles the off by one problem since we want to include stop
    ascii_list = [c for c in range(start, stop + 1)]
    return ascii_list

def get_lowercase_letters():    
    #ascii 97 to 122
    return get_ascii_list(97, 122)

def get_uppercase_letters():    
    #ascii 65 to 90
    return get_ascii_list(65, 90)

def get_numbers():    
    #ascii 48 to 57
    return get_ascii_list(48, 57)

def get_symbols():    
    #symbols are: 33 to 47, 58 to 64, 91 to 96, 123 to 126
    symbols =  get_ascii_list(33, 47)
    symbols += get_ascii_list(58, 64)
    symbols += get_ascii_list(91, 96)
    symbols += get_ascii_list(123, 126)
    return symbols

def display_characters(pass_list):
    for ch in pass_list:
        print(chr(ch))

def generate_password(character_list, length):
    random.seed()
    password = ''

    for i in range(0, length):
        password += chr(random.choice(character_list))    
    return password
    
def main():        
    max_password_length = 32    
    min_password_length = 5

    print('Password Generator V01')

    password_list = display_menu()

    password_length = input('How long should the password be? ')

    try:
        password_length = int(password_length)
    except ValueError:
        print('Please enter a numeric value for the password length.')
        exit()

    if password_length <= min_password_length or password_length > max_password_length:
        print('Please use a password length value between {} and {}.'.format(min_password_length, max_password_length))
        exit()

    password = generate_password(password_list, password_length)

    print(format('', '*^40') + '\n' + 'Your password is:\n\n' + password.center(40) + '\n\n' + format('', '*^40'))

if __name__ == '__main__':
    main()