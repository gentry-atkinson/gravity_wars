import pygame
import GW_globals
import math
import GW_utils
from Projectile import Laser
import Image_Loader as IL
import Sound_Loader as SL
from Particle import Particle
import random

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
        super().__init__(x, y, vx, vy, IL.PLAYER_SHIP['no shield no burn'][0])
        self.imageList = IL.PLAYER_SHIP
        self.lastShot = 0
        self.zap_sound = SL.PLAYER_SHOOT
        self.death_sound = SL.PLAYER_DIE
        self.shield_sound = SL.PLAYER_SHIELD_DOWN
        self.score = 0
        self.shield = True
        self.burn = True
        self.stateTimer = 0

    def move(self, keys, projectiles, particles, dt):
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
            self.burn = True
            off_x = 0.5*math.sin(self.rot * GW_globals.DEG_TO_RAD)*self.get_width() + self.get_width()/2
            off_y = 0.5*math.cos(self.rot * GW_globals.DEG_TO_RAD)*self.get_height() + self.get_height()/2
            par_rot = self.rot + random.randint(-10, 10)
            par_vx = math.sin(par_rot * GW_globals.DEG_TO_RAD)*GW_globals.C*0.5
            par_vy =  math.cos(par_rot * GW_globals.DEG_TO_RAD)*GW_globals.C*0.5
            particles.append(Particle(self.x+off_x, self.y+off_y, par_vx, par_vy))
        else:
            self.burn = False
        # if keys[pygame.K_DOWN]:
        #     self.vy += math.cos(self.rot) * GW_globals.THRUST
        #     self.vx += math.sin(self.rot) * GW_globals.THRUST
        if keys[pygame.K_LEFT]:
            self.rot += GW_globals.TURN_SPEED*dt/1000
        if keys[pygame.K_RIGHT]:
            self.rot -= GW_globals.TURN_SPEED*dt/1000
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
        self.stateTimer = (self.stateTimer + dt)%1000

    def draw(self, screen):
        if self.shield and self.burn:
            GW_utils.blitRotateCenter(screen, self.imageList["with shield with burn"][0 if self.stateTimer < 500 else 1], (self.x, self.y), self.rot)
        elif self.shield and not self.burn:
            GW_utils.blitRotateCenter(screen, self.imageList["with shield no burn"][0 if self.stateTimer < 500 else 1], (self.x, self.y), self.rot)
        elif not self.shield and self.burn:
            GW_utils.blitRotateCenter(screen, self.imageList["no shield with burn"][0 if self.stateTimer < 500 else 1], (self.x, self.y), self.rot)
        else:
            GW_utils.blitRotateCenter(screen, self.imageList["no shield no burn"][0 if self.stateTimer < 500 else 1], (self.x, self.y), self.rot)
        # if self.shield:
        #     #x offset = 3-8
        #     off_x = math.sin(self.rot * GW_globals.DEG_TO_RAD)*5 - 3
        #     #y offset = 9-14
        #     off_y = math.cos(self.rot * GW_globals.DEG_TO_RAD)*5 - 12
        #     screen.blit(IL.SHIELD, (self.x+off_x, self.y+off_y))
        #
        # if self.burn:
        #     # off_x = math.sin(self.rot * GW_globals.DEG_TO_RAD)*self.get_width()
        #     # off_y = math.cos(self.rot * GW_globals.DEG_TO_RAD)*self.get_height()
        #     # GW_utils.blitRotateCenter(screen, IL.PLAYER_SHIP_BURN, (self.x+off_x, self.y+off_y), self.rot)
        #     GW_utils.blitRotateCenter(screen, IL.PLAYER_SHIP_BURN, (self.x, self.y), self.rot)
        # else:
        #     GW_utils.blitRotateCenter(screen, self.icon, (self.x, self.y), self.rot)

class Enemy(Ship):
    def __init__(self, x, y, vx, vy, icon, rot):
        super().__init__(x, y, vx, vy, icon)
        self.rot = rot
        self.death_sound = SL.ENEMY_EXPLODE
        self.points = 0
    def die(self, ps):
        self.dead = True
        pygame.mixer.Sound.play(self.death_sound)
        ps.score += self.points


class Rock(Enemy):
    def __init__(self, x, y, vx, vy, rot):
        super().__init__(x, y, vx, vy, IL.ROCK, rot)
        self.points = 10
    def move(self, projectiles, ps, particles, dt):
        self.fall()
        self.x += self.vx * dt/1000
        self.y += self.vy * dt/1000
        self.rot += 1
        if self.x > 900:
            self.x = 899
            self.vx = -self.vx
        elif self.y > 900:
            self.y = 899
            self.vy = -self.vy
        elif self.y < -100:
            self.y = -99
            self.vy = -self.vy
        elif self.x < -100:
            self.x = -99
            self.vx = -self.vx

class Satelite(Enemy):
    def __init__(self, x, y, vx, vy, rot):
        super().__init__(x, y, vx, vy, IL.SAT, rot)
        self.lastShot = 0
        self.zap_sound = SL.SAT_SHOOT
        self.points = 100
        self.SHOT_RATE = 1500
    def move(self, projectiles, ps, particles, dt):
        self.fall()
        self.x += self.vx * dt/1000
        self.y += self.vy * dt/1000
        self.rot -= 1
        self.lastShot += dt
        if self.lastShot > self.SHOT_RATE:
            self.lastShot = 0
            # directionToPlayer = math.atan2((self.x-ps.x), (self.y - ps.y))
            # directionToPlayer %= 2*math.pi
            # directionToPlayer = math.degrees(directionToPlayer)
            directionToPlayer = GW_utils.directionAtoB(self.x, self.y, ps.x, ps.y)
            off_x = -math.sin(directionToPlayer*GW_globals.DEG_TO_RAD)*self.get_width() + self.get_width()//2
            off_y = -math.cos(directionToPlayer*GW_globals.DEG_TO_RAD)*self.get_height() + self.get_height()//2
            projectiles.append(Laser(self.x+off_x, self.y+off_y, directionToPlayer))
            pygame.mixer.Sound.play(self.zap_sound)
            self.points = math.ceil(self.points*0.9)

class HeavySat(Satelite):
    def __init__(self, x, y, vx, vy, rot):
        super().__init__(x, y, vx, vy, rot)
        self.points = 500
        self.shield = True
        self.stateTimer = 0
        self.imageList = IL.HEAVY_SAT
        self.SHOT_RATE = 1200
    def die(self, ps):
        if self.shield:
            self.shield = False
        else:
            super().die(ps)
    def move(self, projectiles, ps, particles, dt):
        super().move(projectiles, ps, particles, dt)
        self.stateTimer = (self.stateTimer + dt) % 1000
    def draw(self, screen):
        if self.shield:
            GW_utils.blitRotateCenter(screen, self.imageList["with shield"][0 if self.stateTimer < 500 else 1], (self.x, self.y), self.rot)
        else:
            GW_utils.blitRotateCenter(screen, self.imageList["no shield"][0 if self.stateTimer < 500 else 1], (self.x, self.y), self.rot)

class EnemyShip(Enemy):
    def __init__(self, x, y, vx, vy, rot):
        super().__init__(x, y, vx, vy,  IL.OTHER_SHIP ,rot)
        self.points = 1000
        self.lastShot = 0
        self.zap_sound = SL.ENEMY_SHIP_SHOOT
        self.death_sound = SL.ENEMY_EXPLODE
        self.burn = False

    def move(self, projectiles, ps, particles, dt):
        self.fall()
        self.x += self.vx * dt/1000
        self.y += self.vy * dt/1000
        dist_from_planet = euc_dist(self.x, self.y, 0, 0)
        self.lastShot = self.lastShot + dt
        targetRot = 0

        #Set direction
        if dist_from_planet > 600:
            targetRot = GW_utils.directionAtoB(self.x, self.y, 0, 0)
            self.burn = True
        elif dist_from_planet > 150:
            targetRot = GW_utils.directionAtoB(self.x, self.y, ps.x, ps.y)
            self.burn = False
            if self.lastShot > 1000:
                self.lastShot = 0
                self.points = math.ceil(self.points*0.9)
                off_x = -math.sin(self.rot*GW_globals.DEG_TO_RAD)*self.get_width() + self.get_width()//2
                off_y = -math.cos(self.rot*GW_globals.DEG_TO_RAD)*self.get_height() + self.get_height()//2
                projectiles.append(Laser(self.x+off_x, self.y+off_y, self.rot))
                pygame.mixer.Sound.play(self.zap_sound)
        else:
            targetRot = GW_utils.directionAtoB(self.x, self.y, 0, 0)-90
            self.burn = True

        #Turn to face desired direction
        if targetRot < self.rot:
            self.rot -= GW_globals.TURN_SPEED*dt/1000
        else:
            self.rot += GW_globals.TURN_SPEED*dt/1000

        #Thrust if appropriate
        if (-20 < (self.rot-targetRot) < 20) and self.burn and euc_dist(self.vx, self.vy, 0, 0) < GW_globals.C:
             self.vx += GW_globals.THRUST * dt/1000
             off_x = 0.5*math.sin(self.rot * GW_globals.DEG_TO_RAD)*self.get_width() + self.get_width()/2
             off_y = 0.5*math.cos(self.rot * GW_globals.DEG_TO_RAD)*self.get_height() + self.get_height()/2
             par_rot = self.rot + random.randint(-10, 10)
             par_vx = math.sin(par_rot * GW_globals.DEG_TO_RAD)*GW_globals.C*0.5
             par_vy =  math.cos(par_rot * GW_globals.DEG_TO_RAD)*GW_globals.C*0.5
             particles.append(Particle(self.x+off_x, self.y+off_y, par_vx, par_vy))
