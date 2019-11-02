import random
throws = ["rock", "paper", "scissors"]




def main():
    

    while True:
        print("\n Let's play Rock, Paper, Scissors!")
        user_throw = input("\n Please choose rock, paper, or scissors ('q' to quit): ").lower()

        comp_throw = comp_choose()
        outcome = get_outcome(comp_throw, user_throw)
        print_outcome(outcome, comp_throw, user_throw)
        if user_throw == 'q':
            break
def comp_choose():
    throws = ["rock", "paper", "scissors"]

    comp_throw = random.choice(throws)

    return comp_throw

def get_outcome(comp_throw, user_throw):
    if user_throw == comp_throw:
        outcome = "You tied with the computer!"
    elif (user_throw == "scissors" and comp_throw == "paper") or (user_throw == "paper" and comp_throw == "rock") or (user_throw == "rock" and comp_throw == "scissors"):
        outcome = "You won!"
    elif (user_throw == "paper" and comp_throw == "scissors") or (user_throw == "rock" and comp_throw == "paper") or (user_throw == "rock" and comp_throw == "paper"):
        outcome = "The computer won!"

    return outcome

def print_outcome(outcome, comp_throw, user_throw):
    print(f"The computer threw {comp_throw}. You threw {user_throw}.")
    print(outcome)

main()