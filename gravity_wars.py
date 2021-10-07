import pygame
import os
import time
import random
import math
from Ship import Ship, Player
import GW_globals


def draw_screen(screen, static_images, ps):
    for i in static_images:
        screen.blit(i[0], i[1])
    ps.draw(screen)
    pygame.display.update()

if __name__ == '__main__':

    #Setup and Initialize
    print('Launching Gravity Wars')
    pygame.init()
    SCREEN = pygame.display.set_mode((GW_globals.WIDTH,GW_globals.HEIGHT))
    running = True
    main_font = pygame.font.SysFont('Courier 10', 50)

    #Load Images
    PLAYER_SHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship.png')), (20, 20))
    OTHER_SHIP = pygame.image.load(os.path.join('assets/imgs', 'crescent_ship.png'))
    BG = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'background.png')), (GW_globals.WIDTH, GW_globals.HEIGHT))
    PLANET = pygame.image.load(os.path.join('assets/imgs', 'planet.png'))
    game_label = main_font.render('Gravity Wars', 1, (255, 255, 255))
    static_images = [
        [BG, (0, 0)],
        [game_label, (GW_globals.WIDTH//2 - 100, GW_globals.HEIGHT//40)],
        [PLANET, (GW_globals.WIDTH//2 - 30, GW_globals.HEIGHT//2 - 30)]
    ]

    player_ship = Player(GW_globals.WIDTH//4, GW_globals.WIDTH//4, 0, 0, PLAYER_SHIP)

    #Game Loop
    clock = pygame.time.Clock()
    while running:
        clock.tick(GW_globals.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_screen(SCREEN, static_images, player_ship)
        keys = pygame.key.get_pressed()
        player_ship.move(keys)

    print('Explosions! Pew pew pew!')
