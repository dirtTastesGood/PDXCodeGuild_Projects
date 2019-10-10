import random

def check_guess(guess, target):
    if guess == target:
        return True
    else: 
        return False

def high_low(guess, target):
    if guess < target:
        msg = "low"
    elif guess > target:
        msg = "high"
    else: 
        msg = ""
    return msg

def error_margin(curr_guess, prev_guess, target):
    prev_margin = abs(prev_guess - target)
    curr_margin = abs(curr_guess - target)

    if curr_margin > prev_margin:
        msg = "farther"
    elif curr_margin < prev_margin:
        msg = "closer"
    else:
        msg = ""
    return msg

def generate_guess(bottom, top):
    guess = random.randint(bottom, top)

    return guess

def human_player():
    target = random.randint(1,10)
    
    print("Welcome! The computer has chosen a number between 1 and 10. Try to guess the number in ten tries or less!")

    guesses = []
    
    while True:
        guess = int(input(f"\nEnter guess ('q' to quit): "))

        guesses.append(guess)

        if check_guess(guess, target) == True:
            print(f"\nYou guessed correctly! {guess} is the number the computer chose. \nGreat job! \nNumber of guesses: {len(guesses)}")
            break

        elif check_guess(guess, target) == False:

            hi_lo = high_low(guess,target)

            if hi_lo == "low":
                hi_lo_msg = "Your guess is too low!"
            elif hi_lo == "high":
                hi_lo_msg = "Your guess is too high!"

            print(f"{guess} is not the correct number. {hi_lo_msg}.")

            if len(guesses) > 1:
                accuracy = error_margin(guess, guesses[-2], target)

                if accuracy == "closer":
                    print(f"Your guess of {guesses[-1]} is closer to the target than your last guess of {guesses[-2]}.")
                elif accuracy == "farther":
                    print(f"Your guess of {guesses[-1]} is farther from the target than your last guess of {guesses[-2]}.")
        if str(guess).lower() == "q":
           break

def computer_player():
    target = int(input("\nPlease enter a number between 1 and 10 for the computer to guess."))

    guesses = []

    bottom = 1
    top = 10

    while True:

        guess = generate_guess(bottom, top)

        print(f"Guess: {guess}")
        print(f"target: {target}")

        guesses.append(guess)
    
        if check_guess(guess, target) == True:
            print(f"I got it! Your number is {target}. My guesses: {guesses}")
            break
        elif check_guess(guess, target) == False:
            hi_lo = high_low(guess, target)
         
            if hi_lo == "low":
                bottom = guess
            elif hi_lo == "high":
                top = guess  

            # if len(guesses) > 1:
            #     accuracy = error_margin(guess, guesses[-2], target)
                
            #     if accuracy == "farther":
            #         pass
            #     if accuracy == "closer":
            #         pass

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