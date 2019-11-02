def average(numbers):
    sum = 0
    for num in numbers:
        sum += int(num)

    return sum, sum / len(numbers)

def display_result(nums, avg):
    pass

def main():
    nums = []

    while True:
        num = input("\nPlease enter a number or 'done' to exit: ")
        if num.lower() == "done":
            break
        else:
            nums.append(num)

    sum, avg = average(nums)
    print(f"\nThe sum of the numbers {', '.join(nums)} is {sum}. The average is {avg}.")

main()