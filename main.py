import random
print("Are you 18: ")
if input() != "yes":
  kill
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

def deal_card():
    return random.choice(deck)

def total(hand):
    t = sum(hand)
    if t <= 11 and 11 in hand:
        return t + 10
    return t

def is_bust(hand):
    return total(hand) > 21

def show_hand(hand, name='Dealer'):
    print(f'{name} hand: {hand} (Total: {total(hand)})')

def play_again():
    return input('Do you want to play again? (yes or no) ').lower().startswith('y')

while True:
    print('Welcome to Blackjack!')
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    while True:
        show_hand(player_hand, 'Player')
        if is_bust(player_hand):
            print('You bust!')
            break

        action = input('Do you want to hit or stand? ').lower()
        if action == 'hit':
            player_hand.append(deal_card())
        elif action == "stand":
            break
        


