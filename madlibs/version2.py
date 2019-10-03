
print("\nPlease enter:")

adjectives = input("Five adjectives, separated by commas, then press enter: ").split(",")
gerunds = input("Two \"-ing\" verbs, separated by commas: ").split(",")
place = input("A place: ")
plural_noun = input("A plural noun: ")
noun = input("A noun: ")

adjective_1 = adjectives[0]
adjective_2 = adjectives[1]
adjective_3 = adjectives[2]
adjective_4 = adjectives[3]
adjective_5 = adjectives[4]

verb_1 = gerunds[0]
verb_2 = gerunds[1]


print("If you go to some", adjective_1, "place like", place, ", you must know how to deal with wild animals such as bears, wolves and", plural_noun, ". The most important of these is the bear. There are three kinds of bear, the grizzly bear, the", adjective_2, "bear and the", adjective_3, "bear. Bears spend most of their time", verb_1, "or", verb_2, ". They look very", adjective_4, ", but if you make them", adjective_5, ", they might bite your", noun, ".")
