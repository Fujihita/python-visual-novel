class PlaysoundException(Exception):
    pass

class Audio:
    '''
    Exerpt and modified code from playsound module for Windows
    Support .mp3 and .wav files playbacks using only the native Python modules
    This module no longer supports blocking and instead supports multi-channel parallel playbacks
    Built-in loop option
    The playback can now be interrupted at any time with 1s delay while looping
    '''
    def __init__(self):
        self._src = ''
        self._looping_flag = False

    def set(self, src, loop = False):
        if self._src == src:
            return
        
        self._src = src
        self._looping_flag = loop
        from random import random
        self._alias = 'playsound_' + str(random())
        self._play_sound()

    def _winCommand(self, *command):
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

    def _play_sound(self):
        from threading import Timer
        if self._looping_flag:
            sched = Timer(0.1, self._play_loop)
            sched.start()
        else:
            self._play_once()

    def _play_once(self):
        self._winCommand('open "' + self._src + '" alias', self._alias)
        self._winCommand('set', self._alias, 'time format milliseconds')
        self._durationInMS = self._winCommand('status', self._alias, 'length')
        self._winCommand('play', self._alias, 'from 0 to', self._durationInMS.decode())

    def _play_loop(self):
        from time import sleep
        self._play_once()
        counter = 0.0
        while self._looping_flag: 
            if counter >= (float(self._durationInMS) / 1000.0):
                self._winCommand('play', self._alias, 'from 0 to', self._durationInMS.decode())
                counter = 0.0
            sleep(0.1)
            counter += 0.1
        self.stop()
    
    def stop(self):
        if self._src == '':
            return
        from time import sleep
        if self._looping_flag:
            self._looping_flag = False # set flag in Main thread
            sleep(0.1)
        else:
            self._winCommand('close', self._alias)
            sleep(0.1)