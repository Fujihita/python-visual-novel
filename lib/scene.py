from PIL import Image, ImageTk, ImageEnhance
from tkinter import Canvas
from time   import sleep

class scene:
    def __init__(self, callback, _root):
        global canvas
        global root
        root = _root
        canvas = Canvas(root, width=1366, height=768, background="black")
        canvas.bind("<Button-1>", callback)
        canvas.pack()
        self.printFlag = False
        self.images = []
        self.load_interface()

    def create_rectangle(self, x1, y1, x2, y2, **kwargs):
        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            fill = root.winfo_rgb(fill) + (alpha,)
            self.image = Image.new('RGBA', (x2-x1, y2-y1), fill)
            self.images.append(ImageTk.PhotoImage(self.image))
            canvas.create_image(x1, y1, image=self.images[-1], anchor='nw')
        canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

    def load_graphic(self, char1, char2, active):
        if char1 == '' and char2 == '':
            self.sprite1 = ''
            self.sprite2 = ''
            return
            
        if char1 != '':
            self.sprite1 = Image.open(char1).convert("RGBA")
            if active == "char2":
                self.sprite1 = ImageEnhance.Brightness(self.sprite1).enhance(0.3)
            self.sprite1 = self.sprite1.resize((768,768),Image.ANTIALIAS)
            self.sprite1 = ImageTk.PhotoImage(self.sprite1)
        else:
            self.sprite1 = ''

        if char2 != '':
            self.sprite2 = Image.open(char2).convert("RGBA")
            if active == "char1":
                self.sprite2 = ImageEnhance.Brightness(self.sprite2).enhance(0.3)
            self.sprite2 = self.sprite2.resize((768,768),Image.ANTIALIAS)
            self.sprite2 = ImageTk.PhotoImage(self.sprite2)
        else:
            self.sprite2 = ''

    def load_interface(self):
        self.background_content = canvas.create_image(
                            0, 0,
                            anchor = "nw")
        canvas.update()
        # Foreground layer
        self.effect_content = canvas.create_image(
                                        0, 0,
                                        anchor = "nw")
        self.char2 = canvas.create_image(
                                        canvas.winfo_width(), 0,
                                        anchor = "ne")
        self.char1 = canvas.create_image(
                                        0, 0,
                                        anchor = "nw")
        self.char2_top = canvas.create_image(
                                        canvas.winfo_width(), 0,
                                        anchor = "ne")
        self.effect_top_content = canvas.create_image(
                                        0, 0,
                                        anchor = "nw")
        # UX element layer
        self.name_box = self.create_rectangle(
                                        100, canvas.winfo_height() - 250,
                                        400, canvas.winfo_height() - 200,
                                        fill = "black", alpha = 0.8)
        self.dialogbox = self.create_rectangle(
                                        100, canvas.winfo_height() - 200,
                                        canvas.winfo_width() - 100, canvas.winfo_height() - 25,
                                        fill = "black", alpha = 0.5)
        self.namebox_content = canvas.create_text(
                                        250, canvas.winfo_height() - 225,
                                        anchor = "center", fill = "white",
                                        font = "Arial 20 bold")
        self.dialogbox_content = canvas.create_text(
                                        150, canvas.winfo_height() - 175,
                                        anchor = "nw", width = canvas.winfo_width() - 300, fill = "white",
                                        font = "Arial 14 bold")

    def effect(self, src, top=False):
        if src == "":
            canvas.itemconfigure(self.effect_content, image = src)
            canvas.itemconfigure(self.effect_top_content, image = src)
            return
        self.eff_img = Image.open(src).resize((1366,768),Image.ANTIALIAS)
        self.eff_img = ImageTk.PhotoImage(self.eff_img)
        if top:
            canvas.itemconfigure(self.effect_top_content, image = self.eff_img)
        else:
            canvas.itemconfigure(self.effect_content, image = self.eff_img)

    def background(self, src):
        self.bg_img = Image.open(src).resize((1366,768),Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        canvas.itemconfigure(self.background_content, image = self.bg_img)

    def foreground(self, /, char1='', char2='',*, active = ""):
        self.load_graphic(char1, char2, active)
        
        canvas.itemconfigure(self.char1, image = self.sprite1)
        if active == "char2":
            canvas.itemconfigure(self.char2, image = '')
            canvas.itemconfigure(self.char2_top, image = self.sprite2)
        else:
            canvas.itemconfigure(self.char2, image = self.sprite2)
            canvas.itemconfigure(self.char2_top, image = '')
    
    def dialog(self, /, name, dialog):
        canvas.itemconfigure(self.namebox_content, text = name)
        canvas.itemconfigure(self.dialogbox_content, text = '')
        canvas.update()
        self.buffer = dialog
        self.index = 0

    def update_dialog(self):
        if self.index < len(self.buffer) + 1:
            canvas.itemconfigure(self.dialogbox_content, text = self.buffer[:self.index])
            self.index += 1
            sleep(0.05)
        return self.index < len(self.buffer) + 1 # return a flag that indicates printing status

    def skip_dialog(self):
        canvas.itemconfigure(self.dialogbox_content, text = self.buffer)

        
        
