from cocos.director import director

import pyglet.font
import pyglet.resource

from mainmenu import new_menu


if __name__ == '__main__':
    pyglet.resource.path.append('assets')
    pyglet.resource.reindex()
    pyglet.font.add_file('assets/GUI/emulogic.ttf')
    pyglet.font.add_file('assets/GUI/CrackMan.ttf')

    director.init(caption='PAC-MAN', width=672, height=768)
    director.run(new_menu())
