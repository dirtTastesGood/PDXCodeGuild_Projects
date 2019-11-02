def is_even(num):
    if num % 2 == 0:
        return "even"
    elif num % 2 == 1:
        return "odd"

print(f"5 is {is_even(5)}.")
print(f"6 is {is_even(6)}.")