import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import utils as ut

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
        self.title_img = Image.open("C:/Users/esquivr/Desktop/Apps/hsaGUI/images/title.png")#PhotoImage(file="C:/Users/esquivr/Desktop/Apps/hsaGUI/images/satButton.png")
        self.title_image = ImageTk.PhotoImage(self.title_img)
        self.topLabel = Label(self.topFrame, image=self.title_image, borderwidth=0, background="#EDAF52")#text="HSA IT Self Service Tool", bg="#FD9800", fg="white", font="Sitara 35 bold")
        self.topLabel.pack(padx=10,pady=10)
        self.topFrame.pack(fill="x")
    def QuickBar(self):
        # Quick frame and options
        self.quickFrame = Frame(self.mainFrame, bg="#0A6B60")
        self.quick_img = Image.open("C:/Users/esquivr/Desktop/Apps/hsaGUI/images/quickbarTitle.png")
        self.quick_image = ImageTk.PhotoImage(self.quick_img)
        self.quickLabel = Label(self.quickFrame, image= self.quick_image, borderwidth=0, background="#0A6B60")#text="Quick Menu", bg="#0A6B60", fg="white", font="Sitara 20")
        self.quickLabel.pack(fill="x", padx=5,pady=5)
        self.quickFrame.pack(side = LEFT,fill="y")

        self.sat = Button(self.quickFrame, text="Submit a Ticket", background="#0A6B60",borderwidth=0,command= lambda: self.switchtoTicketUI())
        # Create button image with text on it already and add it to this directory and simply just place
        self.img = Image.open("C:/Users/esquivr/Desktop/Apps/hsaGUI/images/satButton.png")#PhotoImage(file="C:/Users/esquivr/Desktop/Apps/hsaGUI/images/satButton.png")
        self.sat_image = ImageTk.PhotoImage(self.img)
        self.sat.config(image=self.sat_image)
        self.sat.pack(padx=5,pady=15)

        self.fileb = Button(self.quickFrame,text="File Backup", background="#0A6B60",borderwidth=0,command= lambda: self.switchtoFileUI())
        self.fb_img = Image.open("C:/Users/esquivr/Desktop/Apps/hsaGUI/images/fbButton.png")#PhotoImage(file="C:/Users/esquivr/Desktop/Apps/hsaGUI/images/satButton.png")
        self.fb_image = ImageTk.PhotoImage(self.fb_img)
        self.fileb.config(image=self.fb_image)
        self.fileb.pack(padx=5,pady=15)

        self.pathp = Button(self.quickFrame,text="Path Printer", background="#0A6B60",borderwidth=0, command= lambda: self.switchtoPathUI())
        self.pp_img = Image.open("C:/Users/esquivr/Desktop/Apps/hsaGUI/images/ppButton.png")#PhotoImage(file="C:/Users/esquivr/Desktop/Apps/hsaGUI/images/satButton.png")
        self.pathp_image = ImageTk.PhotoImage(self.pp_img)
        self.pathp.config(image=self.pathp_image)
        self.pathp.pack(padx=5,pady=15)

    
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
        self.actionticketFrameShadow = ut.Shadow(self.actionticketFrame, size=5)#, #offset_x=10, offset_y=10)
        self.ticketmenu = LabelFrame(self.actionticketFrame, background="white")
        #self.actionticketGeneral = Label(self.actionticketFrame, text="General")
        #self.actionticketGeneral.grid(row=0, column=0)
        #self.ticketcanvas = Canvas(self.ticketmenu)
        #self.ticketmenuscroll = Scrollbar(self.ticketmenu, orient="vertical", command=self.ticketcanvas.yview)

        self.name_frame = Frame(self.ticketmenu, highlightbackground="#0A6B60", highlightthickness=2)
        self.namelabel = Label(self.name_frame,text="Name:", font= "Sitara 12")
        self.name = Entry(self.name_frame,highlightbackground="black", highlightthickness=1)

        self.email_frame = Frame(self.ticketmenu, highlightbackground="#0A6B60", highlightthickness=2)
        self.emaillabel = Label(self.email_frame,text="Email:", font= "Sitara 12")
        self.email = Entry(self.email_frame,highlightbackground="black", highlightthickness=1)

        self.contactnumber_frame = Frame(self.ticketmenu, highlightbackground="#0A6B60", highlightthickness=2)
        self.contactnumberlabel = Label(self.contactnumber_frame,text="Contact Number:", font= "Sitara 12")
        self.contactnumber = Entry(self.contactnumber_frame,highlightbackground="black", highlightthickness=1)

        self.cc_frame = Frame(self.ticketmenu, highlightbackground="#0A6B60", highlightthickness=2)
        self.cclabel = Label(self.cc_frame,text="CC's:", font= "Sitara 12")
        self.cc = Entry(self.cc_frame,highlightbackground="black", highlightthickness=1)

        self.department_frame = Frame(self.ticketmenu, highlightbackground="#0A6B60", highlightthickness=2)
        self.departmentlabel = Label(self.department_frame,text="Department:", font= "Sitara 12")
        self.department = Entry(self.department_frame,highlightbackground="black", highlightthickness=1)

        self.location_frame = Frame(self.ticketmenu, highlightbackground="#0A6B60", highlightthickness=2)
        self.locationlabel = Label(self.location_frame,text="Location:", font= "Sitara 12")
        self.location = Entry(self.location_frame,highlightbackground="black", highlightthickness=1)

        self.description_frame = Frame(self.ticketmenu, highlightbackground="#0A6B60", highlightthickness=2)
        self.descriptionlabel = Label(self.description_frame,text="Description:", font= "Sitara 12")
        self.description = Text(self.description_frame,highlightbackground="black", highlightthickness=1)

        self.sumbit_ticket_button = Button(self.ticketmenu, text="Sumbit Ticket", command= lambda: self.switchtoSumbittedTicketUI())

        # Pack UI elements!
        self.actionticketFrame.pack(side=TOP ,fill="both", padx=160, pady=(5,30), expand=True)
        self.ticketmenu.pack(fill="both", padx=5, pady=5, expand=True)

        # Pack text boxes!
        self.name_frame.pack(fill="x", padx=2, pady=2, expand=True)
        self.namelabel.pack(side=LEFT, padx=35)
        self.name.pack(side=LEFT, expand=True, fill="x", padx=10, pady=10, ipady=5)
        self.email_frame.pack(fill="x", padx=2, pady=2, expand=True)
        self.emaillabel.pack(side=LEFT, padx=36.5)
        self.email.pack(side=LEFT, expand=True, fill="x", padx=10, pady=10, ipady=5)
        self.contactnumber_frame.pack(fill="x", padx=2, pady=2, expand=True)
        self.contactnumberlabel.pack(side=LEFT)
        self.contactnumber.pack(side=LEFT, expand=True, fill="x", padx=10, pady=10, ipady=5)
        self.cc_frame.pack(fill="x", padx=2, pady=2, expand=True)
        self.cclabel.pack(side=LEFT, padx=37)
        self.cc.pack(side=LEFT, expand=True, fill="x", padx=10, pady=10, ipady=5)
        self.department_frame.pack(fill="x", padx=2, pady=2, expand=True)
        self.departmentlabel.pack(side=LEFT, padx=14)
        self.department.pack(side=LEFT, expand=True, fill="x", padx=10, pady=10, ipady=5)
        self.location_frame.pack(fill="x", padx=2, pady=2, expand=True)
        self.locationlabel.pack(side=LEFT, padx=24)
        self.location.pack(side=LEFT, expand=True, fill="x", padx=10, pady=10, ipady=5)
        self.description_frame.pack(fill="x", padx=2, pady=2, expand=True)
        self.descriptionlabel.pack(side=LEFT, padx=14)
        self.description.pack(side=LEFT, expand=True, fill="x", padx=10, pady=10, ipady=10)
        self.sumbit_ticket_button.pack(side=BOTTOM)
        #self.ticketcanvas.pack(side=LEFT)
        #self.ticketmenuscroll.pack(side=RIGHT, fill="y")
    def ActionCenterPath(self):
        self.actionpathFrame = Frame(self.mainFrame, bg="gray")#width=1400, height=800)
        self.actionpathFrame.pack(side=TOP ,fill="both", padx=160, pady=(5,30), expand=True)
    def ActionCenterFile(self):
        self.actionfileFrame = Frame(self.mainFrame, bg="gray")#width=1400, height=800)
        self.actionfileFrame.pack(side=TOP ,fill="both", padx=160, pady=(5,30), expand=True)

    ###################################################################################################  
    # Functions to hide UI elements
    ###################################################################################################  
    def hideTicketUI(self):
        self.ticketLabel.pack_forget()
        self.ticketFrame.pack_forget()
        self.actionticketFrame.pack_forget()
        self.ticketmenu.pack_forget()
        #self.ticketcanvas.pack_forget()
        #self.ticketmenuscroll.pack_forget()
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
    def switchtoSumbittedTicketUI(self):
        #assure user ticket has been sumbitted
        print("in production")

###################################################################################################  
# Run the program
###################################################################################################  
if __name__ == "__main__":
    Launch=GUI() # intiliaze the tk class
    Launch.state("zoomed")
    Launch.title("HSA IT Self Service Tool")
    Launch.wm_iconbitmap("C:/Users/esquivr/Desktop/Apps/hsaGUI/images/Santa_Cruz_County_Seal.ico")
    # Load in the default layer, user control flow is handled by the class itself
    Launch.TopBar() # Load in top bar
    Launch.QuickBar() # Load in quick menu
    Launch.TicketUI() # This will be the default start page to load 
    Launch.ticketuiActivated = True # Since ticket UI is default make sure switch gate is set to true
    Launch.ActionCenterTicket()
    Launch.mainloop() # Run the program using tkinter func