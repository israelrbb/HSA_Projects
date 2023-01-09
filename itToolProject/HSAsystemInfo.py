import tkinter as tk     # GUI help
from tkinter import *
#from tkinter import messagebox
import pyperclip      # Copying to clipboard
import socket         # Used to get IP 
import os             # Command prompt calling and clipping
from PIL import ImageTk, Image 
import sys
                                        
########################################
# Copy to text to clipboard
########################################
def onclick(text):
    pyperclip.copy(text)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def main():
    ########################################
    # Main frame
    ########################################
    window = tk.Tk() # Body to hold GUI 
    canvas = tk.Canvas(window, height=250, width=500, bg="#BFEFFF")                                       # Expand our GUI and give it a background color
    canvas.create_text(155, 30, text= "System Information", fill="Black", font=('Helvetica 15 bold'), anchor='w') # Title text within GUI
    canvas.create_text(180, 50, text= "(Click item to copy)", fill="Black", font=('Helvetica 9'), anchor='w') # Title text within GUI
    canvas.create_text(10, 225, text= "Santa Cruz County \nHealth Services Agency", fill="Black", font=('Helvetica 10 bold'), anchor='w') #lower level writing
    canvas.create_text(200, 200, text= "HSA IT Tools", fill="Black", font=('Helvetica 11 bold'), anchor='w') # lower level wrtiting
    canvas.create_line(5, 60, 500, 60)
    ### images###
    image = Image.open(resource_path("Santa_Cruz_County_Seal.png")).convert("RGBA")
    image = image.resize((45, 45), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(image)
    canvas.create_image(8, 8, image=tk_image, anchor="nw")
    #icon
    window.iconbitmap(resource_path("Santa_Cruz_County_Seal.ico"))
    
    window.title("HSA-IT My PC Info")
    window.resizable(False, False) # Block full screen mode for it can cause our UI to look funky
    canvas.pack()    # Load our canvas into gui
    
    fontvar1 = 'Helvetica 9 bold'
    fontvar2 = 'Helvetica 10 bold'

    ########################################
    # Top left box
    ########################################
    hostname_frame = tk.LabelFrame(window, text="System Hostname:", background="white",font=(fontvar1))# Creating a white frame inside canvas with label
    hostname_frame.place(relwidth=0.3, relheight=0.2, relx=0.15,rely=0.25)                # Defining size/centering and loading into canvas
    myhostname = socket.gethostname()                                                   # Get host name of PC
    button = tk.Button(hostname_frame, text=f"{myhostname}", font= (fontvar2), command=lambda: onclick(myhostname))   # Button to easliy copy text into clipboard
    button.pack()

    ######################
   
    ########################################
    # Bottom left box
    ########################################
    ip_frame = tk.LabelFrame(window, text="System IPv4:", background="white", font=(fontvar1))      # Creating a white frame inside canvas with label
    ip_frame.place(relwidth=0.3, relheight=0.2, relx=0.15,rely=0.50)               # Defining size/centering and loading into canvas
    myip = socket.gethostbyname(myhostname)                                       # Get IP address of PC
    button2 = tk.Button(ip_frame, text=f"{myip}", font =(fontvar2), command=lambda: onclick(myip))        # Button to easliy copy text into clipboard
    button2.pack()

    ########################################
    # Top right box
    ########################################
    serial_frame = tk.LabelFrame(window, text="Device Serial:", background="white",font=(fontvar1))     # Creating a white frame inside canvas with label
    serial_frame.place(relwidth=0.3, relheight=0.2, relx=0.55,rely=0.25)                          # Defining size/centering and loading into canvas
    myserial = os.popen("""wmic bios get SerialNumber """).read()                               # Make a call into command prompt
    myserial = myserial.partition(' ')[2]    
    myserial = myserial.strip()
    button3 = tk.Button(serial_frame, text= f"{myserial}", font= (fontvar2), command=lambda: onclick(myserial), anchor="e")  # Button to easliy copy text into clipboard
    button3.pack()
    

    ########################################
    # Bottom right box
    ########################################
    install_frame = tk.LabelFrame(window, text="OS Install Date:", background="white",font=(fontvar1))             # Creating a white frame inside canvas with label
    install_frame.place(relwidth=0.3, relheight=0.2, relx=0.55,rely=0.50)                           # Defining size/centering and loading into canvas
    myoginstall = os.popen("""systeminfo | find /i "original" """).read()                          # Get OS install
    myoginstall = myoginstall.partition("Date:")[2]
    myoginstall = myoginstall.split(",")                                      
    myoginstall = myoginstall[0].strip()                                                              # Deleteing white spaces or new lines
    button4 = tk.Button(install_frame, text=f"{myoginstall}", font=( fontvar2 ), command=lambda: onclick(myoginstall))             # Button to easliy copy text into clipboard
    button4.pack()


    ########################################
    # Run the script // OR on close
    ########################################
    # def on_closing():
    #     if messagebox.askokcancel("Quit", "Do you want to quit?"):
    #         window.destroy()
    # window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop() # Run our GUI
    return;

if __name__ == "__main__":
    main()
