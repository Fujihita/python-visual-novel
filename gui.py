import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
from time   import sleep

root = tk.Tk() # start class constructor
root.title("Testbench")
canvas = tk.Canvas(root, width=1366, height=768, background="black")
canvas.pack()

class PlaysoundException(Exception):
    pass

class Audio:
    '''
    Exerpt and modified code from playsound module for Windows
    Enable looping and allowing playbacks to be interrupted
    '''

    def load_sound(self, sound, block = False, loop = False):
        self.sound = sound
        self.block = block
        self.loop = loop

    def winCommand(self, *command):
        from ctypes import c_buffer, windll
        from sys    import getfilesystemencoding

        buf = c_buffer(255)
        command = ' '.join(command).encode(getfilesystemencoding())
        errorCode = int(windll.winmm.mciSendStringA(command, buf, 254, 0))
        if errorCode:
            errorBuffer = c_buffer(255)
            windll.winmm.mciGetErrorStringA(errorCode, errorBuffer, 254)
            exceptionMessage = ('\n    Error ' + str(errorCode) + ' for command:'
                                '\n        ' + command.decode() +
                                '\n    ' + errorBuffer.value.decode())
            raise PlaysoundException(exceptionMessage)
        return buf.value

    def play_sound(self):
        from threading import Timer
        from time   import sleep
        from random import random
        self.alias = 'playsound_' + str(random())
        
        self.winCommand('open "' + self.sound + '" alias', self.alias)
        self.winCommand('set', self.alias, 'time format milliseconds')
        durationInMS = self.winCommand('status', self.alias, 'length')
        self.winCommand('play', self.alias, 'from 0 to', durationInMS.decode())

        print("Playing sound")
        print(self.alias)

        if self.block:
            sleep(float(durationInMS) / 1000.0)
        if self.loop:
            self.sched = Timer(float(durationInMS) / 1000.0, self.play_sound)
            print("----New Thread---")
            self.sched.start()
    
    def stop_sound(self):
        print("Stopping sound")
        if self.loop:
            self.sched.cancel()
        print(self.alias)
        self.winCommand('close', self.alias)

class Scene:
    def load_scene(self, /, name, dialog, background_src, char1_src, char2_src=None):
        self.char1_src = char1_src
        self.char2_src = char2_src
        self.background_src = background_src
        self.name = name
        self.dialog = dialog
        self.images = []
        self.char1_first = True
    
    def create_rectangle(self, x1, y1, x2, y2, **kwargs):
        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            fill = root.winfo_rgb(fill) + (alpha,)
            self.image = Image.new('RGBA', (x2-x1, y2-y1), fill)
            self.images.append(ImageTk.PhotoImage(self.image))
            canvas.create_image(x1, y1, image=self.images[-1], anchor='nw')
        canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

    def load_graphic(self):
        self.sprite1 = Image.open(self.char1_src).convert("RGBA")
        if not (self.char1_first):
            self.sprite1 = ImageEnhance.Brightness(self.sprite1).enhance(0.3)
        self.sprite1 = self.sprite1.resize((768,768),Image.ANTIALIAS)
        self.sprite1 = ImageTk.PhotoImage(self.sprite1)

        if self.char2_src is not None:
            self.sprite2 = Image.open(self.char2_src).convert("RGBA")
            if self.char1_first:
                self.sprite2 = ImageEnhance.Brightness(self.sprite2).enhance(0.3)
            self.sprite2 = self.sprite2.resize((768,768),Image.ANTIALIAS)
            self.sprite2 = ImageTk.PhotoImage(self.sprite2)
            
        self.background = Image.open(self.background_src).resize((1366,768),Image.ANTIALIAS)
        self.background = ImageTk.PhotoImage(self.background)

    def draw_scene(self):
        self.load_graphic()
        canvas.update()
        canvas.create_image(0,0,anchor="nw",image=self.background)
        if self.char2_src is None:
            canvas.create_image(0,0,anchor="nw",image=self.sprite1)
        elif self.char1_first:
            canvas.create_image(canvas.winfo_width(),0,anchor="ne",image=self.sprite2)
            canvas.create_image(0,0,anchor="nw",image=self.sprite1)
        else:
            canvas.create_image(0,0,anchor="nw",image=self.sprite1)
            canvas.create_image(canvas.winfo_width(),0,anchor="ne",image=self.sprite2)
        name_box = self.create_rectangle(100,canvas.winfo_height()-300,400,canvas.winfo_height()-250,fill="black",alpha=0.8)
        dialogbox = self.create_rectangle(100,canvas.winfo_height()-250,canvas.winfo_width()-100,canvas.winfo_height()-75,fill="black",alpha=0.5)      
        namebox_content = canvas.create_text(250,canvas.winfo_height()-275,anchor="center",fill="white",font="Arial 20 bold",text=self.name)
        dialogbox_content = canvas.create_text(150,canvas.winfo_height()-225,anchor="nw",fill="white",font="Arial 14 bold",text=self.dialog)

scene = Scene()
bgm = Audio()
voice = Audio()

scene.load_scene("CASTLE-3", "Objective cleared!", "background.jpg", "character.png")
scene.draw_scene()
scene.load_scene("LANCET-2", "Is it?", "background.jpg", "character.png", "character2.png")
scene.char1_first = False
scene.draw_scene()

#bgm.load_sound('7F.mp3')
#bgm.play_sound()
bgm.load_sound('voice.mp3', loop=True)
bgm.play_sound()
#voice.load_sound('voice.mp3', loop=True)
#voice.play_sound()

sleep(8.0)
bgm.stop_sound()
#voice.stop_sound()

tk.mainloop()