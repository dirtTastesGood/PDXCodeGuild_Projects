def swap_keys(original_dict):
    new_dict = {value: key for key, value in original_dict.items()}
    return new_dict

def main():
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    original = {keys[i] : values[i] for i in range(len(keys))}
    
    print(f"\nOriginal dictionary: {original}")
    
    print(f"Swapped dictionary: {swap_keys(original)}")
main()
