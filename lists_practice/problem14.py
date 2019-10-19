def unique(nums):
    uniques = []
    [uniques.append(num) for num in nums if num not in uniques]
    return uniques
    
def main():
    nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155, 17, 32, 100, 32, 17]

    print(nums)
    print(f"Unique numbers in list: {unique(nums)}")
main()
