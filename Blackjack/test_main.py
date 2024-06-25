import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

from cards import *
from player import double, hit, stand, split, calculate_player_value, chips
from dealer import calculate_dealer_value

card_images = []  # prevents garbage collection

def add_card(frame, card_path):  # function to display card
    original_img = Image.open(card_path)
    scaled_img = original_img.resize((125, 182))  # original: 500x726
    img = ImageTk.PhotoImage(scaled_img)
    card_images.append(img)  # prevents garbage collection
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

# start of GUI
root = tk.Tk()
root.title('Blackjack')
root.iconbitmap('icon.ico')
root.state('zoomed')

# dealer frame
dealer_frame = tk.Frame(root)  # frame that the cards will be in
dealer_frame.pack(fill="both", expand="yes")
dealerstr = tk.Label(dealer_frame, text="dealer", height=1)
dealerstr.pack()

# player frame
player_frame = tk.Frame(root)  # frame that the cards will be in
player_frame.pack(fill="both", expand="yes")
playerstr = tk.Label(player_frame, text="player", height=1)
playerstr.pack()

# button frame
button_frame = tk.Frame(root)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)
button_frame.pack(fill="x")

# buttons
button_height = 3

doubleButton = tk.Button(button_frame, text='Double', font=('Arial', 18), height=button_height, bg="orange", fg="white")
doubleButton.grid(row=0, column=0, sticky=tk.W+tk.E)

hitButton = tk.Button(button_frame, text='Hit', font=('Arial', 18), height=button_height, bg="forest green", fg="white")
hitButton.grid(row=0, column=1, sticky=tk.W+tk.E)

standButton = tk.Button(button_frame, text='Stand', font=('Arial', 18), height=button_height, bg="firebrick", fg="white")
standButton.grid(row=0, column=2, sticky=tk.W+tk.E)

splitButton = tk.Button(button_frame, text='Split', font=('Arial', 18), height=button_height, bg="dodger blue", fg="white")
splitButton.grid(row=0, column=3, sticky=tk.W+tk.E)

# Add cards to frames
hidden_card = add_hidden_card(dealer_frame)  # Add hidden card
add_card(dealer_frame, "cards/ace_of_spades.png")  # Example card

add_card(player_frame, "cards/2_of_hearts.png")  # Example card
add_card(player_frame, "cards/3_of_diamonds.png")  # Example card

# Function to reveal the hidden card later in the game
def reveal_dealer_card():
    reveal_card(hidden_card, "cards/king_of_clubs.png")  # Example card

# For testing purposes, reveal the hidden card after 3 seconds
root.after(3000, reveal_dealer_card)

root.mainloop()
