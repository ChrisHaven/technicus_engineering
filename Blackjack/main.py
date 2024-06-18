import random

chips = 100

player_hand = []
dealer_hand = []

blackjack = False

# Define the suits and values of the cards
suits = ['♠', '♡', '♣', '♢']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
deck = [(value, suit) for value in values for suit in suits]
shoe = deck * 6

def new_shoe():
    global shoe
    random.shuffle(shoe)

def dis_hand(hand):
    display_hand = ''.join(str(x) for x in hand)
    return display_hand

def player_start():
    global player_hand
    player_hand = [shoe.pop(), shoe.pop()]
    display_hand = dis_hand(player_hand)
    print(f'Je hand is {display_hand} met een waarde van {calculate_hand_value(player_hand)}')
    print('')

    global first_turn
    first_turn = True

def dealer_start():
    global dealer_hand 
    dealer_hand = [shoe.pop(), shoe.pop()]
    display_hand = dis_hand(dealer_hand)

def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card[0] in ['J', 'Q', 'K']:
            value += 10
        elif card[0] == 'A':
            value += 11
            aces += 1
        else:
            value = value + card[0]
    while value > 21 and aces > 0:
        if aces > 1:
            value -= 10
            aces -= 1
        if value == 21:
            value = 21
    return value
        

def choice():
    value = calculate_hand_value(player_hand)
    if value == 21:
        print('je hand is 21 dus je kan niet meer hitten.')
    elif value > 21:
        bust()
    else:
        print('Wat wil je doen?')
        player_choice = input('kies hit of stand?) ')
        print('')

        if player_choice == 'hit':
            hit()
            choice()
        elif player_choice == 'stand':
            stand()
        else:
            print('Ongeldige keuze!')
            choice()

def hit():
    global first_turn

    global player_hand
    player_hand.append(shoe.pop())
    display_hand = dis_hand(player_hand)

    value = calculate_hand_value(player_hand)

    print(f'Je nieuwe hand is: {display_hand}')
    print(f'De totale waarde is: {value}')
    print('')

def stand():
    print('Je hebt gestand')
    display_hand = dis_hand(player_hand)
    print(f'Je hand is: {display_hand}')
    print(f'De waarde van je hand is {value}')

def bust():
    global player_hand
    value = calculate_hand_value(player_hand)
    player_hand = []
    print(f'{value} is helaas te veel :( probeer opnieuw')
    print('')

new_shoe()
player_start()

value = calculate_hand_value(player_hand)
if value == 21:
    print('Gefeliciteerd je hebt blackjack!')
else:
    choice()