import string
import random

def generate_password(length=12, chars=string.ascii_letters + string.digits + string.punctuation):
    
    if length < 8:
        print("Password length should be at least 8.")
        return None
    if not chars:
        print("Characters should not be empty.")
        return None
    password = ''.join(random.choice(chars) for _ in range(length))
    while True:
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            break
        password = ''.join([random.choice(chars) for _ in range(length)])
    return password

def get_user_input():
    
    while True:
        try:
            length = int(input("Enter password length (8 or more): "))
            if length < 8:
                print("Password length should be at least 8.")
                continue
            chars = input("Enter characters (leave empty for default): ")
            if not chars:
                chars = string.ascii_letters + string.digits + string.punctuation
            return length, chars
        except ValueError:
            print("Invalid input. Please enter an integer for password length.")

def main():
    
    length, chars = get_user_input()
    password = generate_password(length, chars)
    if password:
        print("Generated password:", password)
    else:
        print("Failed to generate password.")

if __name__ == "__main__":
    main()
