import picamera
from time import sleep
import Tkinter
import time
from PIL import ImageTk, Image, ImageDraw, ImageFont
import PIL.ImageOps 

def quit():
    camera.stop_preview()
    global tkTop
    tkTop.destroy()

def loadJpg(file):

    JpgWin = Tkinter.Toplevel(tkTop)
    JpgWin.title('New Window')
    JpgWin.geometry('1280x720')

    image = Image.open(file)
    image = image.resize((1280, 720), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    panel = Tkinter.Label(JpgWin, image=img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    JpgWin.mainloop()

def capture(captureOption):
    #set parameter
    camera.sharpness = scaleSharpness.get()
    camera.contrast = scaleContrast.get()
    camera.brightness = scaleBrightness.get()
    camera.saturation = scaleSaturation.get()
    camera.exposure_compensation = scaleExpCompensation.get()
    

    if (captureOption == 1)
        timeStamp = time.strftime("%Y%m%d-%H%M%S")
        jpgFile='img_'+timeStamp+'-neg.jpg'
        camera.capture(jpgFile)
        inverted_image = PIL.ImageOps.invert(Image.open(jpgFile))
        


def updatePreview(value=None):
    camera.sharpness = scaleSharpness.get()
    camera.contrast = scaleContrast.get()
    camera.brightness = scaleBrightness.get()
    camera.saturation = scaleSaturation.get()
    camera.exposure_compensation = scaleExpCompensation.get()


# Start camera preview and wait 2 seconds for camera to adjust
camera = picamera.PiCamera()
camera.start_preview(fullscreen=False, window = (100, 20, 640, 360))
time.sleep(2)


tkTop = Tkinter.Tk()
tkTop.wm_title("Raspberry Pi Camera - Brightness")
tkTop.geometry('800x500')

tkButtonQuit = Tkinter.Button(
    tkTop, text="Quit", command=quit)
tkButtonQuit.pack()

tkButtonCapture = Tkinter.Button(
    tkTop, text="Capture", command=capture(1))
tkButtonCapture.pack()

tkChoice1 = Tkinter.Radiobutton(tkTop, text = "Negative (default)", command=capture(1),
                               indicatoron = 0, padx = 20, variable=Tkinter.IntVar(),
                                value=1).pack(anchor=Tkinter.W)
tkChoice2 = Tkinter.Radiobutton(tkTop, text = "Normal", command=capture(0), 
                               indicatoron = 0, padx = 20, variable=Tkinter.IntVar(),
                                value=1).pack(anchor=Tkinter.W)

Tkinter.mainloop()

