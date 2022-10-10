# encoding: utf8
# Phil Minard
# Ujas Sidapara
# Sam Cork
from __future__ import unicode_literals
import sys
import os
import pygubu
import imageio
from PIL import Image, ImageTk
import smbus
import time
bus=smbus.SMBus(1)
time.sleep(1)
from adafruit_servokit import ServoKit
from time import sleep

try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))


class Myapp:
    """A GUI for two servos and a webcam feed"""
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        fpath = os.path.join(os.path.dirname(__file__), "test3.ui")
        builder.add_from_file(fpath)
        mainwindow = builder.get_object('mainwindow', master)
        self.is_on = False
        self.kit = ServoKit(channels=16)
        self.kit.servo[0].angle = 90
        self.kit.servo[1].angle = 90
        builder.connect_callbacks(self)
        builder.import_variables(self, 'is_on')

    def on_Button_Show_clicked(self):
        """pressing the button to change between the puppy image
        and a self facing video feed"""
        puppy_image = '/home/pi/Desktop/CamPCVisvis/asleep_puppy.jpg'
        off_image = Image.open(puppy_image)
#         off_image_update = off_image.resize((450, 350), Image.ANTIALIAS)
        off_image_update = off_image.resize((1280, 720), Image.ANTIALIAS)
        label = self.builder.get_object('Label_Feed')
        self.is_on = not self.is_on
        if self.is_on:
            print(self.is_on)
            video_name = '<video0>'
            video = imageio.get_reader(video_name)

            for image in video.iter_data():
                if not self.is_on:
                    break
                """video feed for the label"""
                image_on = ImageTk.PhotoImage(Image.fromarray(image))
                label.config(image=image_on)
                label.image = image_on
                label.update()

        else:
            show_image_off = ImageTk.PhotoImage(off_image_update)
            label.configure(image=show_image_off)
            label.image = show_image_off
            print(self.is_on)
        label.update()
            
    def on_Button_Update_Tilt_clicked(self):
        """Used to update the tilt servos upper and lower limits"""
        Enter_Tilt_High = (self.builder.tkvariables['TiltHighEntryVar'].get())
        Enter_Tilt_Low = (self.builder.tkvariables['TiltLowEntryVar'].get())

        scale = self.builder.get_object('Scale_Tilt')
        scale.configure({'from': int(Enter_Tilt_High)})
        
        scale = self.builder.get_object('Scale_Tilt')
        scale.configure({'to': int(Enter_Tilt_Low)})

    def on_Button_Update_Pan_clicked(self):
        """Used to update the Pan servos upper and lower limits"""
        Enter_High = (self.builder.tkvariables['PanLowEntryVar'].get())
        Enter_Low = (self.builder.tkvariables['PanHighEntryVar'].get())

        scale = self.builder.get_object('Scale_Pan')
        scale.configure({'from': int(Enter_High)})
        
        scale = self.builder.get_object('Scale_Pan')
        scale.configure({'to': int(Enter_Low)})

    def on_scale1_changed(self, event):  # This matches the command for scale1
        """When the slider the scale1 value is updated to match"""
        label = self.builder.get_object('Label_Tilt_Scale')
        scale1 = self.builder.get_object('Scale_Tilt')  # 'scale1' = the ID in gubu
        label.configure(text=scale1.get())
        print(scale1.get())  # Show the value in the terminal
        self.kit.servo[0].angle=int(scale1.get())

    def on_scale2_changed(self, event):  # This matches the command for scale2
        """When the slider the scale2 value is updated to match"""
        label = self.builder.get_object('Label_Pan_Scale')
        scale2 = self.builder.get_object('Scale_Pan')  # 'scale1' = the ID in gubu
        label.configure(text=scale2.get())
        print(scale2.get())  # Show the value in the terminal4
        self.kit.servo[1].angle=int(scale2.get())
        
    def quit(self):
        self.kit.servo[0].angle = 90
        self.kit.servo[1].angle = 90


if __name__ == '__main__':
    root = tk.Tk()
#     root.attributes("-fullscree",True)
    app = Myapp(root)
    root.mainloop()

