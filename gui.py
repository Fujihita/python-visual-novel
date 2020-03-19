import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
from time   import sleep
from threading import Timer

root = tk.Tk() # start class constructor
root.title("Testbench")
canvas = tk.Canvas(root, width=1366, height=768, background="black")
canvas.pack()

class PlaysoundException(Exception):
    pass

class Audio:
    '''
    Exerpt and modified code from playsound module for Windows
    Support .mp3 and .wav files playbacks using only the native Python modules
    This module no longer supports blocking and instead supports multi-channel parallel playbacks
    Built-in loop option
    The playback can now be interrupted at any time with 1s delay while looping
    '''
    def load_sound(self, sound, loop = False):
        self.sound = sound
        self.loop = loop
        from random import random
        self.alias = 'playsound_' + str(random())

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
        if self.loop:
            sched = Timer(0.1, self.play_loop)
        else:
            sched = Timer(0.1, self.play_once)
        sched.start()

    def play_once(self):
        self.winCommand('open "' + self.sound + '" alias', self.alias)
        self.winCommand('set', self.alias, 'time format milliseconds')
        self.durationInMS = self.winCommand('status', self.alias, 'length')
        self.winCommand('play', self.alias, 'from 0 to', self.durationInMS.decode())

    def play_loop(self):
        from time import sleep
        self.play_once()
        counter = 0.0
        while self.loop: 
            if counter >= (float(self.durationInMS) / 1000.0):
                self.winCommand('play', self.alias, 'from 0 to', self.durationInMS.decode())
                counter = 0.0
            sleep(0.5)
            counter += 0.5
        self.stop_sound()
    
    def stop_sound(self):
        if self.loop:
            self.loop = False # set flag in Main thread
        else:
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
        canvas.create_image(
                            0, 0,
                            anchor = "nw", image = self.background)
        if self.char2_src is None:
            canvas.create_image(
                                0, 0,
                                anchor = "nw", image = self.sprite1)
        elif self.char1_first:
            canvas.create_image(
                                canvas.winfo_width(), 0,
                                anchor = "ne", image = self.sprite2)
            canvas.create_image(
                                0, 0,
                                anchor = "nw", image = self.sprite1)
        else:
            canvas.create_image(
                                0, 0,
                                anchor = "nw", image = self.sprite1)
            canvas.create_image(
                                canvas.winfo_width(), 0,
                                anchor = "ne", image = self.sprite2)
        name_box = self.create_rectangle(
                                        100, canvas.winfo_height() - 300,
                                        400, canvas.winfo_height() - 250,
                                        fill = "black", alpha = 0.8)
        dialogbox = self.create_rectangle(
                                        100, canvas.winfo_height() - 250,
                                        canvas.winfo_width() - 100, canvas.winfo_height() - 75,
                                        fill = "black", alpha = 0.5)      
        namebox_content = canvas.create_text(
                                        250, canvas.winfo_height() - 275,
                                        anchor = "center", fill = "white",
                                        font = "Arial 20 bold", text = self.name)
        dialogbox_content = canvas.create_text(
                                        150, canvas.winfo_height() - 225,
                                        anchor = "nw", fill = "white",
                                        font = "Arial 14 bold", text = self.dialog)
        root.update()
        root.update_idletasks()

scene = Scene()
bgm = Audio()
voice = Audio()

def next(_scene, _bgm, _voice = None):
    _scene.draw_scene()
    _bgm.play_sound()
    if _voice is not None:
        sleep(0.1)
        _voice.play_sound()
    sleep(10.0)
    _bgm.stop_sound()
    sleep(0.6)

scene.load_scene(
                "CASTLE-3",
                "Objective cleared!",
                "background.jpg",
                "character.png")
bgm.load_sound('bgm.mp3', loop=True)
next(scene, bgm)

scene.char1_first = False
scene.load_scene(
                "LANCET-2",
                "Is it?",
                "background.jpg",
                "character.png",
                "character2.png")
bgm.load_sound('7F.mp3', loop=True)
voice.load_sound('voice.mp3')
next(scene, bgm, voice)