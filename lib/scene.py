from PIL import Image, ImageTk, ImageEnhance
from tkinter import Canvas
from time   import sleep
from threading import Timer

class scene:
    def __init__(self, callback, _root):
        global canvas
        global root
        root = _root
        canvas = Canvas(root, width=1366, height=768, background="black")
        canvas.bind("<Button-1>", callback)
        canvas.pack()

    def draw(self, /, name, dialog, background_src, char1_src, char2_src = None, char2_first = False):
        self.char1_src = char1_src
        self.char2_src = char2_src
        self.background_src = background_src
        self.name = name
        self.dialog = dialog
        self.images = []
        self.char2_first = char2_first
        self.draw_scene()
    
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
        if self.char2_first:
            self.sprite1 = ImageEnhance.Brightness(self.sprite1).enhance(0.3)
        self.sprite1 = self.sprite1.resize((768,768),Image.ANTIALIAS)
        self.sprite1 = ImageTk.PhotoImage(self.sprite1)

        if self.char2_src is not None:
            self.sprite2 = Image.open(self.char2_src).convert("RGBA")
            if not self.char2_first:
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
        elif not self.char2_first:
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
                                        anchor = "nw", width = canvas.winfo_width() - 300, fill = "white",
                                        font = "Arial 14 bold", text = "")
        root.update()
        root.update_idletasks()
        for i in range(len(self.dialog) + 1): 
            canvas.itemconfigure(dialogbox_content, text = self.dialog[:i])
            root.update()
            root.update_idletasks()
            sleep(0.1)
