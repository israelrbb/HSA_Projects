import tkinter as tk     # GUI help
from tkinter import *
from tkinter import messagebox
import pyperclip      # Copying to clipboard
import socket         # Used to get IP 
import os             # Command prompt calling and clipping

########################################
# Copy to text to clipboard
########################################
def onclick(text):
    pyperclip.copy(text)

def main():
    ########################################
    # Main frame
    ########################################
    window = tk.Tk() # Body to hold GUI 
    canvas = tk.Canvas(window, height=400, width=900, bg="#263D42")                                       # Expand our GUI and give it a background color
    canvas.create_text(350, 40, text= "    HSA IT", fill="white", font=('Helvetica 15 bold'), anchor='w') # Title text within GUI
    window.title("HSA IT")
    canvas.pack()    # Load our canvas into gui

    ########################################
    # Top left box
    ########################################
    hostname_frame = tk.LabelFrame(window, text="Your hostname is:", background="white")# Creating a white frame inside canvas with label
    hostname_frame.place(relwidth=0.3, relheight=0.2, relx=0.1,rely=0.2)                # Defining size/centering and loading into canvas
    myhostname = socket.gethostname()                                                   # Get host name of PC
    hostname_label = tk.Label(hostname_frame, text=f"{myhostname}", background="white") # Place host name within the text label
    hostname_label.pack()
    button = tk.Button(hostname_frame, text="Copy text", command=lambda: onclick(myhostname))   # Button to easliy copy text into clipboard
    button.pack()

    ########################################
    # Bottom left box
    ########################################
    ip_frame = tk.LabelFrame(window, text="Your IP is:", background="white")      # Creating a white frame inside canvas with label
    ip_frame.place(relwidth=0.3, relheight=0.2, relx=0.1,rely=0.45)               # Defining size/centering and loading into canvas
    myip = socket.gethostbyname(myhostname)                                       # Get IP address of PC
    ip_label = tk.Label(ip_frame, text=f"{myip}", background="white")             # Place ip within the text label
    ip_label.pack()
    button2 = tk.Button(ip_frame, text="Copy text", command=lambda: onclick(myip))        # Button to easliy copy text into clipboard
    button2.pack()

    ########################################
    # Top right box
    ########################################
    serial_frame = tk.LabelFrame(window, text="Your Serial Number is:", background="white")     # Creating a white frame inside canvas with label
    serial_frame.place(relwidth=0.3, relheight=0.2, relx=0.5,rely=0.2)                          # Defining size/centering and loading into canvas
    myserial = os.popen("""wmic bios get SerialNumber """).read()                               # Make a call into command prompt
    myserial = myserial.partition(' ')[2]    
    myserial = myserial.strip()
    serial_label = tk.Label(serial_frame, text=f"{myserial}", background="white")               # Place serial number within the text label
    serial_label.pack()
    button3 = tk.Button(serial_frame, text="Copy text", command=lambda: onclick(myserial), anchor="e")  # Button to easliy copy text into clipboard
    button3.pack()

    ########################################
    # Bottom right box
    ########################################
    install_frame = tk.LabelFrame(window, text="OS Install Date:", background="white")             # Creating a white frame inside canvas with label
    install_frame.place(relwidth=0.3, relheight=0.2, relx=0.5,rely=0.45)                           # Defining size/centering and loading into canvas
    myoginstall = os.popen("""systeminfo | find /i "original" """).read()                          # Get OS install
    myoginstall = myoginstall.partition("Date:")[2]                                                  
    myoginstall = myoginstall.strip()                                                              # Deleteing white spaces or new lines
    install_label = tk.Label(install_frame, text=f"{myoginstall}", background="white")             # Place OG OS Install date name within the text label
    install_label.pack()
    button4 = tk.Button(install_frame, text="Copy text", command=lambda: onclick(myoginstall))             # Button to easliy copy text into clipboard
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