def powers_of_two():
    powers = [2 ** n for n in range(10)]
    return powers

def main():
    print(f"Two to the power of 0-10: {powers_of_two()}")
    
main()
