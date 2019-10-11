def within_10(num, targ, lim):
    if abs(num-targ) <= lim:
        return True
    else:
        return False

def main():
    nums = [99, 105, 65, 85, 90, 110]
    targ = 100
    lim = 10

    print(f"\nAre the following numbers within {lim} of {targ}?")
    for num in nums:
        print(f"{num}: {within_10(num, targ, lim)}")

main()