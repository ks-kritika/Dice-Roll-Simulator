#dice roll simulator

import tkinter          #used to create GUI
import random

root = tkinter.Tk()
root.geometry('700x600')    #set dimensions of tkinter window
root.title('DICE ROLL SIMULATOR')   #set name to tkinter window


#label is used to implement display boxes where you can place text or image
label = tkinter.Label(root, text='', font=('times new roman', 200))     #size and font of the dice

def roll_dice():
    #unicode cannot exist without a backslash
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']   #unicode characters of dice no. 1 to 6 rsp.
    # we are formatting the text this is why we write f' here
    label.configure(text=f'{random.choice(dice)}\n{random.choice(dice)}')
    label.pack()

button = tkinter.Button(root, text='Roll dice', foreground='green', command=roll_dice)  #used to add buttons
button.pack()
root.mainloop()         #tells python to run the tkinter event loop