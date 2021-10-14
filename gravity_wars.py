import pygame
import os
import time
import random
import math
from Ship import Ship, Player, Rock, Satelite
import GW_globals
from Planet import Planet
import Image_Loader as IL
from GW_utils import check_collisions


def draw_screen(screen, static_images, ps, projectiles, planet, enemies):
    for i in static_images:
        screen.blit(i[0], i[1])
    ps.draw(screen)
    planet.draw(screen)
    for i in projectiles:
        i.draw(screen)
    for i in enemies:
        i.draw(screen)
    pygame.display.update()

if __name__ == '__main__':

    #Setup and Initialize
    print('Launching Gravity Wars')
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Gravity Wars')
    SCREEN = pygame.display.set_mode((GW_globals.WIDTH,GW_globals.HEIGHT))
    running = True
    main_font = pygame.font.SysFont('Courier 10', 50)

    level = 1

    pygame.mixer.music.load('assets/music/8-bit6-Dirty.ogg')
    #pygame.mixer.music.play(-1)

    #Load Images
    game_label = main_font.render(f'Level {level}', 1, (255, 255, 255))
    static_images = [
        [IL.BG, (0, 0)],
        [game_label, (GW_globals.WIDTH//2 - 100, GW_globals.HEIGHT//40)],
    ]

    player_ship = Player(GW_globals.WIDTH//4, GW_globals.WIDTH//4, 100, -100, IL.PLAYER_SHIP)
    planet = Planet(IL.PLANET)

    projectiles = []
    from Levels import lev_list
    enemies = lev_list[level-1]

    #Game Loop
    clock = pygame.time.Clock()


    while running:
        clock.tick(GW_globals.FPS)
        dt = clock.get_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_screen(SCREEN, static_images, player_ship, projectiles, planet, enemies)
        keys = pygame.key.get_pressed()
        player_ship.move(keys, projectiles, dt)
        projectiles = [p for p in projectiles if not p.dead]
        enemies = [e for e in enemies if not e.dead]
        if enemies == []:
            level += 1
            enemies = lev_list[level-1]
            game_label = main_font.render(f'Level {level}', 1, (255, 255, 255))
            static_images = [
                [IL.BG, (0, 0)],
                [game_label, (GW_globals.WIDTH//2 - 100, GW_globals.HEIGHT//40)],
            ]
        for e in enemies:
            e.move(projectiles, player_ship, dt)
        for p in projectiles:
            p.move(dt)
        check_collisions(player_ship, projectiles, planet, enemies)
        if player_ship.dead:
            running = False

    print('Explosions! Pew pew pew!')
