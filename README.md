# python-visual-novel
![Screenshot](https://i.imgur.com/W91NIVq.jpg)
This is a simple "Hello world" visual novel (Japanese point-click choose-your-own-adventure game) written in Python. The app supports Windows OS and the custom sound library will not work in other OS. 

The only dependency is Pillow (PIL).

## stats
Version: 1.0.0

Project started: 26 February 2020

Project published: 3 March 2020

## backlog
* Scenario importer
* Save/Load system
* Branching selection menu
* Animated UI elements (next arrow icon at the end of line)
* Fade-out scene transition
* Voiceline ending event (to proceed with autoscroll after the playback is finished)
* Autoscroll
* Asynchronous/Non-blocking dialog printer (currently the printer is blocking for 0.05s for every character, circumvented via callback global event hack)