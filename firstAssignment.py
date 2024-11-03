import tkinter as tk
# from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *
import random 

class Application():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1000x250+500+350')
        self.root.title("Number Guesser")
        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.pack(fill='none', expand='True')
        self.startingtext = "You have "+str(lives)+" guesses to find the number between 0-100"
        self.text = Label(self.mainFrame, text=self.startingtext, font=("Brass Mono",30))
        self.text.grid(row = 0, column = 0,sticky='NEWS')
        self.set_text_field = Entry(self.mainFrame,background='green')
        self.set_text_field.grid(row=1,column=0,pady=10,sticky='NWES')
        self.set_button = Button(self.mainFrame, text="Check", command=self.set_text)
        self.set_button.grid(row=2,column=0,pady=10,sticky='NWES')
        # self.entry.grid(row=0,column=2)
        self.root.mainloop()

    def set_text(self):
        try:
            newtext = int(self.set_text_field.get())
        except:
            return
        mytext=''
        # print(lives)
        global lives
        lives-=1
        if newtext > x and lives>0:
            mytext = 'Lower , Your lives: '+str(lives)
            self.text.config(text=mytext)
            
        elif newtext < x and lives>0:
            mytext = 'Higher , Your lives: '+str(lives)
            self.text.config(text=mytext)
        elif newtext == x and lives > 0:
            self.text.config(text='Correct')
            self.set_button.destroy()
            
        else:
            mytext = 'You lost '
            self.text.config(text=mytext)
            self.set_button.destroy()

        # self.text.config(text=newtext)
        # print(x)

lives=7
if __name__ == '__main__':
    x=random.randint(0,100)
    print(x)
    Application()