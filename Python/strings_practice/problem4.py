def count_substring(main_string, substring):
    return main_string.count(substring)

def main():
    
    main_string = "mellow yellow bellow fellow"
    substring = "ellow"

    substring_count = count_substring(main_string, substring)
    
    print(f"\nThe substring \'{substring}\' appears in the string \'{main_string}\' {substring_count} times.")

main()
