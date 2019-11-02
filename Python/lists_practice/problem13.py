import random

def minimum(nums):
    return min(nums)

def maximum(nums):
    return max(nums)

def mean(nums):
    return sum(nums) / len(nums)

def mode(nums):
    counts = {}
    the_mode = 0
    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
        
        if counts[num] > the_mode:
            the_mode = num

    return the_mode

def main():
    nums = [random.randint(1, 100) for i in range(10)]

    print(nums)
    print(f"Min: {minimum(nums)}")
    print(f"Max: {maximum(nums)}")
    print(f"Mean: {mean(nums)}")
    print(f"Mode: {mode(nums)}")

main()
