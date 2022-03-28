# encoding: utf8
from __future__ import unicode_literals
import sys
import os
import pygubu
import imageio
# import visvis as vv  # New
from PIL import Image, ImageTk
# Uncomment on pi
# from board import SCL, SDA
# import busio

try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

# Import the PCA9685 module.
# from adafruit_pca9685 import PCA9685
# This uses Adafruit motor library, note: good for continuous rotation servos
# from adafruit_motor import servo

# i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
# pca = PCA9685(i2c)
# pca.frequency = 50

# servo1 = servo.Servo(pca.channels[0], min_pulse=580, max_pulse=2480)
# servo2 = servo.Servo(pca.channels[1], min_pulse=580, max_pulse=2480)

# The pulse range is 1000 - 2000 by default.
# Re-add to work on the pi!!!!
# servo1 = servo.Servo(pca.channels[0])
# servo2 = servo.Servo(pca.channels[1])
# servo1.angle = 50
# servo2.angle = 50
# for i in range(180):
##    servo1.angle = i
##for i in range(180):
##    servo1.angle = 180 - i
##pca.deinit()#I think this stops the signal after the move to save power
#Adapt the bit above

# servo1.angle = i
# pca.deinit()


class Myapp:
    """A GUI for two servos and a webcam feed"""
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        fpath = os.path.join(os.path.dirname(__file__), "test3.ui")
        builder.add_from_file(fpath)
        mainwindow = builder.get_object('mainwindow', master)
        self.is_on = False

        builder.connect_callbacks(self)
        builder.import_variables(self, 'is_on')

    def on_Button_Show_clicked(self):
        """pressing the button to change between the puppy image
        and a self facing video feed"""
        puppy_image = 'C:\\Users\\gingu\\Desktop\\Gubu Saves\\CamPCVisvis\\asleep_puppy.jpg'
        # puppy_image = 'C:\\The\\Folder\\You\\Save\\code_to\\asleep_puppy.jpg'
        # puppy_image = 'User/The/Folder/You/Save/code_to_on_Linux/asleep_puppy.jpg'
        off_image = Image.open(puppy_image)
        off_image_update = off_image.resize((450, 350), Image.ANTIALIAS)
        # label = self.builder.get_object('labelPicture')
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

    # def entry_invalid(self):
    #     """to show if incorrect value entered"""
    #     messagebox.showinfo('Title', 'Invalid entry input')

    def on_scale1_changed(self, event):  # This matches the command for scale1
        """When the slider the scale1 value is updated to match"""
        label = self.builder.get_object('Label_Tilt_Scale')
        scale1 = self.builder.get_object('Scale_Tilt')  # 'scale1' = the ID in gubu
        label.configure(text=scale1.get())
        print(scale1.get())  # Show the value in the terminal
        # uses the variable from scale to update the servo position
        # servo1.angle = scale1.get()#Deselcted on PC
    
    def on_scale2_changed(self, event):  # This matches the command for scale2
        """When the slider the scale2 value is updated to match"""
        label = self.builder.get_object('Label_Pan_Scale')
        scale2 = self.builder.get_object('Scale_Pan')  # 'scale1' = the ID in gubu
        label.configure(text=scale2.get())
        print(scale2.get())  # Show the value in the terminal
        # uses the variable from scale to update the servo position
        # servo2.angle = scale2.get()#Deselcted on PC


if __name__ == '__main__':
    root = tk.Tk()
    app = Myapp(root)
    root.mainloop()