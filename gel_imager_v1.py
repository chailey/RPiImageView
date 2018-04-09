import picamera
from time import sleep
import Tkinter
import time
from PIL import ImageTk, Image

def quit():
    camera.stop_preview()
    global tkTop
    tkTop.destroy()

def loadJpg(file):

    JpgWin = Tkinter.Toplevel(tkTop)
    JpgWin.title('New Window')
    JpgWin.geometry('400x300')

    image = Image.open(file)
    image = image.resize((400, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    panel = Tkinter.Label(JpgWin, image=img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    JpgWin.mainloop()

def capture():
    #set parameter
    camera.sharpness = scaleSharpness.get()
    camera.contrast = scaleContrast.get()
    camera.brightness = scaleBrightness.get()
    camera.saturation = scaleSaturation.get()
    camera.exposure_compensation = scaleExpCompensation.get()
    
    timeStamp = time.strftime("%Y%m%d-%H%M%S")
    jpgFile='/mnt/Public/'+'gel_'+timeStamp+'.jpg'
    camera.capture(jpgFile)
    loadJpg(jpgFile)


def updatePreview(value=None):
    camera.sharpness = scaleSharpness.get()
    camera.contrast = scaleContrast.get()
    camera.brightness = scaleBrightness.get()
    camera.saturation = scaleSaturation.get()
    camera.exposure_compensation = scaleExpCompensation.get()



camera = picamera.PiCamera()
camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))
time.sleep(2)

tkTop = Tkinter.Tk()
tkTop.wm_title("Raspberry Pi Camera - Brightness")
tkTop.geometry('800x500')

tkButtonQuit = Tkinter.Button(
    tkTop, text="Quit", command=quit)
tkButtonQuit.pack()

tkButtonCapture = Tkinter.Button(
    tkTop, text="Capture", command=capture)
tkButtonCapture.pack()

SCALE_WIDTH = 780;

scaleSharpness = Tkinter.Scale(
    tkTop,
    from_=-100, to=100,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="sharpness",command=updatePreview)
scaleSharpness.set(0)
scaleSharpness.pack(anchor=Tkinter.CENTER)

scaleContrast = Tkinter.Scale(
    tkTop,
    from_=-100, to=100,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="contrast",command=updatePreview)
scaleContrast.set(0)
scaleContrast.pack(anchor=Tkinter.CENTER)

scaleBrightness = Tkinter.Scale(
    tkTop,
    from_=0, to=100,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="brightness",command=updatePreview)
scaleBrightness.set(50)
scaleBrightness.pack(anchor=Tkinter.CENTER)

scaleSaturation = Tkinter.Scale(
    tkTop,
    from_=-100, to=100,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="saturation",command=updatePreview)
scaleSaturation.set(0)
scaleSaturation.pack(anchor=Tkinter.CENTER)

scaleExpCompensation = Tkinter.Scale(
    tkTop,
    from_=-25, to=25,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="exposure_compensation",command=updatePreview)
scaleExpCompensation.set(0)
scaleExpCompensation.pack(anchor=Tkinter.CENTER)

Tkinter.mainloop()

