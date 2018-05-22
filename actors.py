import math

import cocos.sprite
import cocos.audio
import cocos.actions as ac
import cocos.euclid as eu
import cocos.collision_model as cm

import pyglet.image
from pyglet.image import Animation


def load_animation(img, x, y, loop):
    raw = pyglet.image.load(img)
    seq = pyglet.image.ImageGrid(raw, x, y)
    return Animation.from_image_sequence(seq, 0.25, loop)


class Die(cocos.sprite.Sprite):
    def __init__(self, pos):
        die_img = load_animation('Player/pacman_die.png', 1, 11, False)
        super(Die, self).__init__(die_img, pos)
        self.do(ac.Delay(1) + ac.CallFunc(self.kill))

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
        blinky_up    = load_animation('Ghosts/blinky_up.png', 1, 2, True)
        blinky_down  = load_animation('Ghosts/blinky_down.png', 1, 2, True)
        blinky_left  = load_animation('Ghosts/blinky_left.png', 1, 2, True)
        blinky_right = load_animation('Ghosts/blinky_right.png', 1, 2, True)
        super(Blinky, self).__init__(blinky_up, x, y)
        self.do(actions)


class Clyde(Actor):
    def __init__(self, x, y, actions):
        clyde_up    = load_animation('Ghosts/clyde_up.png', 1, 2, True)
        clyde_down  = load_animation('Ghosts/clyde_down.png', 1, 2, True)
        clyde_left  = load_animation('Ghosts/clyde_left.png', 1, 2, True)
        clyde_right = load_animation('Ghosts/clyde_right.png', 1, 2, True)
        super(Clyde, self).__init__(clyde_up, x, y)
        self.do(actions)


class Inky(Actor):
    def __init__(self, x, y, actions):
        inky_up    = load_animation('Ghosts/inky_up.png', 1, 2, True)
        inky_down  = load_animation('Ghosts/inky_down.png', 1, 2, True)
        inky_left  = load_animation('Ghosts/inky_left.png', 1, 2, True)
        inky_right = load_animation('Ghosts/inky_right.png', 1, 2, True)
        super(Inky, self).__init__(inky_up, x, y)
        self.do(actions)


class Pinky(Actor):
    def __init__(self, x, y, actions):
        pinky_up    = load_animation('Ghosts/pinky_up.png', 1, 2, True)
        pinky_down  = load_animation('Ghosts/pinky_down.png', 1, 2, True)
        pinky_left  = load_animation('Ghosts/pinky_left.png', 1, 2, True)
        pinky_right = load_animation('Ghosts/pinky_right.png', 1, 2, True)
        super(Pinky, self).__init__(pinky_up, x, y)
        self.do(actions)


class Player(Actor):
    def __init__(self, x, y, actions):
        pacman_up    = load_animation('Player/pacman_up.png', 1, 4, True)
        pacman_down  = load_animation('Player/pacman_down.png', 1, 4, True)
        pacman_left  = load_animation('Player/pacman_left.png', 1, 4, True)
        pacman_right = load_animation('Player/pacman_right.png', 1, 4, True)
        super(Player, self).__init__('Player/pacman_start.png', x, y)
        self.do(actions)
