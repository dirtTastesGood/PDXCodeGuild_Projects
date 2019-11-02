def double_chars(string):
    words = string.split(" ")
    
    doubled = [[char * 2 for char in word] for word in words]
    
    doubled = [''.join(i) for i in doubled]
    
    return ' '.join(doubled)

def main():
    user_string = input("\nPlease enter a word or phrase: ")

    print(double_chars(user_string))

main()
