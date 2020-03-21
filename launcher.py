from lib.audio import audio
from lib.scene import scene
from tkinter import Tk

root = Tk()
root.title("Hello, Python")
root.wm_state('zoomed')
#root.attributes('-fullscreen', True)
position = 0

def callback(event):
    global position
    position += 1

def next(pos):
    global position
    global root
    global scene
    while position < pos:
        scene.update_dialog()
        root.update()
    if scene.update_dialog():
        scene.skip_dialog()
        position = pos - 1
        while position < pos:
            root.update()

scene = scene(callback, root)
bgm = audio()
voice = audio()

#Scenario starts below
bgm.play('music\\bgm.mp3', loop=True)
scene.background("background\\background-2.jpg")
scene.foreground("sprite\\Castle-3.png")
scene.dialog("Castle-3","Mission accomplished!")
next(1)

bgm.stop_sound()
bgm.play('music\\7F.mp3', loop=True)
scene.foreground("sprite\\Castle-3.png","sprite\\Lancet-2.png", active="char2")
scene.dialog("Lancet-2","Be on your guard, we're not in the clear yet!")
voice.play('voice\\voice.mp3')
next(2)

voice.stop_sound()
scene.foreground("sprite\\Castle-3.png","sprite\\Lancet-2.png", active="char1")
scene.dialog("Castle-3","Please! Nothing here can even put a scratch on my armor. It would take a real boss to get me sweating.")
next(3)

scene.dialog("Castle-3","Well, something that plot-convenient would never happen, right?")
next(4)

bgm.stop_sound()
bgm.play('music\\boss.mp3', loop=True)
scene.background("background\\background-1.jpg")
scene.foreground(char2="sprite\\Navigator.png",active="char2")
scene.effect("effect\\menacing.png")
scene.dialog("A real boss","Famous last words, son.")
next(5)

scene.effect("")
scene.foreground("sprite\\Castle-3.png","sprite\\Lancet-2.png")
scene.effect("effect\\speedlines.png", top=True)
scene.dialog("","*Le gasp* A wild boss appeared!")
voice.play('voice\\voice2.wav')
next(6)
voice.stop_sound()
bgm.stop_sound()