import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image

from cards import *

def blackjackGame():
    root = tk.Tk()
    root.title('Blackjack')
    root.iconbitmap('icon.ico')
    root.state('zoomed')

    #dealer frame
    dealer_frame = tk.Frame(root) ## frame that the cards will be in
    dealer_frame.pack(fill="both", expand="yes")
    dealerstr = tk.Label(dealer_frame, text="dealer", height=1)
    dealerstr.pack()

    #player frame
    player_frame = tk.Frame(root) ## frame that the cards will be in
    player_frame.pack(fill="both", expand="yes")
    playerstr = tk.Label(player_frame, text="player", height=1)
    playerstr.pack()

    #button frame
    button_frame = tk.Frame(root)
    for i in range(4):
        button_frame.columnconfigure(i, weight=1)
    button_frame.pack(fill="x")
    #buttons
    button_height = 3

    doubleButton = tk.Button(button_frame, text='Double', font=('Arial', 18), height=button_height, bg="orange", fg="white")
    doubleButton.grid(row=0, column=0, sticky=tk.W+tk.E)

    hitButton = tk.Button(button_frame, text='Hit', font=('Arial', 18), height=button_height, bg="forest green", fg="white")
    hitButton.grid(row=0, column=1, sticky=tk.W+tk.E)

    standButton = tk.Button(button_frame, text='Stand', font=('Arial', 18), height=button_height, bg="firebrick", fg="white")
    standButton.grid(row=0, column=2, sticky=tk.W+tk.E)

    splitButton = tk.Button(button_frame, text='Split', font=('Arial', 18), height=button_height, bg="dodger blue", fg="white")
    splitButton.grid(row=0, column=3, sticky=tk.W+tk.E)

    root.mainloop()

deck = new_deck()
hand = deal_cards(deck)
print(hand)

blackjackGame()