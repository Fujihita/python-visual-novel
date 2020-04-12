class Save:
    '''
    A save of the game consists of a seek value and the recorded state of the game
    _state list consists of declarative scenario lines that will reconstruct the saved state
    Seven fixed parameters are recorded at the start, alias declarations are appended to the end.
    '''
    def __init__(self):
        self._state = [""]*5
        self._alias = []
        self._seek = 0
    
    def background(self, line):
        self._state[0] = line
    
    def music(self, line):
        self._state[1] = line
    
    def audio(self, line):
        self._state[2] = line
            
    def effect(self, line):
        self._state[3] = line
            
    def character(self, line):
        self._state[4] = line
    
    def alias(self, line):
        self._alias.append(line)

    def position(self, pos):
        self._seek = pos