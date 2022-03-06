from __future__ import unicode_literals
import sys
import os
import pygubu
import imageio
# import visvis as vv  # New
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
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        fpath = os.path.join(os.path.dirname(__file__), "test3.ui")
        builder.add_from_file(fpath)
        mainwindow = builder.get_object('mainwindow', master)
        builder.connect_callbacks(self)

###################

#This section will be for using on the pi
##    camera = picamera.PiCamera()
##
##    def CameraON():
##        camera.preview_fullscreen=False
##        #Need something here to place preview in
##        camera.preview_window=(90,100, 320, 240)
##        camera.resolution=(640,480)
##        camera.start_preview()
##        camera.sharpness = 10
##        camera.contrast = 30
##        camera.vflip=False
##        camera.hflip=False
##        camera.exposure_mode = 'auto'
##        
##    def CameraOFF():
##        camera.stop_preview()
##        
##    def EXIT():
##        root.destroy
##        camera.stop_preview()
##        camera.close()
##        quit()

#####################
        
    def on_Button_Show_clicked(self):
        """Pressing the buton activates and displays the laptops self facing
        camera"""
        label = self.builder.get_object('Label_Feed')
        # print("Got Label_Feed")
        video_name = '<video0>'  # <video1> will be back camera/usb port cam
        # print("got web cam")
        video = imageio.get_reader(video_name)
        # print("got vid from imageio")


        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            #print("image from array")
            label.config(image=frame_image)
            #print("label config (frame image)")
            label.update()
            #print("label Packed")
            # Needs a bool to turn this off and on!!

            
    def on_Button_Update_Tilt_clicked(self):
        """The upper and lower variables can be set, in case of using different
        servos with more/less rotation for fine tuning"""
        Enter_Tilt_High = (self.builder.tkvariables['TiltHighEntryVar'].get())
        Add_High = print(Enter_Tilt_High)
        
        Enter_Tilt_Low = (self.builder.tkvariables['TiltLowEntryVar'].get())
        Add_Tilt_Low = print(Enter_Tilt_Low)

        scale = self.builder.get_object('Scale_Tilt')
        scale.configure({'from':int(Enter_Tilt_High)})
        
        scale = self.builder.get_object('Scale_Tilt')
        scale.configure({'to':int(Enter_Tilt_Low)})

    def on_Button_Update_Pan_clicked(self):
        """The upper and lower variables can be set, in case of using different
        servos with more/less rotation for fine tuning"""
        Enter_High = (self.builder.tkvariables['PanHighEntryVar'].get())
        Add_High = print(Enter_High)
        
        Enter_Low = (self.builder.tkvariables['PanLowEntryVar'].get())
        Add_Low = print(Enter_Low)

        scale = self.builder.get_object('Scale_Pan')
        scale.configure({'from':int(Enter_Low)})
        
        scale = self.builder.get_object('Scale_Pan')
        scale.configure({'to':int(Enter_High)})

    def entry_invalid(self):
        messagebox.showinfo('Title', 'Invalid entry input')


    def on_scale1_changed(self, event):#This matches the command for scale1
        #in test3.ui Gets the scale's command
        label = self.builder.get_object('Label_Tilt_Scale')
        #Gets and builds the label by name
        scale1 = self.builder.get_object('Scale_Tilt')#'scale1' = the ID in gubu
        #of the scale in the UI file. Gets and builds the scale
        label.configure(text=scale1.get())
        #Uses the variable from the scale  and outputs it to the label
        print(scale1.get()) #New Test Worked
        #uses the variable from scale to update the servo position
        # servo1.angle = scale1.get()#Deselcted on PC

    
    def on_scale2_changed(self, event):#This matches the command for scale1
        #in test3.ui Gets the scale's command
        label = self.builder.get_object('Label_Pan_Scale')
        #Gets and builds the label by name
        scale2 = self.builder.get_object('Scale_Pan')#'scale1' = the ID in gubu
        #of the scale in the UI file. Gets and builds the scale
        label.configure(text=scale2.get())
        #Uses the variable from the scale  and outputs it to the label
        print(scale2.get()) #New Test Worked
        #uses the variable from scale to update the servo position
        # servo2.angle = scale2.get()#Deselcted on PC

    
if __name__ == '__main__':
    root = tk.Tk()
    app = Myapp(root)
    root.mainloop()
