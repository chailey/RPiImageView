import picamera
from time import sleep
import Tkinter as tk
import time
from PIL import ImageTk, Image, ImageDraw, ImageFont, ImageOps

    
    
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


def captureNormal():
    timeStamp = time.strftime("%Y%m%d-%H%M%S")
    jpgFile = 'img_' + timeStamp + '-norm.jpg'
    camera.capture(jpgFile)

def captureNegative():
    timeStamp = time.strftime("%Y%m%d-%H%M%S")
    jpgFile = 'img_' + timeStamp + '-neg.jpg'
    camera.capture(jpgFile)
    im = Image.open(jpgFile)
    newIm = ImageOps.invert(im)
    newIm.save(jpgFile)
    



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Select Gel Size")
       label.pack(side="top", fill="both", expand=True)
       bt1 = tk.Radiobutton(self, text= "1")
       bt2 = tk.Radiobutton(self, text= "2")
       bt3 = tk.Radiobutton(self, text= "3")
       bt4 = tk.Radiobutton(self, text= "4")
       bt1.pack(side="top", fill="both", expand=True)
       bt2.pack(side="top", fill="both", expand=True)
       bt3.pack(side="top", fill="both", expand=True)
       bt4.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Select Gel Type")
       label.pack(side="top", fill="both", expand=True)
       bt1 = tk.Radiobutton(self, text= "Wide")
       bt2 = tk.Radiobutton(self, text= "Narrow")
       bt1.pack(side="top", fill="both", expand=True)
       bt2.pack(side="top", fill="both", expand=True)

class Page3(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Capture Gel")
        label.pack(side="top", fill="both", expand=True)
       
        camera = picamera.PiCamera()
        camera.start_preview(fullscreen=False, window = (100, 20, 640, 360))
        time.sleep(2)

        tkTop = tk.Tk()
        tkTop.wm_title("Raspberry Pi Camera")
        tkTop.geometry('800x500')
       
        tkChoice1 = tk.Radiobutton(tkTop, text = "Negative (default)", command= lambda: captureNegative(),
                               indicatoron = 0, padx = 20, variable=tk.IntVar(),
                                value=1).pack(anchor=tk.W)
        tkChoice2 = tk.Radiobutton(tkTop, text = "Normal", command= lambda: captureNormal(),
                               indicatoron = 0, padx = 20, variable=tk.IntVar(),
                                value=1).pack(anchor=tk.W)

class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Annotate Gel")
        label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self) 

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Page 4", command=p4.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left") 

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()