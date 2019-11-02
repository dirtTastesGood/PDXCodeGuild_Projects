def even_even(a):
    result = [i for i in a if i % 2 == 0]
    return True if len(result) % 2 == 0 else False

def main():
    list1 = [1,2,3,4,5]
    list2 = [4,5,4,5,4,5]

    print("Do the following lists contain an even number of even numbers:")
    print(f"{list1}: {even_even(list1)}")
    print(f"{list2}: {even_even(list2)}")
main()
