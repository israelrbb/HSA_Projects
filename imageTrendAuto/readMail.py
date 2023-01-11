import promptlib
from tkinter import Tk
from tkinter import filedialog
import win32com
from win32com.client import constants
from win32com.client.gencache import EnsureDispatch as Dispatch
import os
from datetime import datetime, timedelta
import re

def main():

    #########################################################
    # How far does the user want to go back into their emails
    #########################################################
    range_date_days = 0
    range_date_weeks = 0
    range_date = str(input("How far back should I look, in weeks or days? Type W for weeks or D for days: "))
    if range_date == "W" or range_date == "w":
        range_date_weeks = int(input("How many weeks? : "))
    elif range_date == "D" or range == "d":
        range_date_days = int(input("How many days? : "))
    else:
        range_date_days = 0
        range_date_weeks = 0

    #########################################################
    # Create a root to ask for directory for CSV files
    #########################################################
    root = Tk()
    root.withdraw()
    print("opening file dialog")
    path = filedialog.askdirectory(title='Select Folder to Place CSV Files') # shows dialog box and return the path
    
    if path == "":
        print("error user chose no path")
        return

    #########################################################
    # Information dump
    ######################################################### 
    print("Information dump!:")
    print(f"Path user chose is {path}")
    if range_date_days == 0:
        print(f"Range is in weeks and the number is {range_date_weeks}")
        target_date = range_date_weeks
    else:
        print(f"Range is in days and the number is {range_date_days}")
        target_date = range_date_days 
    todays_date = datetime.today()
    if range_date_days == 0:
        restricted_date = datetime.today() - timedelta(weeks=range_date_weeks)
    else:
        restricted_date = datetime.today() - timedelta(days=range_date_days)
    print(todays_date)
    print(restricted_date)
    return
    #########################################################
    # Open Outlook application and go through emails
    #########################################################
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI") # Open up the outlook application and its properties
    inbox = outlook.GetDefaultFolder(6)                                            # Open up the inbox folder (6)
    messages = inbox.Items                                                         # Set a var to environment
    messages.Sort("[ReceivedTime]", True)
    lastRangeMessages = messages.Restrict("[ReceivedTime] >= '" +restricted_date.strftime('%m/%d/%Y %H:%M %p')+"'")
    filesExplored = []                                                             # List of files we explored
    outputDir = path
    outOfRange = 0

    print("Opening Outlook")

    try:
        for message in lastRangeMessages: # Go through the messages in our inbox
            string = message.subject  # Get the subject line of a email
            if re.search("Scheduled Report", string): # Search the subject line for a report
                if message.SenderEmailAddress == "noReply@imagetrend.com": # Check if flagged email is actually IMAGE TREND
                    print("Found report")
                    try:
                        print(message.SentOn)
                        print(f"Email: {message.subject}")
                        for attachment in message.Attachments:
                            if attachment not in filesExplored:
                                # Record file already explored
                                filesExplored.append(attachment)
                                try:
                                    print(f"File attachment: {attachment}\n")
                                    print("Adding file to directory...\n")
                                    # Add attachment to our directory
                                    attachment.SaveAsFile(os.path.join(outputDir, attachment.FileName))
                                except Exception as error:
                                    print("error when saving the attachment:" + str(error))
                            else:
                                continue
                        else:
                            outOfRange+=1
                            if outOfRange > 10:
                                print(f"We are looking too far into the email inbox, I am going to exit us now \n")
                                break
                            continue
                    except Exception as error:
                        print("error when processing emails messages:" + str(error))
            message = messages.GetNext()
    except Exception as error:
        print("error when trying to open up emails" + str(error))

if __name__ == "__main__":
    main()

