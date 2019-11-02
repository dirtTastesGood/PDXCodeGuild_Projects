def combine(a, b):
    new_list = []    
    for i in range(len(a)):
        new_list.append(a[i])
        new_list.append(b[i])
    return new_list

def main():
    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3]

    print(f"{list1} combined with {list2} is: ")
    print(combine(list1, list2))

main()
