import random

def answerQuestion():

    options = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes","Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

    choice = random.choice(options)

    return choice

def main():
    print("\nCome one, come all, look through truth's eye! Ask the Magic 8-ball your questions!")

    while True:    
        question = input("\nType your question here or enter \'done\' to exit: ")

        if question.lower() == "done":
            break
        else:
            print(answerQuestion())

main()