import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk, Image


root = tk.Tk()
root.title('Images and Icons')
root.iconbitmap('icon.ico')
root.state('zoomed')

my_img = ImageTk.PhotoImage(Image.open('ERROR.webp'))
my_btn = Button(root, image=my_img)
my_btn.pack()

root.mainloop()