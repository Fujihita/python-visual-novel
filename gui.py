from time   import sleep
from lib.audio import audio
from lib.scene import scene
from tkinter import Tk

root = Tk()
root.title("Testbench")
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
        root.update_idletasks()

scene = scene(callback, root)
bgm = audio()
voice = audio()

bgm.play('music\\bgm.mp3', loop=True)
scene.draw(
            "CASTLE-3",
            "Objective cleared!",
            "background\\background.jpg",
            "sprite\\Castle-3.png")
next(1)
bgm.stop_sound()

bgm.play('music\\7F.mp3', loop=True)
voice.play('voice\\voice.mp3')
scene.draw(
            "LANCET-2",
            "But at what cost?",
            "background\\background.jpg",
            "sprite\\Castle-3.png",
            "sprite\\Lancet-2.png", char2_first=True)

next(2)
voice.stop_sound()
scene.draw(
            "CASTLE-3",
            "None that exceeds the margin of error. The important matter is, we survived that bloody skirmish and I sure did not think we would.",
            "background\\background.jpg",
            "sprite\\Castle-3.png",
            "sprite\\Lancet-2.png")
next(3)
bgm.stop_sound()