from header import *

with open("scenario.txt", "r", encoding="utf8") as src:
    src.seek(0)
    line = src.readline()
    while line:
        if line[:9] == 'character':                         # import character aliases
            char_dict[line[10:line.find('"')-1]] = line[line.find('"')+1:-2]
            save.alias(line)

        elif line[:10] == 'background':                     # set background
            background.set("background\\" + bg_dict[line[11:-1]])
            save.background(line)

        elif line[:5] == 'music':                           # set music
            music.set("music\\" + line[6:-1] + ".mp3")
            save.music(line)

        elif line[:5] == 'voice':                           # set voice
            voice.set("voice\\" + line[6:-1] + ".mp3")
            save.voice(line)

        elif line[:6] == 'effect':                          # set effect
            save.effect("effect")
            line = line.replace("effect ", "")
            if "bottom" in line:
                line = line.replace("bottom ", "")
                getattr(effect_bottom, line[:line.find(" ")])("effect\\" + line[line.find(" ")+1:-1] + ".png")
            else:
                line = line.replace("top ", "")
                getattr(effect_top, line[:line.find(" ")])("effect\\" + line[line.find(" ")+1:-1] + ".png")

        elif line[0] == "\t":                               # set dialog
            alias = line[1:line.find('"')-1]
            if alias != '' and "--nameless" not in line:
                name.set(char_dict[alias])
            else:
                name.set("")
            if alias != '':
                character_center.set("art\\" + art_dict[char_dict[alias]][""])
            else:
                character_center.hide()
            dialog.set(line[line.find('"')+1:line.rfind('"')])
            wait_input()
            save.position(src.tell())

        elif line == "exit":
            music.stop()
            scene.update()

        line = src.readline()

'''
music.set('music\\bgm.mp3')
background.set("background\\background-2.jpg")
effect_top.blink("effect\\speedlines.png")
character_center.set("art\\Castle-3.png")
name.set("CASTLE-3")
dialog.set("Mission accomplished!")
next(1)

music.set('music\\7F.mp3')
voice.set('voice\\voice.mp3')
character_left.set("art\\Castle-3.png")
character_left.listening()
character_center.hide()
character_right.set("art\\Lancet-2.png")
character_right.speaking()
name.set("LANCET-2")
dialog.set("Be on your guard, we're not in the clear yet!")
effect_top.stop()
next(2)

character_left.speaking()
character_right.listening()
name.set("CASTLE-3")
dialog.set("Please! Nothing here can even put a scratch on my armor. It would take a real boss to get me sweating.")
next(3)

name.set("CASTLE-3")
dialog.set("Well, something that plot-convenient would never happen, right?")
next(4)

music.set('music\\boss.mp3')
background.set("background\\background-1.jpg")
character_left.hide()
character_center.set("art\\Navigator.png")
character_right.hide()
name.set("A real bosss")
dialog.set("Famous last words, son.")
effect_bottom.shake("effect\\menacing.png")
next(5)

music.stop()

'''