import random

# Define the suits and values of the cards
suits = ['♠', '♡', '♣', '♢']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

buy_in = 10000 # start money
big_blind = 200
small_blind = 100

turn_num = None
min_raise = None
prev_bet = 0

class Player:
    def __init__ (self, number, chips):
        self.number = number
        self.chips = chips
        self.hand = []

# creates the deck
def new_deck():
    deck = [(value, suit) for value in values for suit in suits]
    random.shuffle(deck)
    return deck

# function to deal 2 cards
def deal_cards():
    for player in players:
        player.hand = [deck.pop(), deck.pop()]

def min_raise_check():
    if turn_num == 0:
        min_raise = big_blind
    else:
        min_raise = prev_bet
    return min_raise
        

def flop():
    flop_cards = [deck.pop() for i in range(3)]
    return flop_cards

def turn():
    turn_card = deck.pop()
    return turn_card

def river():
    river_card = deck.pop()
    return river_card

#creates the players
num_players = 5
players = [Player(i+1, buy_in) for i in range(num_players)]

deck = new_deck() #creates the deck
deal_cards() #gives 2 cards to each player

print(f'De small blind is €{small_blind}.')
print(f'De big blind is €{big_blind}.')
print(f'De buy-in is €{buy_in}.')
print(f'Inzet is in hele euros!')

turn_num = 0
min_raise = min_raise_check()

print(f'De minimum raise is {min_raise} ')

print(f'Speler {players[0].number} dit zijn je Hole cards: {players[0].hand}')

real_player_count = 5 #real_player_creation()
