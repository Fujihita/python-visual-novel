from lib.widget import Fadeable, Shadeable

class Character(Fadeable, Shadeable):

    def __init__(self, root, position):
        self._width = 768
        self._height = 768
        self._handler = self._load
        self._root = root
        self._widget = self._root.create_image(
                            self._root.winfo_width()/5, 0,
                            anchor = "nw")
        if position == "left":
            self._move_left()
        elif  position == "right":
            self._move_right()

    def _move_left(self):
        self._root.move(self._widget, -self._root.winfo_width()/5, 0)

    def _move_right(self):
        self._root.move(self._widget, self._root.winfo_width()/5, 0)

    def speaking(self):
        self._unshade()
        self._root.tag_raise(self._widget)

    def listening(self):
        self._shade()
        self._root.tag_lower(self._widget)