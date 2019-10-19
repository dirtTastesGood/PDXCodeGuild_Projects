def combine_all(nums):
    unpacked_nums = []
    for i in nums:
        for j in i:
            unpacked_nums.append(j)

    return unpacked_nums       

def main():
    nums = [[5,2,3],[4,5,1],[7,6,3]]

    print(f"{nums} combined into one list is: {combine_all(nums)}")
main()
