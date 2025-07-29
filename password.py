# Random password generator

import random
import string
lowercase_char = string.ascii_lowercase
uppercase_char = string.ascii_uppercase
digit_chars = string.digits
symbol_chars = string.punctuation

#get password length from user
while True:
    try: 
        length = int(input("enter desired password length: "))
        if length<=0:
            print("Password length must be a positive number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number for length.")

#get character type preferences
include_lowercase = input("Include lowercase letter? (y/n): ").lower() == 'y'
include_uppercase = input("Include uppercase letter? (y/n): ").lower() == 'y'
include_digits = input("Include numbers? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

all_possible_Chars = ""
if include_lowercase:
    all_possible_Chars+= lowercase_char
if include_uppercase:
    all_possible_Chars+= uppercase_char
if include_digits:
    all_possible_Chars+= digit_chars
if include_symbols:
    all_possible_Chars+= symbol_chars

#if no character type is selected
if not all_possible_Chars:
    print("Error: you must select at least one character type. ")
    exit() #exit if no characters are choosen

password=[]
for _ in range(length):
    random_char = random.choice(all_possible_Chars) #random.choice() picks a random element from the sequence
    password.append(random_char)

generated_password = "".join(password)
print(f"\nGenerated Password: {generated_password}")
