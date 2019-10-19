def average_similar_keys(d):
    new_d = {}

    letters = []
    nums = []

    for key in d.keys():
        nums.append(key[1])
    nums = set(nums)

    for key in d.keys():
        letters.append(key[0])
    letters = set(letters)
   
    for letter in letters:
        new_d[letter] = 0
        for num in nums:
            new_d[letter] += d[f'{letter}{num}']
        new_d[letter] = new_d[letter] // len(nums)
    return new_d
def main():
    d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}

    print(average_similar_keys(d))

main()
