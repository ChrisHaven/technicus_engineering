from cards import *

hand = []
chips = None

def double():
    print('double')

def hit(deck, hand):
    new_hand = add_new_card(hand, deck)
    print('hit')
    return(new_hand)

def stand():
    print('stand')

def split():
    print('split')

def calculate_player_value(player_hand):
    player_value = calculate_value(player_hand)
    return player_value
