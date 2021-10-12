import pygame
import GW_globals
import math

def euc_dist (x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

class Ship:
    def __init__(self, x, y, vx, vy, icon):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.rot = 0
        self.icon = icon
        self.mask = pygame.mask.from_surface(self.icon)
    def draw(self, screen):
        screen.blit(self.icon, (self.x, self.y))
    def get_width(self):
        return self.icon.get_width()
    def get_height(self):
        return self.icon.get_height()
    def fall(self):
        dist = euc_dist(self.x, self.y, GW_globals.WIDTH/2, GW_globals.HEIGHT/2)
        if self.x > GW_globals.WIDTH/2:
            self.vx -= GW_globals.GRAVITY/dist
        else:
            self.vx += GW_globals.GRAVITY/dist
        if self.y > GW_globals.HEIGHT/2:
            self.vy -= GW_globals.GRAVITY/dist
        else:
            self.vy += GW_globals.GRAVITY/dist

class Player(Ship):
    def __init__(self, x, y, vx, vy, icon):
        super().__init__(x, y, vx, vy, icon)
    def move(self, keys):
        self.fall()
        self.x += self.vx
        self.y += self.vy
        if keys[pygame.K_UP]:
            self.vy -= .1
        if keys[pygame.K_DOWN]:
            self.vy += .1
        if keys[pygame.K_LEFT]:
            self.rot += .1
            self.vx -= .1
        if keys[pygame.K_RIGHT]:
            self.rot += .1
            self.vx += .1

        self.rot = self.rot%360
        #self.icon = pygame.transform.rotate(self.icon, self.rot)

        if self.vx > GW_globals.C:
            self.vx = GW_globals.C
        elif self.vx < -GW_globals.C:
            self.vx = -GW_globals.C
        elif self.vy > GW_globals.C:
            self.vy = GW_globals.C
        elif self.vy < -GW_globals.C:
            self.vy = -GW_globals.C
