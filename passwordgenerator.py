import random
import string

def generate_password(length, complexity):
    # Define character sets based on complexity level
    if complexity == 1:  # Letters only
        characters = string.ascii_letters
    elif complexity == 2:  # Letters + digits
        characters = string.ascii_letters + string.digits
    else:  # Letters + digits + punctuation
        characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== PASSWORD GENERATOR ===")

    try:
        # User input for length
        length = int(input("Enter desired password length: "))

        if length < 4:
            print("Password length should be at least 4.")
            return

        # Choose complexity
        print("\nSelect Password Complexity:")
        print("1 - Letters only")
        print("2 - Letters + Numbers")
        print("3 - Letters + Numbers + Symbols (Strongest)")

        complexity = int(input("Choose complexity (1/2/3): "))

        if complexity not in [1, 2, 3]:
            print("Invalid complexity selected.")
            return

        # Generate password
        password = generate_password(length, complexity)

        # Display password
        print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
