from threading import Timer, Thread, Event

class PlaysoundException(Exception):
    pass


class WinCommand:
    
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


class Audio(WinCommand):
     
    def __init__(self, mode = "single"):
        self._src = ''
        self._playing = ''
        if mode == "loop":
            self._play_mode = self._play_loop
        else:
            self._play_mode = self._play_once

    def set(self, src):
        self._src = src
        self._change_track()

    def _change_track(self):
        if self._playing == self._src:
            return
        if self._playing != '':
            self.stop()
        self._play_mode()

    def _play_once(self):
        from random import random
        self._alias = 'playsound_' + str(random())
        self._winCommand('open "' + self._src + '" alias', self._alias)
        self._winCommand('set', self._alias, 'time format milliseconds')
        self._duration = self._winCommand('status', self._alias, 'length')
        self._winCommand('play', self._alias, 'from 0 to', self._duration.decode())
        self._cleanup_timer = Timer(float(self._duration) / 1000.0, self._cleanup_handler)
        self._cleanup_timer.start()
        self._playing = self._src

    def _cleanup_handler(self):
        if self._playing != '':
            self._playing = ''
            self._cleanup_timer.cancel()

    def _play_loop(self):
        self._break_loop = Event()
        looper_thread = Thread(target=self._looper,args=(self._break_loop,))
        looper_thread.start()

    def _looper(self, event):
        from time import time as clock
        self._play_once()
        starttime = clock()
        while not self._break_loop.is_set(): 
            if clock() - starttime >= (float(self._duration) / 1000.0):
                self._play_once()
                starttime = clock()
        self.stop()

    def stop(self):
        try:
            self._break_loop.set()
        except AttributeError:
            pass
        if self._playing == '':
            return
        try:
            self._winCommand('close', self._alias)
        except PlaysoundException:
            pass
        finally:
            self._cleanup_handler()