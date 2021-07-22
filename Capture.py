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
import tkinter as tk
import datetime
import os
import time
import tkinter.messagebox



root= tk.Tk()
root.title('โปรแกรมถ่ายภาพหหน้าจอ อัตโนมัติจ้า')


canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

# canvas2 = tk.Canvas(root, width = 300, height = 300)
# canvas2.pack()


def myScreenshot():
    
    tkinter.messagebox.showinfo("ไม่ต้องห่วงไฟล์จะถูกสร้างและเก็บตามวันเวลา",  "เดี๋ยวจัดให้!!!")
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


myButton = tk.Button(text='กดแรงๆที่ปุ่มนี้แล้วไปนอนจ้า' ,command=myScreenshot, bg='green',fg='white',font= 15)
canvas1.create_window(150, 150, window=myButton)



root.mainloop()


