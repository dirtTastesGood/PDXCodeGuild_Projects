def count_char(char, word):
    return word.count(char)

def main():
    print(f"p's in \'pneumonoultramicroscopicsilicovolcanoconiosis\': {count_char('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')}")
    print(f"i's in \'antidisestablishmentterianism\': {count_char('i', 'antidisestablishmentterianism')}")

main()
