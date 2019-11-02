import string

def to_ascii(letters):
    return {i: ord(i) for i in letters}


def main():
    alphabet = string.ascii_lowercase

    for i in to_ascii(alphabet).items():
        print(f"letter {i[0]}, ascii: {i[1]}")    

main()
