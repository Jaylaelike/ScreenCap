'''
Take Screenshot using python with just 3 lines of code.
Author: Ayushi Rawat
'''

# #Without GUI
# import pyautogui

# myScreenshot = pyautogui.screenshot()
# myScreenshot.save(r'')


#With GUI
import pyautogui
import datetime
import os
import schedule
import time

def myScreenshot():
    
    # Determine save location
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H-%M-%S")
    absolute_script_dir = os.path.dirname(os.path.realpath(__file__))
    save_dir = absolute_script_dir + '/snapshots/' + date
    save_path = save_dir + '/' + time + '.png'

    # Save frame as image
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(save_path)


schedule.every().day.at("10:30").do(myScreenshot)
schedule.every().day.at("12:30").do(myScreenshot)
schedule.every().day.at("16:30").do(myScreenshot)

while True:
  
    # Checks whether a scheduled task 
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
