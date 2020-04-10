from lib.widget import Fullscreen, Printable, TextBox

class Wallpaper(Fullscreen):
    pass


class Effect (Fullscreen):
    
    def _handler(self):
        self._callback = self._idle

    def _idle(self):
        pass

    def _blinker(self):
        if self._display_art == '':
            self.show()
        else:
            self.hide()
        self._root.after(100, self._callback)

    def blink(self, src):
        self.set(src)
        self._callback = self._blinker
        self._blinker()
    
    def _shaker_right(self):
        self._root.move(self._widget, 50, 0)
        self._root.after(100, self._callback)
        self._callback = self._shaker_right
    
    def _shaker_left(self):
        self._root.move(self._widget, -50, 0)
        self._root.after(100, self._callback)
        self._callback = self._shaker_left

    def shake(self, src):
        self.set(src)
        self.show()
        self._callback = self._shaker_left
        self._shaker_right()

    def stop(self, src=None):
        self.hide()
        self._callback = self.hide
        

class NameBox(TextBox):
    def __init__(self, root):
        self._root = root
        self.images = []
        self._widget = self._create_rectangle(
                                        100, root.winfo_height() - 250,
                                        400, root.winfo_height() - 200,
                                        fill = "black", alpha = 0.8)
        self._content = root.create_text(
                                        250, root.winfo_height() - 225,
                                        anchor = "center", fill = "white",
                                        font = "Arial 20 bold")


class DialogBox(Printable):
    def __init__(self, root):
        self._root = root
        self.images = []
        self._widget = self._create_rectangle(
                                        100, root.winfo_height() - 200,
                                        root.winfo_width() - 100, root.winfo_height() - 25,
                                        fill = "black", alpha = 0.5)
        self._content = root.create_text(
                                        150, root.winfo_height() - 175,
                                        anchor = "nw", width = root.winfo_width() - 300, fill = "white",
                                        font = "Arial 14 bold")