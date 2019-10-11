import string

def rotate_string(user_string, direction, offset):
    user_string = user_string.replace(" ", "")
    english = list(string.ascii_lowercase)
    
    if direction == "d":
        offset = 26 - offset

    rotated = english[offset::] # letters (offset+1)-26
    p2 = english[0:offset] # letters 1 - offset
    rotated.extend(p2) # move beginning of list to end of list

    holder = []
    for char in list(user_string):
        index = english.index(char)
        holder.append(rotated[index])
        cipher = ''.join(holder)

    return cipher

def main():
    print("Welcome to the rotation cipher encrypter/decrypter!")

    direction = input("\nWhat would you like to do? \nEnter 'e' for encrypt or 'd' for decrypt: ")
    string = input("\nPlease enter a string with lowercase letters only: ")
    offset = int(input("\nPlease enter the number of characters your string should be shifted: "))
    
    cipher = rotate_string(string, direction, offset)

    print(f"Your string \"{string}\" converts to \"{cipher}\".")

main()