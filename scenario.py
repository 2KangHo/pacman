import cocos.tiles
import cocos.actions as ac


RIGHT = ac.RotateBy(90, 1)
LEFT = ac.RotateBy(-90, 1)


class Scenario(object):
    def __init__(self, tmx_map, player_start, ghosts_start):
        self.tmx_map = tmx_map
        self.player_start = player_start
        self.ghosts_start = ghosts_start

    def get_background(self):
        tmx_map = cocos.tiles.load('assets/GUI/pacman.tmx')
        bg = tmx_map[self.tmx_map]
        bg.set_view(0, 0, bg.px_width, bg.px_height)
        return bg





def get_scenario():
    player_start = (336, 176)
    ghosts_start = [(336, 432), (304, 368), (336, 368), (368, 368)]
    sc = Scenario('map0', player_start, ghosts_start)
    return sc