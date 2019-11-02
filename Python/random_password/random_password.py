import string
import random

def display_password(pwd):
    print(f"Your new password is {pwd}")

def getChars(letter_set, num):
    x = 0
    chars = ""
    while x < num:
        char = random.choice(letter_set)
        chars += char
        x += 1
    return chars

def buildPassword(uppers, lowers, nums, specs):
    charSet = list(uppers + lowers + nums + specs)
    pwd = "".join(random.sample(charSet,len(charSet)))
    return pwd

def main():
    print("\nWelcome to the random password generator.")
    uppercase = int(input("\nPlease selecte the number of uppercase characters you'd like your password to contain: "))
    lowercase = int(input("\nPlease selecte the number of lowercase characters you'd like your password to contain: "))
    numbers = int(input("\nPlease selecte the number of number characters you'd like your password to contain: "))
    specials = int(input("\nPlease selecte the number of special characters you'd like your password to contain: "))

    bigs = getChars(string.ascii_uppercase, uppercase)
    littles = getChars(string.ascii_lowercase, lowercase)
    nums = getChars(string.digits, numbers)
    specs = getChars(string.punctuation, specials)

    password = buildPassword(bigs, littles, nums, specs)
    
    display_password(password)

main()