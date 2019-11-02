import random

def choose_random(a):
    return a[random.randint(0, len(a)-1)]

def main():
    fruits=['apple', 'banana', 'tangerine', 'watermelon']

    print(choose_random(fruits))
main()
