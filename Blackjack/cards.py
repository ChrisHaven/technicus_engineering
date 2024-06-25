import random

suits = ['spades', 'hearts', 'clubs', 'diamonds']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']

def new_deck():
    deck = [(value, suit) for value in values for suit in suits]
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    hand = [deck.pop(), deck.pop()]
    return hand

def calculate_value(hand):
    value = 0
    aces = 0
    for card in hand:
        card_value = card[0]
        if card_value in ['jack', 'queen', 'king']:
            value += 10
        elif card_value == 'ace':
            aces += 1
            value += 11
        else:
            value += card_value
        
    while value > 21 and aces > 0:
        value -= 10
        ace_count -= 1

    return value, aces
