import random

def check_guess(guess, answer):
    if guess == answer:
        return True
    else: 
        return False

def high_low(guess, answer):
    if guess < answer:
        msg = "Your guess is too low!"
    elif guess > answer:
        msg = "Your guess is too high!"
    
    return msg

def error_margin(curr_guess, prev_guess, answer):
    prev_margin = abs(prev_guess - answer)
    curr_margin = abs(curr_guess - answer)

    if curr_margin > prev_margin:
        msg = f"Your guess of {curr_guess} is further from the answer than your last guess of {prev_guess}."
    elif curr_margin < prev_margin:
        msg = f"Your guess of {curr_guess} is closer to the answer than your last guess of {prev_guess}."
    else:
        msg = ""
    return msg

def generate_guess(bottom, top):
    guess = random.randint(bottom, top)

    return guess

def human_player():
    answer = random.randint(1,10)
    
    print("Welcome! The computer has chosen a number between 1 and 10. Try to guess the number in ten tries or less!")

    guesses = []
    prev_guess = answer
    
    while True:
        guess = int(input(f"\nEnter guess ('q' to quit): "))
        guesses.append(guess)

        if check_guess(guess, answer) == True:
            print(f"\nYou guessed correctly! {guess} is the number the computer chose. \nGreat job! \nNumber of guesses: {len(guesses)}")
            break

        elif check_guess(guess, answer) == False:
            hi_lo = high_low(guess,answer)
            accuracy = error_margin(guess, prev_guess, answer)
            prev_guess = guess

            print(f"{guess} is not the correct number. {hi_lo}.")
            if len(guesses) > 1:
                print(f"{accuracy} Try again.")
        
        if str(guess).lower() == "q":
           break

def computer_player():
    target = int(input("\nPlease enter a number between 1 and 10 for the computer to guess."))
            
    bottom = 1
    top = 10
    
    guesses = []
    guess = generate_guess(bottom, top)

    if check_guess(guess, target) == True:
        print("got it!")
    elif check_guess(guess, target) == False:
        print("try again")

    # check guess
    # higher or lower than target
    # augment guess, if higher, random number lower than previous guess. If lower, guess higher.
    # repeat until answer is found
    # print iterations
    
    pass          

def main():
    while True: 

        player = input("\nWho would you like the player to be? \n\n1. Human\n2. Computer\n\nEnter 1 or 2 or 'q' to quit: ")

        if player == "1":
            human_player()
        elif player == "2":
            computer_player()

        if player.lower() == 'q':
            break

main()