import random
import string

def check_strength(password):
        hasLetter = False
        hasDigit = False
        hasSymbol = False

        for ch in password: 
            if ch in string.ascii_letters:
                hasLetter = True
            elif ch in string.digits:
                hasDigit = True
            elif ch in string.punctuation:
                hasSymbol = True

        if hasLetter and hasDigit and hasSymbol:
            return "Strong Password"
        elif hasDigit or hasSymbol:
            return "Medium Password"
        else: 
            return "Weak Password"

length = int(input("Enter password length: "))
characters = string.ascii_letters

if length < 7:
    print("Length is too small, password cannot be generated")

else : 
    password = []
    password.append(random.choice(string.ascii_letters))
    use_numbers = input("Include numbers in password? (y/n): ")
    use_symbols = input("Include symbols in password? (y/n): ")
    if use_numbers == "y":
        password.append(random.choice(string.digits))
        characters = characters + string.digits
    if use_symbols == "y": 
        password.append(random.choice(string.punctuation))
        characters = characters + string.punctuation

    remaining_length = length - len(password)

    for i in range(remaining_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print("Generated Password is:", password)
    print("Password Strength:",check_strength(password))
        








