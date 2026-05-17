# ==========================================================
# Project 3: Random Password Generator
# DecodeLabs Python Internship - Week 3
# Developed by Muhammad Younas
# ==========================================================

import string
import secrets
import math


def generate_password(length):
    """
    Generate a secure random password using:
    - Letters (a-z, A-Z)
    - Numbers (0-9)
    - Special Characters (!@#$%^&*)
    """

    # Character pool
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    # Generate password
    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password, len(characters)


def calculate_entropy(length, pool_size):
    """
    Entropy Formula:
    E = L × log2(R)
    """
    return length * math.log2(pool_size)


def check_strength(entropy):
    """Check password strength."""

    if entropy < 50:
        return "Weak"
    elif entropy < 80:
        return "Strong"
    else:
        return "Very Strong"


def main():
    print("=" * 55)
    print("          RANDOM PASSWORD GENERATOR 🔐")
    print("=" * 55)

    # Keep asking until valid input is entered
    while True:
        user_input = input("Enter password length (minimum 8): ")

        # Check if input is numeric
        if not user_input.isdigit():
            print("❌ Invalid input! Please enter numbers only.\n")
            continue

        # Convert to integer
        length = int(user_input)

        # Check minimum length
        if length < 8:
            print("❌ Password length must be at least 8 characters.\n")
            continue

        # Valid input → stop loop
        break

    # Generate password
    password, pool_size = generate_password(length)

    # Calculate entropy
    entropy = calculate_entropy(length, pool_size)

    # Check strength
    strength = check_strength(entropy)

    # Display results
    print("\n✅ Generated Password:")
    print(password)

    print(f"\n📊 Character Pool Size: {pool_size}")
    print(f"🔐 Password Entropy: {entropy:.2f} bits")
    print(f"🛡️ Password Strength: {strength}")


# Run the program
if __name__ == "__main__":
    main()