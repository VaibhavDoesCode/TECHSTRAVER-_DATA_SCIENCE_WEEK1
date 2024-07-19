import random
import string

def generate_password(length, use_digits=True, use_special=True):
    # Define character pools
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_symbols = string.punctuation

    # Combine character pools based on user requirements
    characters = lowercase_letters + uppercase_letters
    if use_digits:
        characters += digits
    if use_special:
        characters += special_symbols

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
desired_length = int(input("Enter desired password length: "))
include_digits = True  # Set to False if you don't want digits
include_special = True  # Set to False if you don't want special symbols

generated_password = generate_password(desired_length, include_digits, include_special)
print(f"Generated password: {generated_password}")
