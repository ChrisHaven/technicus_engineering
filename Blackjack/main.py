import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image

from cards import *
from player import double, hit, stand, split, calculate_player_value, chips
from dealer import calculate_dealer_value

card_images = [] #prevents garbage collection

def add_card(frame, card_path): #function to display card
    original_img = Image.open(card_path)
    scaled_img = original_img.resize((125,182)) #original: 500x726
    img = ImageTk.PhotoImage(scaled_img)
    card_images.append(img) #prevents garbage collection
    card = tk.Label(frame, image=img)
    card.pack(side="left", padx=5, pady=5)
    return card

def add_hidden_card(frame):  # function to display hidden card
    original_img = Image.open("cards/back.png")
    scaled_img = original_img.resize((125, 182))
    img = ImageTk.PhotoImage(scaled_img)
    card_images.append(img)
    card = tk.Label(frame, image=img)
    card.pack(side="left", padx=5, pady=5)
    return card

def reveal_card(card_label, card_path):  # function to reveal hidden card
    original_img = Image.open(card_path)
    scaled_img = original_img.resize((125, 182))
    img = ImageTk.PhotoImage(scaled_img)
    card_images.append(img)
    card_label.configure(image=img)
    card_label.image = img  # prevent garbage collection

#start of GUI
root = tk.Tk()
root.title('Blackjack')
root.iconbitmap('icon.ico')
root.state('zoomed')

#dealer frame
dealer_frame = tk.Frame(root) # frame that the cards will be in
dealer_frame.pack(fill="both", expand="yes")
dealerstr = tk.Label(dealer_frame, text="dealer", height=1)
dealerstr.pack()

#player frame
player_frame = tk.Frame(root) # frame that the cards will be in
player_frame.pack(fill="both", expand="yes")
playerstr = tk.Label(player_frame, text="speler", height=1)
playerstr.pack()

#button frame
button_frame = tk.Frame(root)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)
button_frame.pack(fill="x")

#buttons
button_height = 3

doubleButton = tk.Button(button_frame, text='Double', font=('Arial', 18), height=button_height, bg="orange", fg="white", command=double)
doubleButton.grid(row=0, column=0, sticky=tk.W+tk.E)

hitButton = tk.Button(button_frame, text='Hit', font=('Arial', 18), height=button_height, bg="forest green", fg="white", command=hit)
hitButton.grid(row=0, column=1, sticky=tk.W+tk.E)

standButton = tk.Button(button_frame, text='Stand', font=('Arial', 18), height=button_height, bg="firebrick", fg="white", command=stand)
standButton.grid(row=0, column=2, sticky=tk.W+tk.E)

splitButton = tk.Button(button_frame, text='Split', font=('Arial', 18), height=button_height, bg="dodger blue", fg="white", command=split)
splitButton.grid(row=0, column=3, sticky=tk.W+tk.E)

#creating deck and dealing cards
deck = new_deck()
dealer_hand = deal_cards(deck)
player_hand = deal_cards(deck)

hidden_card = add_hidden_card(dealer_frame)
#print(dealer_hand) #used for testing
add_card(dealer_frame, f"cards/{dealer_hand[0][0]}_of_{dealer_hand[0][1]}.png")
#add_hidden_card() #adds hidden card

#calculates dealers value and hows it (not used first round to prevent giving hidden card)
dealer_value = calculate_dealer_value(dealer_hand)
if dealer_value[1] > 0:
    dealer_display_value = f'{dealer_value[0]}/{dealer_value[0]-10}'
else:
    dealer_display_value = dealer_value[0]

dealer_val = tk.Label(dealer_frame, text=dealer_display_value, height=1, font=('arial', 14))
dealer_val.pack(side="left")

#print(player_hand) #used for testing
add_card(player_frame, f"cards/{player_hand[0][0]}_of_{player_hand[0][1]}.png")
add_card(player_frame, f"cards/{player_hand[1][0]}_of_{player_hand[1][1]}.png")

#calculates player value and prints it
player_value = calculate_player_value(player_hand)
if player_value[1] > 0:
    player_display_value = f'{player_value[0]}/{player_value[0]-10}'
else:
    player_display_value = player_value[0]

player_val = tk.Label(player_frame, text=player_display_value, height=1, font=('arial', 14))
player_val.pack(side="left")

def reveal_dealer_card():
    reveal_card(hidden_card, f"cards/{dealer_hand[1][0]}_of_{dealer_hand[1][1]}.png")

root.after(3000, reveal_dealer_card)

root.mainloop()
