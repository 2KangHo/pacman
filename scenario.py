import cocos.tiles
import cocos.actions as ac


def move(x, y):
    cell_size = 32
    dur = abs(x+y)*cell_size / 100.0
    return ac.MoveBy((x*cell_size, y*cell_size), duration=dur)


class Scenario(object):
    def __init__(self, tmx_map, player_start, ghosts_start, ghosts_action):
        self.tmx_map = tmx_map
        self.player_start = player_start
        self.ghosts_start = ghosts_start
        self.ghosts_action = ghosts_action
        #self._actions = None

    #@property
    #def actions(self):
    #    return self._actions

    #@actions.setter
    #def actions(self, actions):
    #    self._actions = ac.Delay(5)
    #    for step in actions:
    #        self._actions += step
    
    def get_background(self):
        tmx_map = cocos.tiles.load('assets/GUI/pacman.tmx')
        bg = tmx_map[self.tmx_map]
        bg.set_view(0, 0, bg.px_width, bg.px_height)
        return bg


def get_scenario():
    player_start = (336, 176)
    ghosts_start = [(336, 432), (304, 368), (336, 368), (368, 368)]
    ghosts_action = [move(-3,0) + move(0,-6) + move(-2,0) + move(0,-4) +\
                     move(-4,0) + move(0,-2) + move(18,0) + move(0,2) +\
                     move(-4,0) + move(0,4) + move(-2,0) + move(0,6) +\
                     move(-3,0),
                     move(0,0),
                     move(0,0),
                     move(0,0)]
    sc = Scenario('map0', player_start, ghosts_start, ghosts_action)
    #sc.actions = [[],
    #              [],
    #              [],
    #              []]
    return sc