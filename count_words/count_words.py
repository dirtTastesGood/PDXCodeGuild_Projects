import string

def strip_text(text):
    exclude = set(string.punctuation)
    text = ''.join(char for char in text if char not in exclude)

    return text.lower().replace("  ", " ").replace("\n", " ").split(" ")

def count_words(word_list):
    word_dict = {}

    for word in word_list:
        if word not in word_dict:
           word_dict[word] = 1
        elif word_dict[word]:
            word_dict[word] += 1

    return word_dict

def most_frequent_words(word_dict):
    tup_list = []

    words = list(word_dict.items())
    words.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(words))):
        tup_list.append(words[i])

    return tup_list

def main():
    with open('metamorphosis.txt', 'r') as book_file:
        word_list = strip_text(book_file.read())
        word_dict = count_words(word_list)
    
    words = most_frequent_words(word_dict)
    
    print("\nThe 10 most common words in the text are:")
    for word in words:
        print(f"{word[0]}: {word[1]}")

main()