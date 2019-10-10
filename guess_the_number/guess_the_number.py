import random

def check_guess(guess, answer):
    if guess == answer:
        return True
    else: 
        return False

def main():
    answer = random.randint(1,10)
    
    print("Welcome! The computer has chosen a number between 1 and 10. Try to guess the number in ten tries or less!")

    guesses = []

    while len(guesses) < 10: 
        guess = int(input(f"\nEnter guess: "))
        guesses.append(guess)
        
        if check_guess(guess, answer) == True:

            print(f"\nYou guessed correctly! {guess} is the number the computer chose. \nGreat job! \nNumber of guesses: {len(guesses)}")
            break
        elif check_guess(guess, answer) == False:
            if len(guesses) < 10:
                print(f"{guess} is not the correct number. Try again. {9-len(guesses)} guesses left")
            else:
                print(f"\nYou've used all your guesses. \nThe numbers you tried were: {', '.join(str(x) for x in guesses)}. \nHowever, the computer chose {answer}.")
                break           
main()