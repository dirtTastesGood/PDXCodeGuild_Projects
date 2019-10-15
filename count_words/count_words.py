import string

def strip_line(line):
    exclude = set(string.punctuation)
    line = ''.join(char for char in line if char not in exclude)
    return line.lower().replace("  ", " ").strip("\n").split(" ")

def count_words(text, word_dict):
    for word in text:
        if word not in word_dict:
           word_dict[word] = 1
        elif word_dict[word]:
            word_dict[word] += 1
    return word_dict

def most_frequent(word_dict):
    word_list = []

    words = list(word_dict.items())
    words.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(words))):
        word_list.append(words[i])

    return word_list

def main():
    word_dict = {}

    with open('metamorphosis.txt', 'r') as book_file:
        for line in book_file:
            count_words(strip_line(line), word_dict)

    words = most_frequent(word_dict)
    
    print("\nThe 10 most common words in the text are:")
    for word in words:
        print(f"{word[0]}: {word[1]}")
main()