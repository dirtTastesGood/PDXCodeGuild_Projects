import string

def get_rot13(user_string):

    user_string = user_string.replace(" ", "")
    english = list(string.ascii_lowercase)
    
    rot13 = english[13::] # letters 14-26
    p2 = english[0:13] # letters 1 - 13
    rot13.extend(p2) # move beginning of list to end of list

    holder = []
    for char in list(user_string):
        index = english.index(char)
        holder.append(rot13[index])
        cipher = ''.join(holder)

    return cipher

def main():
    print("Welcome to the ROT 13 cipher encrypter/decrypter!")

    string = input("\nPlease enter a string with lowercase letters only: ")

    cipher = get_rot13(string)
    print(f"Your string \"{string}\" converts to \"{cipher}\".")
main()