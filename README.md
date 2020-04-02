# python-visual-novel
![Screenshot](https://i.imgur.com/W91NIVq.jpg)
This is a simple "Hello world" visual novel (Japanese point-click choose-your-own-adventure game) written in Python. The app supports Windows OS and the custom sound library will not work in other OS. 

The only dependency is Pillow (PIL).

## stats
Version: 1.1.0

Project started: 18 March 2020

Project published: 21 March 2020

## feature
* Layer management for background, foreground and interface elements.
* Displaying up to three characters at once.
* Animated effects before or after the characters
* Interruptible multi-track audio playback with looping option (.mp3 and .wav support)
* Running text printer with dialog skip on mouse click option

## backlog
* Refactor audio module, add playback ending event (to proceed with autoscroll after the playback is finished), force each audio object to play only one track and force stop the previous track when a new track is set.
* Animated UI elements (next arrow icon at the end of line)
* Fade-out scene transition
* Scenario importer + Save/Load system
* Branching selection menu
* Autoscroll