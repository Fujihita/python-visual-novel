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

scene = scene(callback, root)
bgm = audio()
voice = audio()
bgm.play('music\\bgm.mp3', loop=True)
scene.set_background("background\\background-2.jpg")
scene.draw(
            "CASTLE-3",
            "Objective cleared!",
            "sprite\\Castle-3.png")
next(1)
bgm.stop_sound()

bgm.play('music\\7F.mp3', loop=True)
voice.play('voice\\voice.mp3')
scene.draw(
            "LANCET-2",
            "But at what cost?",
            "sprite\\Castle-3.png",
            "sprite\\Lancet-2.png", active="char2")
next(2)
voice.stop_sound()
scene.draw(
            "CASTLE-3",
            "Who cares? As long as I'm not the one paying it.",
            "sprite\\Castle-3.png",
            "sprite\\Lancet-2.png")

next(3)
bgm.stop_sound()
bgm.play('music\\boss.mp3', loop=True)
scene.set_background("background\\background-1.jpg")
scene.draw("Boss","Famous last words, son.",char2_src="sprite\\Navigator.png",active="char2")
next(4)
bgm.stop_sound()