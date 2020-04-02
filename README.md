# python-visual-novel
![Screenshot](https://i.imgur.com/W91NIVq.jpg)
This is a simple "Hello world" visual novel (Japanese point-click choose-your-own-adventure game) written in Python. The app supports Windows OS and the custom sound library will not work in other OS. 

The only dependency is Pillow (PIL).

## stats
Version: 1.0.1

Project started: 18 March 2020

Project published: 21 March 2020

## feature
* Setting background
* Displaying two sprites at once and the option to focus on one or both sprites
* Overlaying effects before or after the sprites
* Interruptible multi-track audio playback with looping option (.mp3 and .wav support)
* Running text printer with dialog skip on mouse click option

## backlog
* Scenario importer
* Save/Load system
* Branching selection menu
* Animated UI elements (next arrow icon at the end of line)
* Fade-out scene transition
* Voiceline ending event (to proceed with autoscroll after the playback is finished)
* Autoscroll
* Asynchronous/Non-blocking dialog printer (currently the printer is blocking for 0.05s for every character, circumvented via callback global event hack)
