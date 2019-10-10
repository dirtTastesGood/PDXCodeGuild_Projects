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

    while True: 
        guess = int(input(f"\nEnter guess ('q' to quit): "))
        guesses.append(guess)
        
        if check_guess(guess, answer) == True:
            print(f"\nYou guessed correctly! {guess} is the number the computer chose. \nGreat job! \nNumber of guesses: {len(guesses)}")
            break
        elif check_guess(guess, answer) == False:
            print(f"{guess} is not the correct number. Try again.")
        
        if str(guess).lower() == "q":
            break
           
main()