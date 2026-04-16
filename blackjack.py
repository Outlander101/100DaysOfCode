import random

def create_deck():
    """Creates a standard 52-card deck and shuffles it."""
    ranks = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deck = ranks * 4
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    """Removes and returns the top card from the deck."""
    return deck.pop()

def calculate_sum(cards):
    """ Returns sum of cards"""
    # Standard ACE logic, convert 11 to 1 when score > 21
    score = sum(cards)
    while 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def main():
    deck = create_deck()
    user_cards = []
    dealer_cards = []
    for _ in range(2):
        user_cards.append(deal_cards(deck))
        dealer_cards.append(deal_cards(deck))
    is_game_over = False

    # User's Turn
    while not is_game_over:
        user_score = calculate_sum(user_cards)
        print(f"User Cards: {user_cards}, User Score: {user_score}")
        print(f"Dealer Card: {dealer_cards[0]}")
        
        if user_score >= 21:
            is_game_over = True
        else:
            # Hit/Stand
            user_should_deal = input("User can get another card 'y' or pass 'n': ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_cards(deck))
            else:
                is_game_over = True
    
    # Dealer's Turn, only when user hasn't busted
    while calculate_sum(user_cards) <= 21 and calculate_sum(dealer_cards) < 17:
        dealer_cards.append(deal_cards(deck))
    
    # Final Cards and Scores
    user_score = calculate_sum(user_cards)
    dealer_score = calculate_sum(dealer_cards)

    print(f"Final User Hand: {user_cards}, Final User Score: {user_score}")
    print(f"Final Dealer Hands: {dealer_cards}, Final Dealer Score: {dealer_score}")

    if user_score > 21:
        print("User went over, Dealer wins")
    elif dealer_score > 21:
        print("Dealer went over, User wins")
    elif user_score > dealer_score:
        print("User wins")
    elif dealer_score > user_score:
        print("Dealer wins")
    else:
        print("It's a Draw.")

if __name__ == '__main__':
    main()

                    
        
