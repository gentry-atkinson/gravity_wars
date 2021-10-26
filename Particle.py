import random
import Image_Loader as IL
import GW_utils

class Particle:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.rot = 0
        self.icon = IL.PARTICLE
        self.dead = False
        self.spin = random.randint(0, 10)
        self.lifeSpan = random.randint(200, 500);

    def move(self, dt):
        self.x += self.vx * dt/1000
        self.y += self.vy * dt/1000
        self.rot += self.spin
        self.lifeSpan -= dt
        if self.lifeSpan <= 0:
            self.dead = True

    def draw(self, screen):
        GW_utils.blitRotateCenter(screen, self.icon, (self.x, self.y), self.rot)
