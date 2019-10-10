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

def main():
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
           
main()