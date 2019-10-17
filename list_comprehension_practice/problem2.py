def first_ten_evens():
    evens = [n for n in range(1, 21) if n % 2 == 0]
    return evens

def main():
    print(f"First ten even numbers : {first_ten_evens()}")
    
main()
