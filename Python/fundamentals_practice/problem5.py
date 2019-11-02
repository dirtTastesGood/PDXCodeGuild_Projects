def power_of(num, exp):
    return num ** exp

def main():
    num = 2
    lim = 20
    
    i = 0
    while i <= lim:    
        print(f"{num} to the power of {i} is {power_of(num, i)}")
        i += 1
main()