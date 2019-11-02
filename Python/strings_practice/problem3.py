import string

def latest_letter(user_string):
    latest = 0
    alphabet = string.ascii_lowercase

    for char in user_string:
        if int(alphabet.index(char)) > latest:
            latest = int(alphabet.index(char))

    return alphabet[latest]

def main():
    word = "supercalifragilisticexpialidocious"

    print(f"\nThe letter closest to 'z' in \'{word}\' is \'{latest_letter(word)}\'")
main()
