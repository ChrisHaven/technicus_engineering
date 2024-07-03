from cards import *

hand = []

chips = float(25)

hit_status = False # to make sure you cant split or double after hitting
split_status = False # to make sure you cant split twice
next_hand = False # to be able to go to the second hand after splitting

def double():
    print('double')

def hit(deck, hand):
    new_hand = add_new_card(hand, deck)
    print('hit')
    global hit_status #to prevent doubeling/splitting after hitting
    hit_status = True
    return new_hand

def stand():
    if split_status == True:
        next_hand == True
    hit_status = False
    print('stand')

def split(deck, hand):
    global split_status
    print(f'split: {split_status}, hit: {hit_status}') 
    val1 = hand[0][0]
    val2 = hand[1][0]
    
    hand1 = []
    hand2 = []

    if val1 == 'jack' or 'queen' or 'king':
        val1 == 10
    elif val1 == 'ace':
        val1 == 11

    if val2 == 'jack' or 'queen' or 'king':
        val2 == 10
    elif val2 == 'ace':
        val2 == 11

    if val1 == val2 and hit_status == False and split_status == False:
        split_status = True
        
        hand1.append(hand[0])
        hand1 = add_new_card(hand1, deck)
        # print(hand1)

        hand2.append(hand[1])
        hand2 = add_new_card(hand2, deck)
        # print(hand2)
    else:
        hand1 = 'error'
        hand2 = 'error'
    return hand1, hand2

def calculate_player_value(player_hand):
    player_value = calculate_value(player_hand)
    return player_value

def add_chips(add_val):
    global chips
    chips += add_val