# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Filename:    player_animation.py
# Created:     03/16/2017
# Author:      TurBoss
# E-mail:      j.l.toledano.l@gmail.com
# License:     GNU GPL 3.0
# ---------------------------------------------------------------------------

from sdl2.ext import Applicator, Sprite

from player import PlayerData

from components.velocity import Velocity


class PlayerMovementSystem(Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(PlayerMovementSystem, self).__init__()
        self.componenttypes = PlayerData, Velocity, Sprite
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def process(self, world, componentsets):
        for playerdata, velocity, sprite in componentsets:

            if not playerdata.life:
                return

            swidth, sheight = sprite.size
            sprite.x += velocity.vx
            sprite.y += velocity.vy

            sprite.x = max(self.minx, sprite.x)
            sprite.y = max(self.miny, sprite.y)

            pmaxx = sprite.x + swidth
            pmaxy = sprite.y + sheight
            if pmaxx > self.maxx:
                sprite.x = self.maxx - swidth
            if pmaxy > self.maxy:
                sprite.y = self.maxy - sheight
