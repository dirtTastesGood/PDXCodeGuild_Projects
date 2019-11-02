def missing_char(word):
    return [f"{word[:i]}{word[i+1::]}" for i in range(len(word))]
    
def main():
    word = "ornery"
    print(f"\nWord: {word}")
    print("\nWith chars missing: ")
    [print(i) for i in missing_char(word)]

main()