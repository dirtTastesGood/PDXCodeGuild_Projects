import random

def pick6():
    nums = []
    i = 0
    while i < 6:
        num = random.randint(1,99)
        nums.append(num)
        i += 1
    return nums

def check_ticket(ticket, goal):
    matches = []
    for index, num in enumerate(ticket):
        if num == goal[index]:
            matches.append(num)
        else:
            matches.append(0)

    return matches     

def collect_winnings(matches):
    scores = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000} # number of matches vs dollar rewards    
    
    i = 0 # number of matches
    for num in matches:
        if num > 0:
            i += 1      
    
    reward = scores[i]
    return reward

def main():
    plays = int(input("\nWelcome to Pick 6. Enter the number of times you'd like to play: "))

    winning_ticket = pick6()
    ticket_price = 2
    balance = 0

    i = 0
    while i < plays:
        balance -= ticket_price

        ticket = pick6()

        matches = check_ticket(ticket, winning_ticket)

        reward = collect_winnings(matches)

        if reward:
            balance += reward
    
        i += 1

    print(f"Your final balance is {balance}.")

main()