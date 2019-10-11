def largest_num(a, b, c):
    largest = 0
    nums = [a,b,c]

    for num in nums:
        if num > largest:
            largest = num
        else:
            continue 

    return largest   

def main():
    x = -1
    y = 10
    z = 6

    print(f"Of {x}, {y}, and {z}, which is the largest?")
    print(largest_num(x,y,z))

main()
