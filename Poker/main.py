import random

# Define the suits and values of the cards
suits = ['♠', '♡', '♣', '♢']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

buy_in = 10000 # start money
big_blind = 200
small_blind = 100
pot = 0

turn_num = None
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
        
def pre_flop():
    turn_num = 0
    for i in range(player_count):
        if players[i].hand == []:
            turn_num = turn_num + 1
            print(f'speler{players[i].number} heeft gefold en doet dus niet meer mee!')
        else:
            choice = input(f'Speler{players[i].number} wat wil je doen? fold, check of bet) ')
            turn_choice(choice, i)
            turn_num = turn_num + 1
    return turn_num

def flop():
    print('flop')

def turn():
    print('turn')

def river():
    print('river')

def turn_choice(choice, i):
    if choice == 'fold':
        fold(i)
    elif choice == 'check':
        check(i)
    elif choice == 'bet':
        bet(i)
    else:
        choice = input('kies fold, check of bet! ')
        turn_choice(choice, i)
    return choice

def fold(i):
    print(f'Speler{players[i].number} heeft gefold')
    players[i].hand = []
    print(f'De pot is {pot}')

def check(i):
    print(f'Speler{players[i].number} heeft gecheckt')
    print(f'De pot is {pot}')
    print(prev_bet)

def bet(i):
    global pot
    global prev_bet
    bet_amount = input(f'Speler{players[i].number} hoeveel wil je inzetten? De minimum raise is {prev_bet}! Als je toch wil folden of checken typ dan fold of check) ')
    if bet_amount == 'fold':
        fold(i)
    elif bet_amount == 'check':
        check(i)
    elif bet_amount.isdigit():
        bet_input = int(bet_amount)
        if bet_input < prev_bet:
            bet(i)
        else:
            print(f'Je gaat {bet_amount} inzetten')
        
            players[i].chips = players[i].chips - bet_input
            pot = pot + bet_input
            prev_bet = bet_input
            print(f'De pot is {pot}')
    else:
        print('je moet geld inzetten, checken of folden! Je kan alleen hele euros inzetten!')
        bet(i)



#creates the players
player_count = 5
players = [Player(i+1, buy_in) for i in range(player_count)]

deck = new_deck() #creates the deck
deal_cards() #gives 2 cards to each player

print(f'De small blind is €{small_blind}.')
print(f'De big blind is €{big_blind}.')
print(f'De buy-in is €{buy_in}.')
print('Inzet is in hele euros!')

turn_num = pre_flop()

if turn_num == 5:
    flop()

real_player_count = 5 #real_player_creation()
