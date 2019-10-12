def check_anagram(string1, string2):
    list1 = sorted(string1.lower().replace(" ", ""))
    list2 = sorted(string2.lower().replace(" ", ""))
    
    if list1 == list2:
        return True
    else:
        return False

def check_palindrome(string):
    string = string.lower().replace(" ","")

    if string[::-1] == string:
        return True
    else:
        return False

def main():
    anagram_strings = [["i am lord voldemort","tom marvolo riddle"], ["you are a wizard harry", "welcome to hogwarts"]]
    palindrome_strings = ["taco cat", "just a flesh wound", "racecar"]

    print("\nAnagrams: ")
    for pair in anagram_strings:
        if check_anagram(pair[0], pair[1]):
            print(f"Yes, \"{pair[0]}\" is an anagram of \"{pair[1]}\"")
        else: 
            print(f"Sorry, \"{pair[0]}\" is not an anagram of \"{pair[1]}\"")

    print("\nPalindromes: ")
    for string in palindrome_strings:
        if check_palindrome(string):
            print(f"Yes, \"{string}\" is a palindrome.")
        else:
            print(f"Sorry, \"{string}\" is not a palindrome.")
    
main()