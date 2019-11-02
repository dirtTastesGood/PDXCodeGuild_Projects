def main():
    nums = []
    while True:
        num = input("Please enter a number to be inserted into your list (or 'done' to print your list): ")
        if num.lower() == 'done':
            break
        else: 
            nums.append(num)
    print(nums)
main()
