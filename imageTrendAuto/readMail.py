import win32com
from win32com.client import constants
from win32com.client.gencache import EnsureDispatch as Dispatch
import time
from datetime import datetime, timedelta
import re
import schedule 
import threading

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


if __name__ == "__main__":
    main()


#############################################
# IF WE WANT IT TO RUN AT SCHEDULE SOLO TIMES
#############################################
# def run_continuously():
#     cease_continuous_run = threading.Event()
#     class ScheduleThread(threading.Thread):
#         @classmethod
#         def run(cls):
#             while not cease_continuous_run.is_set():
#                 schedule.run_pending()
#     continuous_thread = ScheduleThread()
#     continuous_thread.start()
#     return cease_continuous_run

# if __name__ == "__main__":
#     schedule.every().second.do(main)
#     stop_run_continuously = run_continuously()
#     #time.sleep(5)
#     #stop_run_continuously.set()
