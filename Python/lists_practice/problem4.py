def every_other(a):
    return [i for i in range(len(a)) if i % 2 == 0]

def main():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    print(f"Every other number in {nums} is {every_other(nums)}")

main()
