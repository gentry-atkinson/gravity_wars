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
    for i in static_images.values():
        if i != []:
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
    #main_font = pygame.font.SysFont('Courier 10', 50)
    main_font = pygame.font.Font('assets/font/Baskic8.otf', 50)

    level = 1
    drift_timer = 0

    pygame.mixer.music.load('assets/music/8-bit6-Dirty.ogg')
    pygame.mixer.music.play(-1)

    #Load Images

    player_ship = Player(GW_globals.WIDTH//4, GW_globals.WIDTH//4, 100, -100)
    planet = Planet(IL.PLANET)
    game_label = main_font.render(f'Level {level}', 1, (255, 255, 255))
    score_label = main_font.render('Score: 0', 1, (255, 255, 255))
    static_images = {
        'BG': [IL.BG, (0, 0)],
        'LEVEL': [game_label, (GW_globals.WIDTH//2 - 120, GW_globals.HEIGHT//40)],
        'SCORE': [score_label,(GW_globals.WIDTH//2 - 120, GW_globals.HEIGHT - 100)]
    }

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
                #pygame.quit()
        draw_screen(SCREEN, static_images, player_ship, projectiles, planet, enemies)
        keys = pygame.key.get_pressed()
        player_ship.move(keys, projectiles, dt)
        projectiles = [p for p in projectiles if not p.dead]
        enemies = [e for e in enemies if not e.dead]
        score_label = main_font.render(f'Score: {player_ship.score}', 1, (255, 255, 255))
        static_images['SCORE'][0] = score_label
        if player_ship.drift:
            static_images['ALERT'] = [IL.ALERT, (10, GW_globals.HEIGHT*0.9)]
            drift_timer += dt
            drift_label = main_font.render(f'{drift_timer//1000}', 1, (255, 255, 255))
            static_images['DRIFT_LABEL'] = [drift_label, (60, GW_globals.HEIGHT*0.9)]
            if drift_timer > 3000:
                player_ship.dead = True
        else:
            drift_timer = 0
            static_images['ALERT'] = []
            static_images['DRIFT_LABEL'] = []
        if enemies == []:
            level += 1
            if level > len(lev_list):
                running = False
                break
            enemies = lev_list[level-1]
            game_label = main_font.render(f'Level {level}', 1, (255, 255, 255))
            static_images['LEVEL'][0] = game_label
        for e in enemies:
            e.move(projectiles, player_ship, dt)
        for p in projectiles:
            p.move(dt)
        check_collisions(player_ship, projectiles, planet, enemies)
        if player_ship.dead:
            running = False

    death_screen = True
    pygame.mixer.music.stop()

    high_score = 0
    with open('high_score.txt', 'r') as score_file:
        high_score = int(score_file.readline().strip())

    if player_ship.score > high_score:
            high_score = player_ship.score
            with open('high_score.txt', 'w') as score_file:
                score_file.write(str(high_score))

    score_label = main_font.render(f'Final Score: {player_ship.score}', 1, (255, 255, 255))
    high_label = main_font.render(f'High Score: {high_score}', 1, (255, 255, 255))
    game_label = main_font.render('You Have {}'.format('Won' if level > len(lev_list) else 'Died'), 1, (255, 255, 255))
    static_images['LEVEL'][0] = game_label
    static_images['SCORE'][0] = score_label
    static_images['HIGH'] = [high_label, (GW_globals.WIDTH//2 - 120, GW_globals.HEIGHT * 0.7)]
    draw_screen(SCREEN, static_images, player_ship, projectiles, planet, enemies)
    pygame.time.wait(500)



    while death_screen:
        clock.tick(GW_globals.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                death_screen = False
        keys = pygame.key.get_pressed()
        if sum(keys) != 0: death_screen = False
    #
    # print('Explosions! Pew pew pew! Final score: ', player_ship.score)
