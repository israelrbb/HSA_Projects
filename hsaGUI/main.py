import tkinter as tk
from tkinter import *

# Making a class for fun
class GUI(Tk):
    def __init__(self):
        # Class constructor
        super().__init__()
        self.mainFrame = Frame(self, bg="white") # Build off of our main frame so make it accessible to all
        self.mainFrame.pack(fill="both", expand=True)
        self.pathuiActivated = False
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
        self.sat.pack(fill="x", padx=5)
        self.pathp = Button(self.quickFrame,text="Path Printer", command= lambda: self.switchtoPathUI())
        self.pathp.pack(fill="x", padx=5,pady=20)
    def TicketUI(self):
        # Controls UI for Sumbit a Ticket
        self.ticketFrame = Frame(self.mainFrame, bg="white")
        self.ticketLabel = Label(self.ticketFrame, text="Sumbit a Ticket",font= "Sitara 25 bold", bg="white")
        self.ticketLabel.pack(side = LEFT, padx=160)
        self.ticketFrame.pack(fill="x")
    def PathUI(self):
        # Controls UI for Path Printer
        self.pathFrame = Frame(self.mainFrame, bg="white")
        self.pathLabel = Label(self.pathFrame, text="Path Printer",font= "Sitara 25 bold", bg="white")
        self.pathLabel.pack(side = LEFT, padx=160)
        self.pathFrame.pack(fill="x")
    def ActionCenterTicket(self):
        self.actionticketFrame = Frame(self.mainFrame, bg="gray")#width=1400, height=800)
        self.actionticketGeneral = Label(self.actionticketFrame, text="General")
        self.actionticketGeneral.grid(row=0, column=0)
        self.actionticketFrame.pack(side=TOP ,fill="both", padx=160, expand=True, pady=10)
    def ActionCenterPath(self):
        self.actionFrame = Frame(self.mainFrame, bg="gray")#width=1400, height=800)
        self.actionFrame.pack(side=TOP ,fill="both", padx=160, expand=True, pady=10)
    def switchtoPathUI(self):
        # Switching to path UI should hide other UI aspects
        if self.pathuiActivated == False: # switch gate to prevent overload
            self.ticketLabel.pack_forget()
            self.ticketFrame.pack_forget()
            self.actionticketFrame.pack_forget()
            self.actionticketGeneral.pack_forget()
            self.PathUI()
            self.ActionCenterPath()
            self.pathuiActivated = True



if __name__ == "__main__":
    Launch=GUI() # intiliaze the tk class
    Launch.state("zoomed")
    # Load in the default layer, user control flow is handled by the class itself
    Launch.TopBar() # Load in top bar
    Launch.QuickBar() # Load in quick menu
    Launch.TicketUI()
    Launch.ActionCenterTicket()
    Launch.mainloop() # Run the program using tkinter func