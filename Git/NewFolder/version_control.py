### Arjun Malkani Lab 6 VC

def encoder(password):
    try:
        encoded_password = " "

        if len(password) != 8:
            raise ValueError('Invalid length.')

        elif len(password) == 8:
            for char in password:
                if char.isdigit():
                    new_char = str((int(char)+3) % 10)
                    encoded_password += new_char

    except ValueError as e:
        print(e)

    except TypeError:
        print('Type Error')

    return encoded_password


def menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')


def main():
    menu()
    menu_selection = int(input('Please enter an option:'))
    print()
    if menu_selection == 1:
        password = (input('Please enter your password to encode:'))
        encoded_password = encoder(password)
        print('Your password has been encoded and stored!')
        print()
    elif menu_selection == 3:
        quit()


while True:
    main()
