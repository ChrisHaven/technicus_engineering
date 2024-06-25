from cards import *

chips = None

def double():
    print('double')

def hit():
    print('hit')

def stand():
    print('stand')

def split():
    print('split')

def calculate_player_value(player_hand):
    player_value = calculate_value(player_hand)
    return player_value
#if player_value[1] > 0:
#    print(f'playerval {player_value[0]}/{player_value[0]-10}')