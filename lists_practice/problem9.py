def find_pairs(nums, target):
    pairs = []
    for i in nums:
        for j in range(len(nums)):
            if i + nums[j] == target:
                pairs.append((i, nums[j]))
            
    return pairs

def main():
    nums = [1,2,3,4,5,6]
    target = 7

    print(f"Pairs of numbers in {nums} whose sum is {target}: {find_pairs(nums, target)}")
main()
