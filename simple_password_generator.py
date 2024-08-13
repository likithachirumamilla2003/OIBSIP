import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "No character types selected then Please try again."

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password

def main():
    print("Its a Password Generator!")

    length = int(input("Enter the length of the password: "))
    use_letters = input("Do You Want Letters (y/n)? ").lower() == 'y'
    use_numbers = input("Do You Want Numbers (y/n)? ").lower() == 'y'
    use_symbols = input("Do You Want Symbols (y/n)? ").lower() == 'y'

    password = generate_password(length,use_letters,use_numbers,use_symbols)

    print("Generated Password:", password)

if __name__ == "__main__":
    main()
