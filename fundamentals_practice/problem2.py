def is_opposite(x,y):
    if (x < 0 and y > 0) or (y < 0 and x > 0):
        return True
    else:
        return False

def main():
    pairs = ((10, -1), (2,3), (-1,-1))

    print("Opposite signs?")
    for pair in pairs:
        print(f"{pair}: {is_opposite(pair[0], pair[1])}.")

main()