def main():
    pass

main()


from random import randint, choice

def roll_die(die):
    print(die)

def main():
    centered_chips = 0
    dice = []
    for x in range(0,3):
       dice.append(['l', 'c', 'r', 'dot', 'dot', 'dot'])

    players = {}
    while True:
        player_name = input(f"Please enter the name of player {len(players)+1} (or 'done' to begin the game): ")
        
        if player_name.lower() == "done":
            break
        else:
            players[player_name] = {'score': 0, 'chips':0}
    

    print(players)
    for die in dice:
        print(die.roll())

main()