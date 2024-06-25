import random

suits = ['♠', '♡', '♣', '♢']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

def new_deck():
    deck = [(value, suit) for value in values for suit in suits]
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    hand = [deck.pop(), deck.pop()]
    return hand
