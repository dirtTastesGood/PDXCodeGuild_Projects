def merge(a,b):
    pairs = []

    [pairs.append([a[i], b[i]]) for i in range(len(a))]

    return pairs

def main():
    list1 = ["a", "b", "c"]
    list2 = [1,2,3]

    print(f"{list1}, {list2}. Merged: {merge(list1, list2)}")
main()
