import string
import random

n = 16
x = 0
password = ""
while x < n:
    char = random.choice(string.ascii_letters)
    password += char
    x += 1
print(password)