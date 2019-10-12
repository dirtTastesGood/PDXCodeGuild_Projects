def num_to_phrase(split_num):
    num_names = {0:{1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"},
                 1:{1:"eleven", 2:"twelve", 3:"thirteen", 4:"fourteen", 5:"fifteen", 6:"sixteen", 7:"seventeen", 8:"eighteen", 9:"nineteen"},
                 2:"twenty",
                 3:"thirty",
                 4:"forty",
                 5:"fifty",
                 6:"sixty",
                 7:"seventy",
                 8:"eighty",
                 9:"ninety" 
                } 

    hundreds = split_num[0]
    tens = split_num[1]
    ones = split_num[2]

    print(f"{hundreds} {tens} {ones}")
    phrase = ""

    if hundreds > 0:
        phrase += num_names[0][hundreds]
        phrase += " hundred "
    
    if tens == 0 or tens == 1:
        phrase += num_names[tens][ones]
    
    if tens > 1:
        phrase += num_names[tens] 
        if ones > 0:
            phrase += "-" + num_names[0][ones]
    return phrase

def split_number(num):
    # split number into hundreds, tens and ones
    split_num = []

    hundreds = num // 100
    split_num.append(hundreds)
    num -= hundreds * 100

    tens = num // 10
    split_num.append(tens)

    ones = num % 10
    split_num.append(ones)

    return split_num

def main():
    num = int(input("\nPlease enter a number 1-999: "))
    split_num = split_number(num)

    phrase = num_to_phrase(split_num)

    print(f"Digits: {num}, written: {phrase}")

main()