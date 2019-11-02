from math import ceil

def text_counts(text):
    counts = {'chars':0, 'words':0, 'sentences':0}
    punct = ['.', '!', '?']
    text = text.replace("\n", " ").split(" ")

    sentence = []

    for i, word in enumerate(text):

        word = word.lower()
        if word == '':
            del text[i]
        else:
            counts['words'] += 1

            text[i] = word.replace(",", "")
            counts['chars'] += len(word)

            if word.lower() == "mr." or word.lower() == "mrs.":
                text[i] = word.replace(".", "")
            
            sentence.append(word)
            if word[-1] in punct:
                counts['sentences'] += 1
                sentence = []


    return counts

def get_ari(counts):
    ari = ceil((4.71 * (counts['chars'] / counts['words'])) + (0.5 * (counts['words'] / counts['sentences'])) - 21.43)
    
    return ari

def get_grade_level(ari):
    passari_scale = {
        1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
        2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
        3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
        4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
        5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
        6: {'ages': '10-11', 'grade_level':    '5th Grade'},
        7: {'ages': '11-12', 'grade_level':    '6th Grade'},
        8: {'ages': '12-13', 'grade_level':    '7th Grade'},
        9: {'ages': '13-14', 'grade_level':    '8th Grade'},
        10: {'ages': '14-15', 'grade_level':    '9th Grade'},
        11: {'ages': '15-16', 'grade_level':   '10th Grade'},
        12: {'ages': '16-17', 'grade_level':   '11th Grade'},
        13: {'ages': '17-18', 'grade_level':   '12th Grade'},
        14: {'ages': '18-22', 'grade_level':      'College'}
    }

    return passari_scale[ari]

def main():
    with open('metamorphosis.txt', 'r') as book_file:
        counts = text_counts(book_file.read())

    ari = get_ari(counts)
    if ari > 14:
        ari = 14
    ari_info = get_grade_level(ari)

    print(f"The ARI for {book_file.name} is {ari}.\nThis indicates a/an {ari_info['grade_level']} reading difficulty that is suitable for ages {ari_info['ages']}")

main()
