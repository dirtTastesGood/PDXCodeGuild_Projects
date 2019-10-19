def common_elements(a, b):
    return [i for i in a if i in b]

def main():
    list1 = ['cat', 'dog', 'turtle', 'elephant','giraffe', 'rhinoceros']
    list2 = ['turtle', 'dog', 'rhinoceros']

    print(f"The common elements in {list1} and {list2} are:\n {common_elements(list1, list2)}")

main()
