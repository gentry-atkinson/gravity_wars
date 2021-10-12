import GW_utils
import GW_globals
import pygame
import os
import math


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
    def move(self, dt):
        self.x += self.vx * dt/1000
        self.y += self.vy * dt/1000
        if -100 > self.x > 900 or -100 > self.y > 900:
            self.dead = True

class Laser(Projectile):
    def __init__(self, x, y, rot):
        icon = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'shot.png')), (3, 6))
        vx = -math.sin(rot*GW_globals.DEG_TO_RAD) * GW_globals.C
        vy = -math.cos(rot*GW_globals.DEG_TO_RAD) * GW_globals.C
        super().__init__(x, y, vx, vy, icon, rot)
