"""
CP1404 - Practical 3
Password Check

Created on 27-11-21 by Richard Reynard
"""

MINIMUM_LENGTH = 4


def first_trial():
    """Get password with valid length and print asterisks."""
    user_password = input(f"Enter password of minimum {MINIMUM_LENGTH} characters: ")
    while len(user_password) < MINIMUM_LENGTH:
        user_password = input(f"Enter password of minimum {MINIMUM_LENGTH} characters: ")
    print("*"*len(user_password))


first_trial()


def main():
    """Get password and print using function."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get valid password that meets the minimum length requirement."""
    password = input(f"Enter password of minimum {minimum_length} characters: ")
    while len(password) < minimum_length:
        password = input(f"Enter password of minimum {minimum_length} characters: ")
    return password


def print_asterisks(count):
    """Print asterisks by the number of the characters of password."""
    print("*" * len(count))


main()
