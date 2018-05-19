import math

import cocos.sprite
import cocos.audio
import cocos.actions as ac
import cocos.euclid as eu
import cocos.collision_model as cm

import pyglet.image
from pyglet.image import Animation


class Actor(cocos.sprite.Sprite):
    def __init__(self, img, x, y):
        super(Actor, self).__init__(img, position=(x, y))
        self._cshape = cm.CircleShape(self.position, self.width*0.5)

    @property
    def cshape(self):
        self._cshape.center = eu.Vector2(self.x, self.y)
        return self._cshape


class Blinky(Actor):
    def __init__(self, x, y, actions):
        super(Blinky, self).__init__('', x, y)
        self.do(actions)


class Clyde(Actor):
    def __init__(self, x, y, actions):
        super(Clyde, self).__init__('', x, y)
        self.do(actions)


class Inky(Actor):
    def __init__(self, x, y, actions):
        super(Inky, self).__init__('', x, y)
        self.do(actions)


class Pinky(Actor):
    def __init__(self, x, y, actions):
        super(Pinky, self).__init__('', x, y)
        self.do(actions)


class Player(Actor):
    def __init__(self, x, y, actions):
        super(Player, self).__init__('', x, y)
        self.do(actions)
