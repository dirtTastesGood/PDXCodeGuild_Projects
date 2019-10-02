print("\nPlease enter: \n")

adjective_1 = input("Adjective: ")
place = input("Place: ")
plural_noun = input("Plural noun: ")
adjective_2 = input("Adjective: ")
adjective_3 = input("Adjective: ")
verb_1 = input("\"ing\" verb: ")
verb_2 = input("\"ing\" verb: ")
adjective_4 = input("Adjective: ")
adjective_5 = input("Adjective: ")
noun_1 = input("Noun: ")
# vehicle = input("Vehicle: ")
# food_1 = input("Food (plural)")
# body_part = input("Part of the body (plural): ")
# adjective_6 = input("Adjective: ")
# food_2 = input("Food (plural): ")
# food_3 = input("Food (plural): ")
# live_thing_1 = input("Something alive: ")
# live_thing_2 = input("Something else alive: ")
# adjective_7 = input("Adjective: ")

print("If you go to some", adjective_1, "place like", place, ", you must know how to deal with wild animals such as bears, wolves and", plural_noun, ". The most important of these is the bear. There are three kinds of bear, the grizzly bear, the", adjective_2, "bear and the", adjective_3, "bear. Bears spend most of their time", verb_1, "or", verb_2, ". They look very", adjective_4, ", but if you make them", adjective_5, ", they might bite your", noun_1, ".")

# , ". Bears will come up to your ", vehicle, " and beg for ", food_1, ". They will stand on their hind legs and clap their ", body_part, " together and pretend to be ", adjective_6, ". However, do not get out of your ", vehicle, " or offer the bears", food_2, " or ", food_3, ". This applies to other wild creatures as well, including the ", live_thing_1, " and the ", live_thing_2, ". Remember these rules and your vacation will be ", adjective_7, " and you won't be eaten by a bear.")

## Version 2: Use lists. Ask for x adjectives, separated by commas, then use split() to store each separately
## Version 3: Make a repeatable game