#!/usr/bin/python
import datetime
import cv2
import os
import pyautogui

# # Config
# stream_url = 'rtsp://admin:88888888@192.168.1.101:10544/tcp/av0_0'


# Determine save location
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H-%M-%S")
absolute_script_dir = os.path.dirname(os.path.realpath(__file__))
save_dir = absolute_script_dir + '/snapshots/' + date
save_path = save_dir + '/' + time + '.jpg'
# save_dir = absolute_script_dir + '/snapshots/'
# save_path = save_dir + '/' + 'last_picure' + '.jpg'

# # Capture frame from camera stream
# cap = cv2.VideoCapture(stream_url)
# ret, frame = cap.read()
myScreenshot = pyautogui.screenshot()



# Save frame as image
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

cv2.imwrite(save_path, myScreenshot)
