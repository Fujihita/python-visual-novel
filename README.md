# python-visual-novel
This is a simple "Hello world" visual novel engine (Japanese point-click choose-your-own-adventure game) written in Python. The app supports Windows OS and the custom sound library will not work in other OS. 

The only dependency is Pillow (PIL).

## stats
Version: 1.2.3

Project started: 18 March 2020

Project published: 21 March 2020

## feature
* Layer management for background, foreground and interface elements.
* Displaying up to three characters at once (auto-managed positions).
* Animated effects before or after the characters
* Interruptible multi-track audio playback with looping option (.mp3 and .wav support)
* Running text printer with dialog skip on mouse click option
* Importing custom scenarios from an editable text file (custom syntax based on Ren'Py)

## preview
* Scenario 1: Two robots wander outside despite the doctor's order to stay home.
![Scenario 1](https://i.imgur.com/bq6JsIW.jpg)
* Scenario 2 (default): A conversation between an inventor and a knight. Based on an ongoing novel project (https://fujihita.wordpress.com/tag/white-destiny/)
![Scenario 2](https://i.imgur.com/svJbEAh.jpg)

## backlog
* Save/Load system
* Animated UI elements (next arrow icon at the end of line)
* Fade-out scene transition
* Branching selection menu
* Autoscroll