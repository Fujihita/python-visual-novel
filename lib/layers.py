from lib.character import Character
from lib.elements import Wallpaper, Effect, NameBox, DialogBox


class Background:
    def __init__(self, root):
        self.wallpaper = Wallpaper(root)
        self.effect = Effect(root)
        root.itemconfig(self.wallpaper._widget, tags="background")
        root.itemconfig(self.effect._widget, tags="background")

        self._root = root

    def to_bottom(self):
        for item in reversed(self._root.find_withtag("background")):
            self._root.tag_lower(item)


class Foreground:

    def __init__(self, root):
        self.character_center = Character(root, "center")
        self.character_left = Character(root, "left")
        self.character_right = Character(root, "right")
        root.itemconfig(self.character_center._widget, tags="foreground")
        root.itemconfig(self.character_left._widget, tags="foreground")
        root.itemconfig(self.character_right._widget, tags="foreground")
        self._root = root
        self._visibile_char_list = []
    
    def to_bottom(self):
        for item in reversed(self._root.find_withtag("foreground")):
            self._root.tag_lower(item)

    def set(self, char):
        '''
        Manage the addition of characters on the visible foreground layer.
        _visible_char_list manages which character is visible (both speaking and listening states)
        characters not on _visibile_char_list are set to be hidden.
        '''
        if char not in self._visibile_char_list:
            self._visibile_char_list.append(char)
        
        char_position_list = self._sync_visibility()
        char_position_list[self._visibile_char_list.index(char)].speaking()
        for i in range(len(self._visibile_char_list)):
            if self._visibile_char_list[i] != char:
                char_position_list[i].listening()
                pass

    def hide(self, char):
        if char in self._visibile_char_list:
            self._visibile_char_list.remove(char)
            self._sync_visibility()

    def clear(self):
        self._visibile_char_list = []
        self._sync_visibility()        

    def _sync_visibility(self):
        '''
        _char_list manages the position of characters on the GUI, it's synced to _visible_char_list
        upon append() or remove() operations of _visible_char_list
        The object order is based on the number of characters visible.
        '''
        _char_list_dict = {
                        0: [],
                        1: [self.character_center],
                        2: [self.character_left, self.character_right],
                        3: [self.character_left, self.character_right, self.character_center],
                        }

        show_list = _char_list_dict[len(self._visibile_char_list)]
        for i in range(len(show_list)):
            show_list[i].set(self._visibile_char_list[i])
        
        hide_list = _char_list_dict[3-len(self._visibile_char_list)]
        for i in range(len(hide_list)):
            hide_list[i].hide()

        return show_list



class Interface:

    def __init__(self, root):
        self.effect = Effect(root)
        self.name = NameBox(root)
        self.dialog = DialogBox(root)
        root.itemconfig(self.effect._widget, tags="interface")
        root.itemconfig(self.name._content, tags="interface")
        root.itemconfig(self.dialog._content, tags="interface")
        self._root = root

    def to_top(self):
        for item in self._root.find_withtag("interface"):
            self._root.tag_raise(item)


class Scene:

    def __init__(self,root):
        self.background = Background(root)
        self.foreground = Foreground(root)
        self.interface = Interface(root)
        self._root = root
        self._canvas_stack = self._root.find_withtag("all")

    def update(self):
        if self._canvas_stack != self._root.find_withtag("all"):
            self.foreground.to_bottom()
            self.background.to_bottom()
            self._canvas_stack = self._root.find_withtag("all")
        self._root.update()
