import tkinter as tk
from tkinter import *
from tkinter import ttk

# Class for better structure and future reorganization ease
class GUI(Tk):
    def __init__(self):
        # Class constructor
        super().__init__()
        self.mainFrame = Frame(self, bg="white") # Build off of our main frame so make it accessible to all
        self.mainFrame.pack(fill="both", expand=True)
        # Switch gate variables
        self.pathuiActivated = False
        self.ticketuiActivated = False
        self.fileuiActivated = False
    ###################################################################################################    
    # Functions to load in static elements that should never change because they comprise base look
    ###################################################################################################  
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
        self.sat = Button(self.quickFrame, text="Submit a Ticket", command= lambda: self.switchtoTicketUI())
        # Create button image with text on it already and add it to this directory and simply just place
        # self.img = PhotoImage(file="C:/Users/esquivr/Desktop/Apps/hsaGUI/button.png")
        # self.sat.config(image=self.img)
        self.sat.pack(fill="x", padx=5,pady=10)
        self.pathp = Button(self.quickFrame,text="Path Printer", command= lambda: self.switchtoPathUI())
        self.pathp.pack(fill="x", padx=5,pady=10)
        self.fileb = Button(self.quickFrame,text="File Backup", command= lambda: self.switchtoFileUI())
        self.fileb.pack(fill="x", padx=5,pady=10)
    
    ###################################################################################################  
    # Base UI for now it is just titles, SHOULD BE CHANGED SOON
    ###################################################################################################  
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
    def FileUI(self):
        # Controls UI for File Backup
        self.fileFrame = Frame(self.mainFrame, bg="white")
        self.fileLabel = Label(self.fileFrame, text="File Backup",font= "Sitara 25 bold", bg="white")
        self.fileLabel.pack(side = LEFT, padx=160)
        self.fileFrame.pack(fill="x")

    ###################################################################################################  
    # Our Action Centers
    ###################################################################################################  
    def ActionCenterTicket(self):
        # Set elements!
        self.actionticketFrame = Frame(self.mainFrame, bg="black")#width=1400, height=800)
        #self.actionticketGeneral = Label(self.actionticketFrame, text="General")
        #self.actionticketGeneral.grid(row=0, column=0)
        self.ticketmenu = LabelFrame(self.actionticketFrame)
        self.ticketcanvas = Canvas(self.ticketmenu)
        self.ticketmenuscroll = Scrollbar(self.ticketmenu, orient="vertical", command=self.ticketcanvas.yview)
        # Pack UI elements!
        self.actionticketFrame.pack(side=TOP ,fill="both", padx=160, expand=True, pady=10)
        self.ticketmenu.pack(fill="both", padx=5, pady=5, expand=True)
        self.ticketcanvas.pack(side=LEFT)
        self.ticketmenuscroll.pack(side=RIGHT, fill="y")
    def ActionCenterPath(self):
        self.actionpathFrame = Frame(self.mainFrame, bg="gray")#width=1400, height=800)
        self.actionpathFrame.pack(side=TOP ,fill="both", padx=160, expand=True, pady=10)
    def ActionCenterFile(self):
        self.actionfileFrame = Frame(self.mainFrame, bg="gray")#width=1400, height=800)
        self.actionfileFrame.pack(side=TOP ,fill="both", padx=160, expand=True, pady=10)

    ###################################################################################################  
    # Functions to hide UI elements
    ###################################################################################################  
    def hideTicketUI(self):
        self.ticketLabel.pack_forget()
        self.ticketFrame.pack_forget()
        self.actionticketFrame.pack_forget()
        self.ticketmenu.pack_forget()
        self.ticketcanvas.pack_forget()
        self.ticketmenuscroll.pack_forget()
    def hidePathUI(self):
        self.pathLabel.pack_forget()
        self.pathFrame.pack_forget()
        self.actionpathFrame.pack_forget()
    def hideFileUI(self):
        self.fileLabel.pack_forget()
        self.fileFrame.pack_forget()
        self.actionfileFrame.pack_forget()

    ###################################################################################################  
    # Functions to control the switch of Action Centers accordingly
    ###################################################################################################  
    def switchtoPathUI(self):
        # Switching to path UI should hide other UI aspects
        if self.pathuiActivated == False: # switch gate to prevent overload
            if self.ticketuiActivated == True:
                self.hideTicketUI()
            else:
                self.hideFileUI()
            self.PathUI()
            self.ActionCenterPath()
            self.pathuiActivated = True
            self.ticketuiActivated = False
            self.fileuiActivated = False
    def switchtoTicketUI(self):
        if self.ticketuiActivated == False:
            if self.pathuiActivated == True:
                self.hidePathUI()
            else:
                self.hideFileUI()
            self.TicketUI()
            self.ActionCenterTicket()
            self.ticketuiActivated = True
            self.pathuiActivated = False
            self.fileuiActivated = False
    def switchtoFileUI(self):
        if self.fileuiActivated == False:
            if self.ticketuiActivated == True:
                self.hideTicketUI()
            else:
                self.hidePathUI()
            self.FileUI()
            self.ActionCenterFile()
            self.fileuiActivated = True
            self.ticketuiActivated = False
            self.pathuiActivated = False

###################################################################################################  
# Run the program
###################################################################################################  
if __name__ == "__main__":
    Launch=GUI() # intiliaze the tk class
    Launch.state("zoomed")
    Launch.title("HSA IT Self Service Tool")
    Launch.wm_iconbitmap("C:/Users/esquivr/Desktop/Apps/hsaGUI/Santa_Cruz_County_Seal.ico")
    # Load in the default layer, user control flow is handled by the class itself
    Launch.TopBar() # Load in top bar
    Launch.QuickBar() # Load in quick menu
    Launch.TicketUI()
    Launch.ticketuiActivated = True # Since ticket UI is default make sure switch gate is set to true
    Launch.ActionCenterTicket()
    Launch.mainloop() # Run the program using tkinter func