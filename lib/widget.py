from PIL import Image, ImageTk, ImageEnhance

class Widget:

    def __init__(self):
        ''' Implement widget creation and root window binding in subclasses before use '''
        self._widget = ''
        self._root = ''

    def set(self, source):
        try:
            if self._src == source:
                return
        except AttributeError:
            pass
        self._src = source
        self._handler()

    def _handler(self): 
        ''' Implement set handler in subclasses before use '''
        pass


class Graphic(Widget):
    '''
    Base class for graphic elements
    Require _width and _height to be defined by the subclass.
    Extension for runtime resizing is possible
    '''

    def _load(self):
        self._file = Image.open(self._src).convert("RGBA")
        self._file = self._file.resize((self._width,self._height),Image.ANTIALIAS)
        self._default_art = ImageTk.PhotoImage(self._file)
        self._set_default()
 
    def _set_default(self):
        self._display_art = self._default_art
        self._update()

    def _update(self):     
        self._root.itemconfigure(self._widget, image = self._display_art)


class Hideable(Graphic):

    def hide(self):
        self._display_art = ''
        self._update()

    def show(self):
        self._set_default()


class Shadeable(Graphic):

    def _load(self):
        self._file = Image.open(self._src).convert("RGBA")
        self._file = self._file.resize((self._width,self._height),Image.ANTIALIAS)
        self._default_art = ImageTk.PhotoImage(self._file)
        try:
            del self._shaded_art
        except:
            pass
        self._set_default()

    def _shade(self):
        try:
            self._display_art = self._shaded_art
        except AttributeError:
            self._shaded_art = ImageTk.PhotoImage(ImageEnhance.Brightness(self._file).enhance(0.3))
            self._display_art = self._shaded_art
        self._update()

    def _unshade(self):
        self._set_default()


class Fadeable(Hideable): #to be implemented
    pass 


class Fullscreen(Fadeable):

    def __init__(self, root):
        self._width = 1366
        self._height = 768
        self._root = root
        self._widget = self._root.create_image(
                            0, 0,
                            anchor = "nw")
        self._handler = self._load


class TextBox:

    def __init__(self):
        ''' Implement widget creation and root window binding in subclasses before use '''
        self._widget = ''
        self._root = ''
        self.images = []
        self._content

    def _create_rectangle(self, x1, y1, x2, y2, **kwargs):
        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            fill = self._root.winfo_rgb(fill) + (alpha,)
            self.image = Image.new('RGBA', (x2-x1, y2-y1), fill)
            self.images.append(ImageTk.PhotoImage(self.image))
            self._root.create_image(x1, y1, image=self.images[-1], anchor='nw')
        self._root.create_rectangle(x1, y1, x2, y2, **kwargs)

    def set(self,text):
        self._text = text
        self._root.itemconfigure(self._content, text = text)
        self._handler()

    def _handler(self): 
        ''' Implement set handler in subclasses before use '''
        pass


class Printable(TextBox):
    
    def set(self,text):
        self._text = text
        self._root.itemconfigure(self._content, text = '')
        self._buffer = text
        self._index = 0
        self._printer()

    def _printer(self):
        if self._index <= len(self._buffer):
            self._root.itemconfigure(self._content, text = self._buffer[:self._index])
            self._index += 1
            self._root.after(50,self._printer)
    
    def skip(self):
        try:
            if self._index <= len(self._buffer):
                self._root.itemconfigure(self._content, text = self._buffer)
                self._index = len(self._buffer)
                return True
        except:
            pass
        return False
