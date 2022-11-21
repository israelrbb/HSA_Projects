import tkinter as tk
from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.mainFrame = Frame(self, bg="white")
        self.mainFrame.pack(fill="both", expand=True)
    def TopBar(self):
        self.topFrame = Frame(self.mainFrame, bg="#EDAF52")
        self.topLabel = Label(self.topFrame, text="HSA IT", bg="#FD9800", fg="white", font="Sitara 24 bold")
        self.topLabel.pack(padx=30,pady=30)
        self.topFrame.pack(fill="x")
    def QuickBar(self):
        self.quickFrame = Frame(self.mainFrame, bg="#0A6B60")
        self.quickLabel = Label(self.quickFrame, text="Quick Menu", bg="#0A6B60", fg="white", font="Sitara 16")
        self.quickLabel.pack(padx=40,pady=40)
        self.quickFrame.pack(side = LEFT,fill="y")



if __name__ == "__main__":
    Launch=GUI()
    Launch.TopBar()
    Launch.QuickBar()
    Launch.mainloop()