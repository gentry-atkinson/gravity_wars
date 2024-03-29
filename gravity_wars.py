import pygame
import os
import time
import random
import math
from Ship import Ship, Player, Rock, Satelite
import GW_globals
from Planet import Planet
import Image_Loader as IL
import Sound_Loader as SL
from GW_utils import check_collisions


def draw_screen(screen, static_images, ps, projectiles, planet, enemies, particles):
    for i in static_images.values():
        if i != []:
            screen.blit(i[0], i[1])
    if planet:
        planet.draw(screen)
    if enemies:
        for e in enemies:
            e.draw(screen)
    if ps:
        ps.draw(screen)
    if projectiles:
        for p in projectiles:
            p.draw(screen)
    if particles:
        for p in particles:
            p.draw(screen)

    pygame.display.update()

if __name__ == '__main__':

    #Setup and Initialize
    #print('Launching Defender of Zyrth!')
    pygame.init()
    pygame.display.set_caption('Gravity Wars')
    SCREEN = pygame.display.set_mode((GW_globals.WIDTH,GW_globals.HEIGHT))
    running = True
    main_font = pygame.font.Font('assets/font/Baskic8.otf', 50)

    #Initialize game variables
    level = 0
    drift_timer = 0
    screen_changed = True
    player_ship = None
    planet = None
    enemies = None
    particles = None


    projectiles = []
    from Levels import lev_list
    gameState = "title"

    #Game Loop
    clock = pygame.time.Clock()
    while running:
        clock.tick(GW_globals.FPS)
        dt = clock.get_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                #pygame.quit()
        keys = pygame.key.get_pressed()

        if gameState == "title":
            if screen_changed:
                title_lable = main_font.render('Defender of Zyrth!', 1, (255, 255, 255))
                key_lable = main_font.render('Press Any Key...', 1, (255, 255, 255))
                static_images = {
                    'BG': [IL.BG, (0, 0)],
                    'TITLE':[title_lable, (GW_globals.WIDTH//2 - 190, GW_globals.HEIGHT//6)],
                    'KEY': [key_lable, (GW_globals.WIDTH//2 - 150, GW_globals.HEIGHT*0.8)],
                    'ARROWS': [IL.ARROWS, (GW_globals.WIDTH *0.7, GW_globals.HEIGHT//2)],
                    'SPACE':[IL.SPACE, (GW_globals.WIDTH//2 *0.2, GW_globals.HEIGHT//2+40)]
                }
                static_images['HIGH'] = []
                screen_changed = False
            else:
                pygame.time.wait(10)
            if sum(keys) != 0:
                gameState = "play"
                level = 0
                screen_changed = True


        elif gameState == "play":
            if screen_changed:
                level = 1
                game_label = main_font.render(f'Level {level}', 1, (255, 255, 255))
                score_label = main_font.render('Score: 0', 1, (255, 255, 255))
                static_images['LEVEL'] = [game_label, (GW_globals.WIDTH//2 - 120, GW_globals.HEIGHT//40)]
                static_images['SCORE'] = [score_label,(GW_globals.WIDTH//2 - 120, GW_globals.HEIGHT - 100)]
                static_images['ARROWS'] = []
                static_images['SPACE'] = []
                static_images['TITLE'] = []
                static_images['KEY'] = []
                static_images['HIGH'] = []
                static_images['DRIFT_LABEL'] = []
                SL.music_on()
                player_ship = Player(GW_globals.WIDTH//4, GW_globals.WIDTH//4, 100, -100, 280)
                planet = Planet(IL.PLANET)
                enemies = lev_list[level-1].copy()
                particles = []
                screen_changed = False
            player_ship.move(keys, projectiles, particles, dt)
            score_label = main_font.render(f'Score: {player_ship.score}', 1, (255, 255, 255))
            static_images['SCORE'][0] = score_label
            if player_ship.drift:
                static_images['ALERT'] = [IL.ALERT, (10, GW_globals.HEIGHT*0.9)]
                drift_timer += dt
                drift_label = main_font.render(f'{3 - drift_timer//1000}', 1, (255, 255, 255))
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
                    player_ship.dead = True
                else:
                    enemies = lev_list[level-1].copy()
                game_label = main_font.render(f'Level {level}', 1, (255, 255, 255))
                static_images['LEVEL'][0] = game_label
                projectiles = []
                gameState = 'load'
                continue
            for e in enemies:
                e.move(projectiles, player_ship, particles, dt)
            for p in projectiles:
                p.move(dt)
            for p in particles:
                p.move(dt)
            check_collisions(player_ship, projectiles, planet, enemies, particles)
            # for e in enemies:
            #     print(type(e), '\t', e.dead)
            enemies = [e for e in enemies if not e.dead]
            projectiles = [p for p in projectiles if not p.dead]
            particles = [p for p in particles if not p.dead]
            if player_ship.dead:
                gameState = 'death'
                screen_changed = True
                pygame.mixer.Sound.play(player_ship.death_sound)
        #End Play State
        elif gameState == 'load':
            title_lable = main_font.render('A New Wave Approaches...', 1, (255, 255, 255))
            static_images['LEVEL'] = []
            static_images['SCORE'] = []
            static_images['TITLE'] = [title_lable, (100, GW_globals.HEIGHT*0.8)]
            static_images['DRIFT_LABEL'] = []
            player_ship.x = GW_globals.WIDTH//4
            player_ship.y =  GW_globals.HEIGHT//4
            player_ship.vx = 100
            player_ship.vy = -100
            player_ship.rot = 280
            player_ship.shield = True
            draw_screen(SCREEN, static_images, None, None, planet, None, None)
            pygame.time.wait(1000)
            static_images['LEVEL'] = [game_label, (GW_globals.WIDTH//2 - 120, GW_globals.HEIGHT//40)]
            static_images['SCORE'] = [score_label,(GW_globals.WIDTH//2 - 120, GW_globals.HEIGHT - 100)]
            static_images['TITLE'] = []
            gameState = 'play'
            continue
        #End Load State
        elif gameState == 'death':
            if screen_changed:
                SL.music_off()

                high_score = 0
                with open('high_score.txt', 'r') as score_file:
                    high_score = int(score_file.readline().strip())

                if player_ship.score > high_score:
                        high_score = player_ship.score
                        with open('high_score.txt', 'w') as score_file:
                            score_file.write(str(high_score))

                score_label = main_font.render(f'Final Score:  {player_ship.score}', 1, (255, 255, 255))
                high_label =  main_font.render(f'High Score:   {high_score}', 1, (255, 255, 255))
                if level > len(lev_list):
                    game_label = main_font.render('You Have Defended Zyrth!', 1, (255, 255, 255))
                else:
                    game_label = main_font.render('You Have Died on Level {}'.format(level), 1, (255, 255, 255))
                static_images['LEVEL'] = [game_label, (20, GW_globals.HEIGHT * 0.1)]
                static_images['SCORE'] = [score_label, (20, GW_globals.HEIGHT * 0.5)]
                static_images['HIGH'] = [high_label, (20, GW_globals.HEIGHT * 0.7)]
                static_images['DRIFT_LABEL'] = []
                static_images['ALERT'] = []
                level = 0
                drift_timer = 0
                screen_changed = True
                player_ship = None
                planet = None
                enemies = None
                particles = None
                projectiles = None
                screen_changed = False
                draw_screen(SCREEN, static_images, player_ship, projectiles, planet, enemies, particles)
                keys = []
                pygame.time.wait(500)
            else:
                pygame.time.wait(10)
            if sum(keys) != 0:
                running = False
        #End Death State
        draw_screen(SCREEN, static_images, player_ship, projectiles, planet, enemies, particles)
    #End Game Loop
#End Main Function
