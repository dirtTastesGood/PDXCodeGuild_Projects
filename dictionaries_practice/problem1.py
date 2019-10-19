def combine(a,b):
    return {a[i]:b[i] for i in range(len(a))}

def main():
    fruits = ['apple', 'banana', 'pear']
    prices = [1.2, 3.3, 2.1]

    print(f"keys: {fruits}, values: {prices}\ndictionary: {combine(fruits, prices)}")
main()
