from header import *

with open("scenario.txt", "r", encoding="utf8") as src:
    src.seek(0)
    line = src.readline()
    while line:
        if line[:9] == 'character':                         # import character aliases
            char_dict[line[10:line.find('"')-1]] = line[line.find('"')+1:-2]
            save.alias(line)

        elif line[:-1] == "hide all":
            character.clear()

        elif line[:10] == 'background':                     # set background
            character.clear()
            background.set("background\\" + line[11:-1] + ".jpg")
            save.background(line)

        elif line[:5] == 'music':                           # set music
            music.set("music\\" + line[6:-1] + ".mp3")
            save.music(line)

        elif line[:5] == 'audio':                           # set voice
            audio.set("audio\\" + line[6:-1] + ".mp3")
            save.audio(line)

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
            if alias != '' and  '" "' not in line and '--nameless' not in line:
                name.set(char_dict[alias])
            elif '" "' in line:
                name.set(line[2:line.find('" "')])
            else:
                name.set("")
            
            if alias != '':
                character.set("art\\" + char_dict[alias] + ".png")
            elif '" "' not in line:                         # narrator
                character.clear()
            else:
                line = line[line.find('" "')+2:]
            
            if "--nographic" in line:
                character.hide("art\\" + char_dict[alias] + ".png")

            dialog.set(line[line.find('"')+1:line.rfind('"')])
            
            wait_input()
            save.position(src.tell())

        elif line == "exit":
            music.stop()
            scene.update()

        line = src.readline()