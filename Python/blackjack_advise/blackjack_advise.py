def get_score(cards):
    card_scores = {"a": 1,
                   "2": 2,
                   "3": 3,
                   "4": 4,
                   "5": 5,
                   "6": 6,
                   "7": 7,
                   "8": 8,
                   "9": 9,
                   "10": 10,
                   "j": 10,
                   "q": 10,
                   "k": 10,
                   "A": 11
                  }
    score = 0
    for card in cards:
        card.lower()
        if card == 'a' and (score + card_scores['A']) <= 21:
            card = 'A'
        
        score += card_scores[card]

    return score

def score_advise(score):
    if score < 17:
        advise = "You should proabably hit."
    elif 17 <= score < 21:
        advise = "You should probably stay."
    elif score == 21:
        advise = "You've already acheived Blackjack"
    elif score > 21:
        advise = "You've busted."

    return advise

def main():
    cards = []

    print("\nWelcome to Blackjack Adviser. Please enter three cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)")
    
    cards.append(input("\nPlease enter your first card: ").lower())
    cards.append(input("\nPlease enter your second card: ").lower())
    cards.append(input("\nPlease enter your third card: ").lower())
    score = get_score(cards)

    advise = score_advise(score)
    
    print(f"Your score is {score}. {advise}")

main()