import random
throws = ["rock", "paper", "scissors"]

print("\n Let's play Rock, Paper, Scissors!")
user_throw = input("\n Please choose rock, paper, or scissors: ").lower()

comp_throw = random.choice(throws)

if user_throw == comp_throw:
    outcome = "You tied with the computer!"
elif (user_throw == "scissors" and comp_throw == "paper") or (user_throw == "paper" and comp_throw == "rock") or (user_throw == "rock" and comp_throw == "scissors"):
    outcome = "You won!"
elif (user_throw == "paper" and comp_throw == "scissors") or (user_throw == "rock" and comp_throw == "paper") or (user_throw == "rock" and comp_throw == "paper"):
    outcome = "The computer won!"

print(f"The computer threw {comp_throw}. You threw {user_throw}.")
print(outcome)
