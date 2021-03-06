import random

from cocos.director import director
from cocos.scenes.transitions import SplitColsTransition, FadeTransition
import cocos.layer
import cocos.scene
import cocos.text
import cocos.actions as ac
import cocos.collision_model as cm

import pygame.mixer

import actors
import mainmenu
from scenario import get_scenario


class GameLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, hud, scenario):
        super(GameLayer, self).__init__()
        self.hud = hud
        self.scenario = scenario
        self.score = self._score = 0
        self.lives = self._lives = 3

        self.create_player()
        self.create_ghosts()
        self.create_dots()

        w, h = director.get_window_size()
        cell_size = 32
        self.coll_man = cm.CollisionManagerGrid(0, w, 0, h, cell_size, cell_size)
        self.coll_man_dots = cm.CollisionManagerGrid(0, w, 0, h, cell_size, cell_size)

        pygame.mixer.init()
        self.sounds={'die'   : pygame.mixer.Sound("assets/Sounds/pacman_death.wav"), \
                     'intro' : pygame.mixer.Sound("assets/Sounds/pacman_beginning.wav"), \
                     'waka'  : pygame.mixer.Sound("assets/Sounds/pacman_chomp.wav")}
                     
        self.sounds['intro'].play()
        self.schedule(self.game_loop)
    
    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, val):
        self._lives = val
        self.hud.update_lives(val)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        self._score = val
        self.hud.update_score(val)

    def game_loop(self, _):
        self.coll_man.clear()
        self.coll_man_dots.clear()
        for obj in self.get_children():
            if isinstance(obj, actors.Blinky):
                self.coll_man.add(obj)
            if isinstance(obj, actors.Clyde):
                self.coll_man.add(obj)
            if isinstance(obj, actors.Inky):
                self.coll_man.add(obj)
            if isinstance(obj, actors.Pinky):
                self.coll_man.add(obj)

    def create_player(self):
        player_start = self.scenario.player_start
        x, y = player_start
        self.add(actors.Player(x, y, ac.Delay(5)))

    def create_ghosts(self):
        ghosts_start = self.scenario.ghosts_start
        blinky_x, blinky_y = ghosts_start[0]
        clyde_x, clyde_y = ghosts_start[1]
        inky_x, inky_y = ghosts_start[2]
        pinky_x, pinky_y = ghosts_start[3]
        self.add(actors.Blinky(blinky_x, blinky_y, ac.Delay(5)+ac.Repeat(self.scenario.ghosts_action[0])))
        self.add(actors.Clyde(clyde_x, clyde_y, ac.Delay(7)+ac.Repeat(self.scenario.ghosts_action[1])))
        self.add(actors.Inky(inky_x, inky_y, ac.Delay(9)+ac.Repeat(self.scenario.ghosts_action[2])))
        self.add(actors.Pinky(pinky_x, pinky_y, ac.Delay(11)+ac.Repeat(self.scenario.ghosts_action[3])))

    def create_dots(self):
        pass

    def on_key_release(self, key, _):
        pass
        #actors.Player.speed *= 1


class HUD(cocos.layer.Layer):
    def __init__(self):
        super(HUD, self).__init__()
        w, h = director.get_window_size()
        self.score_text = self._create_text(w/2, h-18)
        self.score_points = self._create_text(w/2, h-48)

    def _create_text(self, x, y):
        text = cocos.text.Label(font_size=15, font_name='Emulogic',
                                anchor_x='center', anchor_y='center')
        text.position = (x, y)
        self.add(text)
        return text

    def update_score(self, score):
        self.score_text.element.text = 'Score: %s' % score

    def update_lives(self, lives):
        self.score_points.element.text = 'Lives: %s' % lives


def new_game():
    scenario = get_scenario()
    background = scenario.get_background()
    hud = HUD()
    game_layer = GameLayer(hud, scenario)
    return cocos.scene.Scene(background, game_layer, hud)


def game_over():
    w, h = director.get_window_size()
    layer = cocos.layer.Layer()
    text = cocos.text.Label('Game Over', position=(w*0.5, h*0.5),
                            font_name='Emulogic', font_size=64,
                            anchor_x='center', anchor_y='center')
    layer.add(text)
    scene = cocos.scene.Scene(layer)
    new_scene = FadeTransition(mainmenu.new_menu())
    func = lambda: director.replace(new_scene)
    scene.do(ac.Delay(3) + ac.CallFunc(func))
    return scene


Game_Map = \
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
 [0, 7, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 7, 0],
 [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
 [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
 [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 4, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 1, 1, 0, 4, 4, 4, 0, 1, 1, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
 [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
 [0, 7, 1, 1, 0, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 0, 1, 1, 7, 0],
 [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
 [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]