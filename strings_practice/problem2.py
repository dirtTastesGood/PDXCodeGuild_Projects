def missing_char(word):
    variations = [f"{word[:i]}{word[i+1::]}" for i in range(len(word))]

    return variations
    
def main():
    word = "ornery"
    print(f"\nWord: {word}")
    print("\nWith chars missing: ")
    [print(i) for i in missing_char(word)]

main()