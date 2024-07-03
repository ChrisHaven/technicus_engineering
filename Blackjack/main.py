import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image

from cards import *
import player
from player import double, stand, hit, split, calculate_player_value
import dealer
from dealer import calculate_dealer_value

import time

card_images = [] # prevents garbage collection
player_cards_icons = [] # to be able to remove cards when splitting

# commands
def hit_command(hand):
    global player_hand
    global player_value

    player_hand = player.hit(deck, hand)

    #calculates player value and prints it
    player_value = player.calculate_player_value(player_hand)
    if player_value[1] > 0:
        player_display_value = f'{player_value[0]}/{player_value[0]-10}'
    else:
        player_display_value = player_value[0]

    player_val.config(text=player_display_value)

    add_card(player_frame, f'cards/{player_hand[len(player_hand)-1][0]}_of_{player_hand[len(player_hand)-1][1]}.png')

    # print(player_hand)
    # print(player_display_value)
    # print(f'cards/{player_hand[len(player_hand)-1][0]}_of_{player_hand[len(player_hand)-1][1]}')
    # print(len(player_hand))

def split_command(hand):
    hands = player.split(deck, hand)

    hand1 = hands[0]
    hand2 = hands[1]

    value1 = player.calculate_player_value(hand1)
    value2 = player.calculate_player_value(hand2)

    if value1[1] > 0:
        display_value1 = f'{value1[0]}/{value1[0] - 10}'
    else:
        display_value1 = value1[0]

    if value1[1] > 0:
        display_value2 = f'{value2[0]}/{value2[0] - 10}'
    else:
        display_value2 = value2[0]

    player_val.config(text=display_value1)
    player_val_double = tk.Label(player_frame_double, text=display_value2, height=1, font=('arial', 14))
    player_val_double.pack()

    if hands[0] == 'error':
        messagebox.showinfo(title='error', message='je mag alleen splitten als beide waardes gelijk zijn en als er nog niet is gehit of gesplit!')
    else:
        print(f'hand1: {hand1}, hand2: {hand2}')

        for card in player_cards_icons:
            card.destroy()
        player_cards_icons.clear()
        
        player_frame_double.pack(fill="both", expand="yes", before=button_frame)
        add_card(player_frame, f'cards/{hand1[0][0]}_of_{hand1[0][1]}.png')
        add_card(player_frame, f'cards/{hand1[1][0]}_of_{hand1[1][1]}.png')
        add_card(player_frame_double, f'cards/{hand2[0][0]}_of_{hand2[0][1]}.png')
        add_card(player_frame_double, f'cards/{hand2[1][0]}_of_{hand2[1][1]}.png')

def add_card(frame, card_path): # function to display card
    original_img = Image.open(card_path)
    scaled_img = original_img.resize((100,145)) # original: 500x726
    img = ImageTk.PhotoImage(scaled_img)
    card_images.append(img) # prevents garbage collection
    card = tk.Label(frame, image=img)
    card.pack(side="left", padx=5, pady=5)
    return card

def add_hidden_card(frame):  # function to display hidden card
    original_img = Image.open("cards/back.png")
    scaled_img = original_img.resize((100,145))
    img = ImageTk.PhotoImage(scaled_img)
    card_images.append(img)
    card = tk.Label(frame, image=img)
    card.pack(side="left", padx=5, pady=5)
    return card

def reveal_card(card_label, card_path):  # function to reveal hidden card
    original_img = Image.open(card_path)
    scaled_img = original_img.resize((100,145))
    img = ImageTk.PhotoImage(scaled_img)
    card_images.append(img)
    card_label.configure(image=img)
    card_label.image = img  # prevent garbage collection

def add_chip_button():
    add = chip_entry.get()
    if add.isdigit():
        add = float(add)
        player.add_chips(add)
        chip_display.config(text=f"chips: {player.chips}")
        # print(f'digit {add}')
    else:
        # print('not digit')
        messagebox.showinfo(title="ongeldig getal", message="Vul een geldig getal in! Geen comma getallen of letters!")

#start of GUI
root = tk.Tk()
root.title('Blackjack')
root.iconbitmap('icon.ico')
root.state('zoomed')

# dealer frame
dealer_frame = tk.Frame(root) # frame that the cards will be in
dealer_frame.pack(fill="both", expand="yes")
dealerstr = tk.Label(dealer_frame, text="dealer", height=1)
dealerstr.pack()

# player frame
player_frame = tk.Frame(root) # frame that the cards will be in
player_frame.pack(fill="both", expand="yes")
playerstr = tk.Label(player_frame, text="speler", height=1)
playerstr.pack()

# player frame double
player_frame_double = tk.Frame(root) # frame that the cards will be in
# player_frame_double.pack(fill="both", expand="yes")

# chip entry
chip_entry = tk.Entry(player_frame)
chip_entry.pack()
chip_entry_botton = tk.Button(player_frame, text="deposit chips", font= ("Arial", 11), height=1, command=add_chip_button)
chip_entry_botton.pack()

# chip amount
chip_display = tk.Label(player_frame, text=f"chips: {player.chips}", font=("Arial", 14))
chip_display.pack()

# button frame
button_frame = tk.Frame(root)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)
button_frame.pack(fill="x")

# buttons
button_height = 3

doubleButton = tk.Button(button_frame, text='Double', font=('Arial', 18), height=button_height, bg="orange", fg="white", command=double)
doubleButton.grid(row=0, column=0, sticky=tk.W+tk.E)

hitButton = tk.Button(button_frame, text='Hit', font=('Arial', 18), height=button_height, bg="forest green", fg="white", command=lambda: hit_command(player_hand))
hitButton.grid(row=0, column=1, sticky=tk.W+tk.E)

standButton = tk.Button(button_frame, text='Stand', font=('Arial', 18), height=button_height, bg="firebrick", fg="white", command=stand)
standButton.grid(row=0, column=2, sticky=tk.W+tk.E)

splitButton = tk.Button(button_frame, text='Split', font=('Arial', 18), height=button_height, bg="dodger blue", fg="white", command=lambda: split_command(player_hand))
splitButton.grid(row=0, column=3, sticky=tk.W+tk.E)

# creating deck and dealing cards
deck = new_deck()
dealer_hand = deal_cards(deck)
# player_hand = deal_cards(deck)
val1 = 10
val2 = val1
player_hand = [(val1, 'spades'), (val2, 'spades')]
player.hand = player_hand



# calculates dealers value and hows it (not used first round to prevent giving hidden card)
dealer_value = calculate_dealer_value(dealer_hand)
if dealer_value[1] > 0:
    dealer_display_value = f'{dealer_value[0]}/{dealer_value[0]-10}'
else:
    dealer_display_value = dealer_value[0]

dealer_val = tk.Label(dealer_frame, text=dealer_display_value, height=1, font=('Arial', 14))
dealer_val.pack()

hidden_card = add_hidden_card(dealer_frame)
# print(dealer_hand) #used for testing
add_card(dealer_frame, f"cards/{dealer_hand[0][0]}_of_{dealer_hand[0][1]}.png")
# add_hidden_card() #adds hidden card

# calculates player value and prints it
player_value = calculate_player_value(player_hand)
if player_value[1] > 0:
    player_display_value = f'{player_value[0]}/{player_value[0]-10}'
else:
    player_display_value = player_value[0]

player_val = tk.Label(player_frame, text=player_display_value, height=1, font=('arial', 14))
player_val.pack()

# print(player_hand) #used for testing
player_cards_icons.append(add_card(player_frame, f"cards/{player_hand[0][0]}_of_{player_hand[0][1]}.png"))
player_cards_icons.append(add_card(player_frame, f"cards/{player_hand[1][0]}_of_{player_hand[1][1]}.png"))



def reveal_dealer_card():
    reveal_card(hidden_card, f"cards/{dealer_hand[1][0]}_of_{dealer_hand[1][1]}.png")

root.after(3000, reveal_dealer_card)

root.mainloop()