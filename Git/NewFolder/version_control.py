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

def decode_password(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

def menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    return int(input('Please enter an option:'))

def main():
    while True:
        option = menu()
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encoder(password)
            print('Your password has been encoded and stored!')
        elif option == 2:
            encoded_password = input('Please enter the encoded password: ')
            original_password = decode_password(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {original_password}.')
        elif option == 3:
            break
        else:
            print('Invalid option. Please select a valid option.')

main()
