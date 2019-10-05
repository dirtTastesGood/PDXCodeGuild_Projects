import string
import random

def display_password(pwd):
    print(pwd)

def main():
    print("\nWelcome to the random password generator.")
    n = int(input("\nPlease enter the number of characters you'd like your password to be: "))

    x = 0
    password = ""
    while x < n:
        char = random.choice(string.ascii_letters)
        password += char
        x += 1
    display_password(password)

main()