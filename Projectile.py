import GW_utils
import GW_globals
import pygame
import os
import math
import Image_Loader as IL


class Projectile:
    def __init__(self, x, y, vx, vy, icon, rot):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.rot = rot
        self.icon = icon
        self.mask = pygame.mask.from_surface(self.icon)
        self.dead = False
    def draw(self, screen):
        GW_utils.blitRotateCenter(screen, self.icon, (self.x, self.y), self.rot)
    def get_width(self):
        return self.icon.get_width()
    def get_height(self):
        return self.icon.get_height()


class Laser(Projectile):
    def __init__(self, x, y, rot):
        icon = IL.LAS
        vx = -math.sin(rot*GW_globals.DEG_TO_RAD) * GW_globals.C
        vy = -math.cos(rot*GW_globals.DEG_TO_RAD) * GW_globals.C
        super().__init__(x, y, vx, vy, icon, rot)
    def move(self, dt):
        self.x += self.vx * dt/1000
        self.y += self.vy * dt/1000
        if self.x < -100 or self.x > GW_globals.WIDTH+100:
            self.dead = True
        elif self.y < -100 or self.y > GW_globals.HEIGHT+100:
            self.dead = True
