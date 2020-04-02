from lib.scene import Scene
from tkinter import Tk, Canvas
from time import sleep

root = Tk()
root.title("Hello, Python")
root.wm_state('zoomed')

canvas = Canvas(root, width=1366, height=768, background="black")
canvas.pack()
root.update()

scene = Scene(canvas)

scene.background.set("background\\background-2.jpg")
scene.foreground.effect.set("effect\\speedlines.png")
scene.foreground.character_center.set("sprite\\Castle-3.png")
scene.update()
sleep(3)
scene.foreground.character_center.hide()
scene.foreground.character_left.set("sprite\\Castle-3.png")
scene.foreground.character_right.set("sprite\\Lancet-2.png")
scene.foreground.character_right.listening()
scene.background.to_bottom()
scene.update()
sleep(3)
scene.foreground.character_left.listening()
scene.foreground.character_right.speaking()
scene.background.to_bottom()
scene.update()
sleep(3)
scene.foreground.character_left.hide()
scene.foreground.character_right.hide()
scene.foreground.character_center.set("sprite\\Lancet-2.png")
scene.update()
sleep(3)

root.mainloop()


'''
def f(pos, / , kw1='', kw2='', kw3='no'):
    print("pos =", pos)
    print("kw1 =", kw1)
    print("kw2 =", kw2)

kw2 = "Cruel"
f("Hello", kw2="World")

#fade effect
from PIL import Image

sprite2 = Image.open("sprite\\Castle-3.png").convert("RGBA")
sprite2 = sprite2.point(lambda x: x * 0.4)
sprite2.show()
sprite2.save("Test.png")
'''