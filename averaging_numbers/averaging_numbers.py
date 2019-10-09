def average(numbers):
    sum = 0
    for num in numbers:
        sum += num

    return sum/len(numbers)

def main():
    nums = [1,2,3,4,5,6,7,8,9]
    print(f"\nThe average of the numbers {nums} is {average(nums)}")

main()