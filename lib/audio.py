class PlaysoundException(Exception):
    pass

class audio:
    '''
    Exerpt and modified code from playsound module for Windows
    Support .mp3 and .wav files playbacks using only the native Python modules
    This module no longer supports blocking and instead supports multi-channel parallel playbacks
    Built-in loop option
    The playback can now be interrupted at any time with 1s delay while looping
    '''
    def play(self, sound, loop = False):
        self.sound = sound
        self.loop = loop
        from random import random
        self.alias = 'playsound_' + str(random())
        self.play_sound()

    def winCommand(self, *command):
        from ctypes import c_buffer, windll
        from sys    import getfilesystemencoding

        buf = c_buffer(255)
        command = ' '.join(command).encode(getfilesystemencoding())
        errorCode = int(windll.winmm.mciSendStringA(command, buf, 254, 0))
        if errorCode:
            errorBuffer = c_buffer(255)
            windll.winmm.mciGetErrorStringA(errorCode, errorBuffer, 254)
            exceptionMessage = ('\n    Error ' + str(errorCode) + ' for command:'
                                '\n        ' + command.decode() +
                                '\n    ' + errorBuffer.value.decode())
            raise PlaysoundException(exceptionMessage)
        return buf.value

    def play_sound(self):
        from threading import Timer
        if self.loop:
            sched = Timer(0.1, self.play_loop)
            sched.start()
        else:
            self.play_once()

    def play_once(self):
        self.winCommand('open "' + self.sound + '" alias', self.alias)
        self.winCommand('set', self.alias, 'time format milliseconds')
        self.durationInMS = self.winCommand('status', self.alias, 'length')
        self.winCommand('play', self.alias, 'from 0 to', self.durationInMS.decode())

    def play_loop(self):
        from time import sleep
        self.play_once()
        counter = 0.0
        while self.loop: 
            if counter >= (float(self.durationInMS) / 1000.0):
                self.winCommand('play', self.alias, 'from 0 to', self.durationInMS.decode())
                counter = 0.0
            sleep(0.1)
            counter += 0.1
        self.stop()
    
    def stop(self):
        from time import sleep
        if self.loop:
            self.loop = False # set flag in Main thread
            sleep(0.1)
        else:
            self.winCommand('close', self.alias)