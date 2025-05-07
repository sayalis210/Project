import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Combine all character types
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("🔐 Welcome to the Python Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive number.")
            return

        password = generate_password(length)
        print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
