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

def buildPassword(uppers, lowers):
    charSet = list(uppers + lowers)
    pwd = "".join(charSet)
    
    return pwd

def main():
    print("\nWelcome to the random password generator.")
    uppercaseNum = int(input("\nPlease selecte the number of uppercase characters you'd like your password to contain: "))
    lowercaseNum = int(input("\nPlease selecte the number of lowercase characters you'd like your password to contain: "))
   
    bigs = getChars(string.ascii_uppercase, uppercaseNum)
    littles = getChars(string.ascii_lowercase, lowercaseNum)

    password = buildPassword(bigs, littles)
    
    display_password(password)

main()