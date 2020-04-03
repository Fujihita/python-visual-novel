from lib.layers import Scene
from tkinter import Tk, Canvas
from lib.audio import Audio

position = 0

def callback(event):
    global position
    global scene
    scene.update()
    position += 1

root = Tk()
root.title("Hello, Python")
root.wm_state('zoomed')
canvas = Canvas(root, width=1366, height=768, background="black")
canvas.bind("<Button-1>", callback)
canvas.pack()
root.update()

scene = Scene(canvas)

music = Audio(mode="loop")
voice = Audio()
background = scene.background.wallpaper
effect_bottom = scene.background.effect
character_center = scene.foreground.character_center
character_left =  scene.foreground.character_left
character_right =  scene.foreground.character_right
effect_top =  scene.interface.effect
dialog = scene.interface.dialog
name = scene.interface.name

def next(pos):
    global position
    global root
    global scene
    while position < pos:
        scene.update()
    if dialog.skip():
        position -= 1
        while position < pos:
            scene.update()
        voice.stop()

#Scenario starts below
'''
Settings for scenes:
    music.set
    voice.set
    background.set
    character_left.set
    character_center.set
    character_right.set
    dialog.set
    name.set
    effect_bottom.set
    effect_top.set
'''

music.set('music\\bgm.mp3')
background.set("background\\background-2.jpg")
character_left.hide()
character_center.set("art\\Castle-3.png")
character_right.hide()
name.set("CASTLE-3")
dialog.set("Mission accomplished!")
effect_bottom.stop()
effect_top.set("effect\\speedlines.png")
effect_top.blink()
next(1)

music.set('music\\7F.mp3')
voice.set('voice\\voice.mp3')
background.set("background\\background-2.jpg")
character_left.set("art\\Castle-3.png")
character_left.listening()
character_center.hide()
character_right.set("art\\Lancet-2.png")
character_right.speaking()
name.set("LANCET-2")
dialog.set("Be on your guard, we're not in the clear yet!")
effect_bottom.stop()
effect_top.stop()
next(2)

music.set('music\\7F.mp3')
background.set("background\\background-2.jpg")
character_left.set("art\\Castle-3.png")
character_left.speaking()
character_center.hide()
character_right.set("art\\Lancet-2.png")
character_right.listening()
name.set("CASTLE-3")
dialog.set("Please! Nothing here can even put a scratch on my armor. It would take a real boss to get me sweating.")
effect_bottom.stop()
effect_top.stop()
next(3)

music.set('music\\7F.mp3')
background.set("background\\background-2.jpg")
character_left.set("art\\Castle-3.png")
character_left.speaking()
character_center.hide()
character_right.set("art\\Lancet-2.png")
character_right.listening()
name.set("CASTLE-3")
dialog.set("Well, something that plot-convenient would never happen, right?")
effect_bottom.stop()
effect_top.stop()
next(4)

music.set('music\\boss.mp3')
background.set("background\\background-1.jpg")
character_left.hide()
character_center.set("art\\Navigator.png")
character_right.hide()
name.set("A real bosss")
dialog.set("Famous last words, son.")
effect_bottom.set("effect\\menacing.png")
effect_bottom.shake()
effect_top.stop()
next(5)

music.stop()