import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import os


import picamera
import numpy as np
import time 
from datetime import datetime


#storing motion in the x and y direction
#sum of absolute differences (SAD) compares similarity between pixel blocks (block-matching algorithm)
motion_dtype = np.dtype([
    ('x','i1'),
    ('y','i1'),
    ('sad','u2'),
    ])

#motion detection breaks the image into 16x16 pixel blocks
#the number of rows and columns set up by the motion detector will vary based on resolution 
class MyMotionDetector(object):
    def __init__(self, camera):
        width, height = camera.resolution
        self.cols = (width + 15) // 16
        self.cols += 1
        self.rows = (height + 15) // 16
        
    #takes motion in the x and y direction and calculates the magnitude of the vector using pythagorean theorem  
        
    def write(self, s):
        data = np.frombuffer(s, dtype=motion_dtype)
        data = data.reshape((self.rows, self.cols))
        data = np.sqrt(
            np.square(data['x'].astype(np.float)) +
            np.square(data['y'].astype(np.float))
            ).clip(0, 255).astype(np.uint8)
        
        
        #motion is detected if the camera picks up a certain number of vectors (size threshold) at a certain magnitude (speed threshold)
        #ex: motion 5 vectors of magnitude 30 is considered motion
        motionDetected = (data > 30).sum() > 5          
        
        if motionDetected == True:                       
            if time.time() - start > 1:
                
                #if more than 1 second has passed, print time stamp whenever motion is detected
                print('icu at:', datetime.now())
                
                #use configuration file to get directory name for photos
                config = open('/home/pi/Desktop/urmum.cfg', mode = 'r')
                config = config.readlines()
                
                #get last element in configuration file and remove it '/n'
                dir = config[-1][:-1]                     
                
                #continuously capture images with different filenames  and store in a folder
                for i, SecurityImages in enumerate(camera.capture_continuous(dir+'/Security footage {counter:03d}.jpg')):
                    
                    #Time stamp on the images
                    camera.annotate_background = picamera.Color('black')
                    camera.annotate_text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
                    print('Captured %s' % SecurityImages)
                    time.sleep(0.5)
                    if i == 4:       
                        break
                
                #send email using our other python script
                import sendEmail
                print('Security email has been sent')
                
                camera.stop_preview()
                camera.close()
                camera.stop_recording()
                
                
        #time stamp frames of motion
        return len(s)
      
    
#initial conditions of camera, use motion detection class
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 30
    start = time.time()
    camera.start_recording('/dev/null', format='h264', motion_output=MyMotionDetector(camera))  #starts recording but does not keep the video 
    camera.vflip = True
    camera.start_preview()
    
    while True:
        continue
    