Title:
Python-Pan-n-Tilt

Description:
The Python-Pan-n-Tilt camera/video application is made to control two servos linked to a raspberry pi with a 
camera feed.

What your application does,
Why you used the technologies you used,
Some of the challenges you faced and features you hope to implement in the future.

The Python-Pan-n-Tilt application is made to control two servos from an Adafruit PCA_9685 (I2C controlled) servo 
driver board attached to a raspberry pi(Because these are wiely avaliable) because this board does not require constant power to the servo instead 
only when the position is moved, making it more efficient. A usb camera is used for video feed for simplicity and 
the cost Vs the raspberry pi camera at the time of writing. Pygubu and it's extension Visvis has been to make the 
GUI development much easier
This application is currently made to be a desktop 
application controlled over remote desktop (VCC or RDP).
The initial version is made to run on laptop PC using the self facing camera, changing variable values which will
later be used to change servo positions.
Camera on/off needs fixing.
There is potential to add third servo to make this into a pan n tilt neft gun turret for a bit of fun.


How to Install and Run the Project:
Pull repo into a folder then call with python using


How to Use the Project:
Although this will initially run on laptop PC for testing purposes, it is inteneded to be run on a raspberry pi 
via remote desktop. Much more detailed plan for setup and running are to follow.


Include Credits:
Pygubu - https://github.com/alejandroautalan/pygubu
Pygubu, Visvis - https://github.com/almarklein/visvis
Pillow - https://pypi.org/project/Pillow/
Adafruit PCA_9685 - https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython



Add a License:


How to Contribute to the Project:
Add Later