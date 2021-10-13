import pygame
import GW_globals
import math
import GW_utils
from Projectile import Laser

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
        self.dead = False
    def draw(self, screen):
        GW_utils.blitRotateCenter(screen, self.icon, (self.x, self.y), self.rot)
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
        self.lastShot = 0
    def move(self, keys, projectiles, dt):
        self.fall()
        self.x += self.vx * dt/1000
        self.y += self.vy * dt/1000
        if self.x > 900 or self.x < -100:
            print('Lost in Space')
            self.dead = True
        elif self.y > 900 or self.y < -100:
            print('Lost in Space')
            self.dead = True
        self.lastShot += dt
        if keys[pygame.K_UP]:
            self.vy -= math.cos(self.rot*GW_globals.DEG_TO_RAD) * GW_globals.THRUST
            self.vx -= math.sin(self.rot*GW_globals.DEG_TO_RAD) * GW_globals.THRUST
        # if keys[pygame.K_DOWN]:
        #     self.vy += math.cos(self.rot) * GW_globals.THRUST
        #     self.vx += math.sin(self.rot) * GW_globals.THRUST
        if keys[pygame.K_LEFT]:
            self.rot += GW_globals.TURN_SPEED
        if keys[pygame.K_RIGHT]:
            self.rot -= GW_globals.TURN_SPEED
        if keys[pygame.K_SPACE]:
            if self.lastShot > 500:
                self.lastShot = 0
                projectiles.append(Laser(self.x, self.y, self.rot))


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

class Enemy(Ship):
    def __init__(self, x, y, vx, vy, icon, rot):
        super().__init__(x, y, vx, vy, icon)
        self.rot = rot

class Rock(Enemy):
    def __init__(self, x, y, vx, vy, icon, rot):
        super().__init__(x, y, vx, vy, icon, rot)
    def move(self, dt):
        self.fall()
        self.x += self.vx * dt/1000
        self.y += self.vy * dt/1000
        self.rot += 1

class Satelite(Enemy):
    def __init__(self, x, y, vx, vy, icon, rot):
        super().__init__(x, y, vx, vy, icon, rot)
        self.lastShot = 0
    def move(self, projectiles, ps, dt):
        self.fall()
        self.x += self.vx * dt/1000
        self.y += self.vy * dt/1000
        self.lastShot += dt
        if self.lastShot > 1000:
            self.lastShot = 0
            directionToPlayer = math.atan2((ps.y-self.y),(ps.x-self.x))
            projectiles.append(Laser(self.x, self.y, directionToPlayer))
