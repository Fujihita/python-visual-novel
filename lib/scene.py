from lib.background import Background
from lib.foreground import Foreground


class Scene:

    def __init__(self,root):
        self.background = Background(root)
        self.foreground = Foreground(root)
        self.root = root
    
    def update(self):
        self.root.update()
        self.background.to_bottom()
        self.foreground.to_top()


'''
dictionary look up table
[{
    name: 'Lancet-2'
    state: 'normal'
    art: 'art\\Lancet-2.png'
},
{
    name: 'Lancet-2'
    state: 'angry'
    art: 'art\\Lancet-2.png'
},
{
    name: 'Castle-3'
    state: 'normal'
    art: 'art\\Castle-3.png'
}
]
'''

        
        
