import tkinter as tk
from tkinter import *

# Making a class for fun
class GUI(Tk):
    def __init__(self):
        # Class constructor
        super().__init__()
        self.mainFrame = Frame(self, bg="white") # Build off of our main frame so make it accessible to all
        self.mainFrame.pack(fill="both", expand=True)
    def TopBar(self):
        # Top frame and label of app
        self.topFrame = Frame(self.mainFrame, bg="#EDAF52")
        self.topLabel = Label(self.topFrame, text="HSA IT Self Service Tool", bg="#FD9800", fg="white", font="Sitara 35 bold")
        self.topLabel.pack(padx=30,pady=30)
        self.topFrame.pack(fill="x")
    def QuickBar(self):
        # Quick frame and options
        self.quickFrame = Frame(self.mainFrame, bg="#0A6B60")
        self.quickLabel = Label(self.quickFrame, text="Quick Menu", bg="#0A6B60", fg="white", font="Sitara 18")
        self.quickLabel.pack(padx=40,pady=40)
        self.quickFrame.pack(side = LEFT,fill="y")
        self.sat = Button(self.quickFrame, text="Submit a Ticket")
        # Create button image with text on it already and add it to this directory and simply just place
        # self.img = PhotoImage(file="C:/Users/esquivr/Desktop/Apps/hsaGUI/button.png")
        # self.sat.config(image=self.img)
        self.sat.pack()
    def TicketTitle(self):
        self.ticketFrame = Frame(self.mainFrame, bg="white")
        self.ticketLabel = Label(self.ticketFrame, text="Sumbit a Ticket",font= "Sitara 25 bold", bg="white")
        self.ticketLabel.pack(side = LEFT, padx=160)
        self.ticketFrame.pack(fill="x")
    def ActionCenter(self):
        self.actionFrame = Frame(self.mainFrame, bg="gray")#width=1400, height=800)
        self.actionGeneral = Label(self.actionFrame, text="General")
        self.actionGeneral.grid(row=0, column=0)
        self.actionFrame.pack(side=TOP ,fill="both", padx=160, expand=True, pady=10)


if __name__ == "__main__":
    Launch=GUI() # intiliaze the tk class
    Launch.state("zoomed")
    Launch.TopBar() # Load in top bar
    Launch.QuickBar() # Load in quick menu
    Launch.TicketTitle()
    Launch.ActionCenter()
    Launch.mainloop() # Run the program using tkinter func