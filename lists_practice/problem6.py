def all_less_than_10(l):
    return [i for i in l if i < 10]
def main():
    my_list = [1,11,2,12,3,13,4,14,5,15,6,16,7,17,8,18,9,19]

    print(f"All numbers less than ten in {my_list} are: {all_less_than_10(my_list)}")
main()
