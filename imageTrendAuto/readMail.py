import win32com
from win32com.client import constants
from win32com.client.gencache import EnsureDispatch as Dispatch
import os 
from datetime import datetime, timedelta
import re

def main():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI") # Open up the outlook application and its properties
    inbox = outlook.GetDefaultFolder(6)                                            # Open up the inbox folder (6)
    messages = inbox.Items
    filesExplored = []
    for message in list(messages): # Go through the messages in our inbox
        string = message.subject  # Get the subject line of a email
        if re.search("Scheduled Report", string): # Search the subject line for a report
            if message.SenderEmailAddress == "noReply@imagetrend.com": # Check if flagged email is actually IMAGE TREND
                #try:
                for attachment in message.Attachments:
                    if attachment not in filesExplored:
                        filesExplored.append(attachment)
                        print(f"Email: {message.subject}")
                        print(f"File attachment: {attachment}")
                    else:
                        continue

    # message = messages.Getlast
    # body_content = message.body
    # print (body_content)

if __name__ == "__main__":
    main()