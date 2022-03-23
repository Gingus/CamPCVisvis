# encoding: utf8
from __future__ import unicode_literals
import sys
import os
import pygubu
import imageio
import visvis as vv  # New
# import picamera
# from time import sleep
from PIL import Image, ImageTk

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

        builder.connect_callbacks(self)
        builder.import_variables(self, 'is_on')

    def on_Button_Show_clicked(self):
        """pressing the button to change between the puppy image
        and a self facing video feed"""
        puppy_image = 'C:\\Users\\pminard\\Desktop\\Gubu\\CamPCVisvis\\Puppies.jpg'
        off_image = Image.open(puppy_image)
        off_image_update = off_image.resize((450, 350), Image.ANTIALIAS)
        # label = self.builder.get_object('labelPicture')
        label = self.builder.get_object('Label_Feed')
        self.is_on = not self.is_on
        if self.is_on:
            # label = self.builder.get_object('Label_Feed')
            video_name = '<video0>'
            video = imageio.get_reader(video_name)

            for image in video.iter_data():
                if(not self.is_on):
                    break
                """video feed for the label"""
                image_on = ImageTk.PhotoImage(Image.fromarray(image))
                # frame_image = ImageTk.PhotoImage(Image.fromarray(image))
                # print("image from array")
                # label.config(image=frame_image)
                label.config(image=image_on)
                # label.config(image=video)
                label.image = image_on
                # print("label config (image_on)")
                # self.is_on = False
                label.update()

        else:
            # stop the video feed
            # see note at bottom
            show_image_off = ImageTk.PhotoImage(off_image_update)
            label.configure(image=show_image_off)
            label.image = show_image_off
            # self.is_on = True
            print(self.is_on)
        label.update()
            
    def on_Button_Update_Tilt_clicked(self):
        """Used to update the tilt servos upper and lower limits"""
        Enter_Tilt_High = (self.builder.tkvariables['TiltHighEntryVar'].get())
        Add_High = print(Enter_Tilt_High)
        
        Enter_Tilt_Low = (self.builder.tkvariables['TiltLowEntryVar'].get())
        Add_Tilt_Low = print(Enter_Tilt_Low)

        scale = self.builder.get_object('Scale_Tilt')
        scale.configure({'from': int(Enter_Tilt_High)})
        
        scale = self.builder.get_object('Scale_Tilt')
        scale.configure({'to': int(Enter_Tilt_Low)})

    def on_Button_Update_Pan_clicked(self):
        """Used to update the Pan servos upper and lower limits"""
        Enter_High = (self.builder.tkvariables['PanHighEntryVar'].get())
        Add_High = print(Enter_High)
        
        Enter_Low = (self.builder.tkvariables['PanLowEntryVar'].get())
        Add_Low = print(Enter_Low)

        scale = self.builder.get_object('Scale_Pan')
        scale.configure({'from': int(Enter_High)})
        
        scale = self.builder.get_object('Scale_Pan')
        scale.configure({'to': int(Enter_Low)})

    def entry_invalid(self):
        """to show if incorrect value entered"""
        messagebox.showinfo('Title', 'Invalid entry input')

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

# Note: To set the slider variables try self.slider.set(100) OR
# self.slider.From_.set(100)/self.slider.To:.set(100) maybe

# root = tk.Tk()
#     my_label = tk.Label(root)
#     my_label.pack()
#     thread = threading.Thread(target=stream, args=(my_label,))
#     thread.daemon = 1
#     thread.start()
#     root.mainloop()

# Also see https://stackoverflow.com/questions/36635567/tkinter-inserting-video-into-window
