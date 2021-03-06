from lib.layers import Scene
from tkinter import Tk, Canvas
from lib.audio import Audio
from lib.save import Save

save = Save()
wait_flag = False

def callback(event):
    global wait_flag
    wait_flag = False
    
root = Tk()
root.title("Hello, Python")
root.wm_state('zoomed')
canvas = Canvas(root, width=1366, height=768, background="black")
canvas.bind("<Button-1>", callback)
canvas.pack()
root.update()

scene = Scene(canvas)

music = Audio(mode="loop")
audio = Audio()
background = scene.background.wallpaper
effect_bottom = scene.background.effect
character_center = scene.foreground.character_center
character_left =  scene.foreground.character_left
character_right =  scene.foreground.character_right
character = scene.foreground
effect_top =  scene.interface.effect
dialog = scene.interface.dialog
name = scene.interface.name

def on_closing():
    music.stop()
    audio.stop()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

def wait_input():
    global position
    global scene
    global wait_flag
    wait_flag = True
    while wait_flag:
        scene.update()
    if dialog.skip():
        wait_flag = True
        while wait_flag:
            scene.update()
    audio.stop()

char_dict = {}      # map user-defined alias -> character