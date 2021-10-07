import pygame
import os
import time
import random
import math

WIDTH, HEIGHT = 800, 800
FPS = 60
GRAVITY = 10
C = 10

def draw_screen(screen, static_images, ps):
    for i in static_images:
        screen.blit(i[0], i[1])
    ps.draw(screen)
    pygame.display.update()

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
        dist = euc_dist(self.x, self.y, WIDTH/2, HEIGHT/2)
        if self.x > WIDTH/2:
            self.vx -= GRAVITY/dist
        else:
            self.vx += GRAVITY/dist
        if self.y > HEIGHT/2:
            self.vy -= GRAVITY/dist
        else:
            self.vy += GRAVITY/dist

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
            self.vx -= .1
        if keys[pygame.K_RIGHT]:
            self.vx += .1

        if self.vx > C:
            self.vx = C
        elif self.vx < -C:
            self.vx = -C
        elif self.vy > C:
            self.vy = C
        elif self.vy < -C:
            self.vy = -C


if __name__ == '__main__':

    #Setup and Initialize
    print('Launching Gravity Wars')
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    running = True
    main_font = pygame.font.SysFont('Courier 10', 50)

    #Load Images
    PLAYER_SHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship.png')), (20, 20))
    OTHER_SHIP = pygame.image.load(os.path.join('assets/imgs', 'crescent_ship.png'))
    BG = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'background.png')), (WIDTH, HEIGHT))
    PLANET = pygame.image.load(os.path.join('assets/imgs', 'planet.png'))
    game_label = main_font.render('Gravity Wars', 1, (255, 255, 255))
    static_images = [
        [BG, (0, 0)],
        [game_label, (WIDTH//2 - 100, HEIGHT//40)],
        [PLANET, (WIDTH//2 - 30, HEIGHT//2 - 30)]
    ]

    player_ship = Player(WIDTH//4, WIDTH//4, 0, 0, PLAYER_SHIP)

    #Game Loop
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_screen(SCREEN, static_images, player_ship)
        keys = pygame.key.get_pressed()
        player_ship.move(keys)

    print('Explosions! Pew pew pew!')
