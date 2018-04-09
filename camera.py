from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.framerate = 15
camera.brightness = 68
camera.contrast = 80
camera.sharpness = 75
camera.start_preview()
for i in range(10):
    sleep(5)
    #camera.capture("/home/pi/Desktop/GelImages/imageRuler%s.jpg" %i)
camera.stop_preview() 
