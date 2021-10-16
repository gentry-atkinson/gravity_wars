import pygame
import GW_globals
import math
import GW_utils
from Projectile import Laser
import Image_Loader as IL

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
        self.drift = False

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
    def __init__(self, x, y, vx, vy):
        super().__init__(x, y, vx, vy, IL.PLAYER_SHIP)
        self.lastShot = 0
        self.zap_sound = pygame.mixer.Sound('assets/sounds/low_chirp.wav')
        self.score = 0
        self.shield = True

    def move(self, keys, projectiles, dt):
        self.fall()
        self.x += self.vx * dt/1000
        self.y += self.vy * dt/1000
        if self.x > 900 or self.x < -100:
            self.drift = True
        elif self.y > 900 or self.y < -100:
            self.drift = True
        else:
            self.drift = False

        self.lastShot += dt
        if keys[pygame.K_UP]:
            self.vy -= math.cos(self.rot*GW_globals.DEG_TO_RAD) * GW_globals.THRUST
            self.vx -= math.sin(self.rot*GW_globals.DEG_TO_RAD) * GW_globals.THRUST
            self.icon = IL.PLAYER_SHIP_BURN
        else:
            self.icon = IL.PLAYER_SHIP
        # if keys[pygame.K_DOWN]:
        #     self.vy += math.cos(self.rot) * GW_globals.THRUST
        #     self.vx += math.sin(self.rot) * GW_globals.THRUST
        if keys[pygame.K_LEFT]:
            self.rot += GW_globals.TURN_SPEED
        if keys[pygame.K_RIGHT]:
            self.rot -= GW_globals.TURN_SPEED
        if keys[pygame.K_SPACE]:
            off_x = -math.sin(self.rot*GW_globals.DEG_TO_RAD)*self.get_width() + self.get_width()//2
            off_y = -math.cos(self.rot*GW_globals.DEG_TO_RAD)*self.get_height() + self.get_height()//2
            if self.lastShot > 500:
                self.lastShot = 0
                projectiles.append(Laser(self.x+off_x, self.y+off_y, self.rot))
                pygame.mixer.Sound.play(self.zap_sound)

        self.rot = self.rot%360

        if self.vx > GW_globals.C:
            self.vx = GW_globals.C
        elif self.vx < -GW_globals.C:
            self.vx = -GW_globals.C
        elif self.vy > GW_globals.C:
            self.vy = GW_globals.C
        elif self.vy < -GW_globals.C:
            self.vy = -GW_globals.C
    def draw(self, screen):
        if self.shield:
            screen.blit(IL.SHIELD, (self.x-13, self.y-13))
        if self.icon == IL.PLAYER_SHIP_BURN:
            GW_utils.blitRotateCenter(screen, self.icon, (self.x, self.y-5), self.rot)
        else:
            GW_utils.blitRotateCenter(screen, self.icon, (self.x, self.y), self.rot)

class Enemy(Ship):
    def __init__(self, x, y, vx, vy, icon, rot):
        super().__init__(x, y, vx, vy, icon)
        self.rot = rot
        self.death_sound = pygame.mixer.Sound('assets/sounds/grumble.wav')
        self.points = 0
        self.mult = 1
    def die(self, ps):
        self.dead = True
        pygame.mixer.Sound.play(self.death_sound)
        ps.score += self.points*self.mult


class Rock(Enemy):
    def __init__(self, x, y, vx, vy, icon, rot):
        super().__init__(x, y, vx, vy, icon, rot)
        self.points = 10
    def move(self, projectiles, ps, dt):
        self.fall()
        self.x += self.vx * dt/1000
        self.y += self.vy * dt/1000
        self.rot += 1

class Satelite(Enemy):
    def __init__(self, x, y, vx, vy, icon, rot):
        super().__init__(x, y, vx, vy, icon, rot)
        self.lastShot = 0
        self.zap_sound = pygame.mixer.Sound('assets/sounds/high_chirp.wav')
        self.points = 100
    def move(self, projectiles, ps, dt):
        self.fall()
        self.x += self.vx * dt/1000
        self.y += self.vy * dt/1000
        self.rot -= 1
        self.lastShot += dt
        if self.lastShot > 1500:
            self.lastShot = 0
            directionToPlayer = math.atan2((self.x-ps.x), (self.y - ps.y))
            directionToPlayer %= 2*math.pi
            directionToPlayer = math.degrees(directionToPlayer)
            off_x = -math.sin(directionToPlayer*GW_globals.DEG_TO_RAD)*self.get_width() + self.get_width()//2
            off_y = -math.cos(directionToPlayer*GW_globals.DEG_TO_RAD)*self.get_height() + self.get_height()//2
            projectiles.append(Laser(self.x+off_x, self.y+off_y, directionToPlayer))
            pygame.mixer.Sound.play(self.zap_sound)
            self.points = math.ceil(self.points*0.9)
