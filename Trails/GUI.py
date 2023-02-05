import tkinter
import random
from PIL import Image, ImageTk

turn = 0

#To show that win opens tkinter
win = tkinter.Tk()
#Title
win.title("Rolling Dice")
#The resultion
win.geometry("350x280")
#Position of the window
win.eval("tk::PlaceWindow . centre")

dice_images = ["D1.png","D2.png","D3.png","D4.png","D5.png","D6.png"]

img = ImageTk.PhotoImage(Image.open(random.choice(dice_images)))

lbl_image = tkinter.Label(win, image = img)
lbl_image.image = img
lbl_image.pack(expand = True)

while turn <= 0:
    def roll_the_dice():
        pressed = False
        img = ImageTk.PhotoImage(Image.open(random.choice(dice_images)))
        lbl_image.configure(image = img)
        lbl_image.image = img
        print(turn)
        
    btn = tkinter.Button(win, text = "ROLL THE DICE", command = roll_the_dice)
    pressed = True
    btn.pack(expand = True)
    turn = turn + 1

roll_the_dice()



