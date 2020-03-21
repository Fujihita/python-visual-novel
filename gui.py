from time   import sleep
from lib.audio import audio
from lib.scene import scene
from tkinter import Tk

root = Tk()
root.title("Hello, Python")
root.wm_state('zoomed')
position = 0

def callback(event):
    global position
    position += 1

def next(pos):
    global position
    global root
    while position < pos:
        root.update()
    print("next", position)

scene = scene(callback, root)
bgm = audio()
voice = audio()

#Scenario starts below
scene.background("background\\background-2.jpg")
scene.foreground("sprite\\Castle-3.png")
bgm.play('music\\bgm.mp3', loop=True)
scene.dialog("Castle-3","Objective cleared!")
next(1)
bgm.stop_sound()
scene.foreground("sprite\\Castle-3.png","sprite\\Lancet-2.png", active="char2")
bgm.play('music\\7F.mp3', loop=True)
voice.play('voice\\voice.mp3')
scene.dialog("Lancet-2","Be on your guard, we're not in the clear yet!")
next(2)
voice.stop_sound()
scene.foreground("sprite\\Castle-3.png","sprite\\Lancet-2.png")
scene.dialog("Castle-3","Please! Nothing here can even put a scratch on my armor. It would take a real boss to get me sweating.")
next(3)
scene.dialog("Castle-3","Well, but that will never happen, right?")
next(4)
bgm.stop_sound()
scene.background("background\\background-1.jpg")
scene.foreground(char2="sprite\\Navigator.png",active="char2")
bgm.play('music\\boss.mp3', loop=True)
scene.dialog("A real boss","Famous last words, son.")
next(5)
bgm.stop_sound()