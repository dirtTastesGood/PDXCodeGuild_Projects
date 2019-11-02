def compare_substring_counts(main_string, substring1, substring2):
    count1 = main_string.count(substring1)
    count2 = main_string.count(substring2)

    return count1 == count2

def main():
    substring1 = "cat"
    substring2 = "dog"
    main_string = "cat dog cat dog"

    print(f"\'{substring1}\' occurs the same number of times as \'{substring2}\' in the string \'{main_string}\': {compare_substring_counts(main_string, substring1, substring2)}")

main()
