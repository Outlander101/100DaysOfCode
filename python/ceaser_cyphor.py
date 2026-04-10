import string

def encrypt(text, shift):
    result = ""
    for char in text:
        is_upper = char.isupper()
        char = char.lower()
        index = string.ascii_lowercase.index(char)
        shift_index = abs((index + shift) % 26)
        shift_char = string.ascii_lowercase[shift_index]
        if is_upper:
            shift_char = shift_char.upper()
            result += shift_char
        else:
            result += shift_char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        is_upper = char.isupper()
        char = char.lower()
        index = string.ascii_lowercase.index(char)
        shift_index = abs((index - shift) % 26)
        shift_char = string.ascii_lowercase[shift_index]
        if is_upper:
            shift_char = shift_char.uppper()
            result += shift_char
        else:
            result += shift_char
    return result

def main():

    retry = False
    while not retry:
        choice = input("Do you want to encrypt or decrypt? (e/d): ")
        if choice == 'e':
            text = input("Enter the text to encrypt:")
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt(text, shift)
            print("Encrypted text: ", encrypted_text)
            retry = True
        elif choice == 'd':
            text = input("Enter the text to decrypt:")
            shift = int(input("Enter the shift value: "))
            decrypted_text = decrypt(text, shift)
            print("Decrypted text: ", decrypted_text)
            retry = True
        else:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        
        retry_choice = input("Do you want to try again? (y/n): ")
        if retry_choice.lower() == 'y':
            retry = False
        else:
            print("Goodbye!")
            retry = True

if __name__ == "__main__":
    main()


