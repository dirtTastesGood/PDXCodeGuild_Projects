def validate(numbers):
    num_list = list(numbers)
    num_list = [int(i) for i in num_list]
    
    check_digit = num_list[-1]
    del num_list[-1]

    num_list = num_list[::-1]

    num_sum = 0

    for i, num in enumerate(num_list):
        if i % 2 == 0:
            num_list[i] = num * 2
            
            if num_list[i] > 9:
                num_list[i] -= 9
        num_sum += num
    
    num_sum = str(num_sum)
    if int(num_sum[1]) == check_digit:
        return "valid"
    else:
        return "invalid"

def main():
    cc_num = "4556737586899855"
    
    print(validate(cc_num))

main()