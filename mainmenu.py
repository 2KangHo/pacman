import cocos.menu
import cocos.scene
import cocos.layer
import cocos.actions as ac
from cocos.director import director
from cocos.scenes.transitions import FadeTRTransition

import pyglet.app

from gamelayer import new_game


class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super(MainMenu, self).__init__('PAC-MAN')

        self.font_title['font_name'] = 'CrackMan'
        self.font_title['color'] = (255, 255, 0, 255)
        self.font_item['font_name'] = 'Emulogic'
        self.font_item['color'] = (255, 255, 255, 150)
        self.font_item_selected['font_name'] = 'Emulogic'
        self.font_item_selected['font_size'] = 32
        self.font_item_selected['color'] = (255, 255, 255, 255)

        self.menu_anchor_y = 'center'
        self.menu_anchor_x = 'center'

        items = list()
        items.append(cocos.menu.MenuItem('New Game', self.on_new_game))
        items.append(cocos.menu.MenuItem('Quit', pyglet.app.exit))

        self.create_menu(items)

    def on_new_game(self):
        director.push(FadeTRTransition(new_game(), duration=2))

    def show_fps(self, val):
        director.show_FPS = val


def new_menu():
    scene = cocos.scene.Scene()
    color_layer = cocos.layer.ColorLayer(0, 0, 0, 255)
    scene.add(MainMenu(), z=1)
    scene.add(color_layer, z=0)
    return scene
