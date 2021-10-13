import pygame
import os
import time
import random
import math
from Ship import Ship, Player, Rock
import GW_globals
from Planet import Planet


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

def check_collisions(ps, projectiles, planet, enemies):
    ship_rect = ps.icon.get_rect(center=(ps.x + ps.get_width()/2, ps.y+ps.get_height()/2))
    planet_rect = planet.icon.get_rect(center=(planet.x+planet.get_width()/2, planet.y+planet.get_height()/2))
    off_x = planet_rect.x - ship_rect.x
    off_y = planet_rect.y - ship_rect.y
    if ps.mask.overlap(planet.mask, (int(off_x), int(off_y))) != None:
        ps.dead = True
        print("Kaboom!")
    for p in projectiles:
        p_rect = ship_rect = p.icon.get_rect(center=(p.x + p.get_width()/2, p.y+p.get_height()/2))
        off_x = ship_rect.x - p_rect.x
        off_y = ship_rect.y - p_rect.y
        if p.mask.overlap(ps.mask, (int(off_x), int(off_y))) != None:
            ps.dead = True
            print("Zap!")
        for e in enemies:
            e_rect = ship_rect = ps.icon.get_rect(center=(e.x + e.get_width()/2, e.y+e.get_height()/2))
            off_x = e_rect.x - p_rect.x
            off_y = e_rect.y - p_rect.y
            if p.mask.overlap(e.mask, (int(off_x), int(off_y))) != None:
                e.dead = True
                print("Score!")

if __name__ == '__main__':

    #Setup and Initialize
    print('Launching Gravity Wars')
    pygame.init()
    pygame.display.set_caption('Gravity Wars')
    SCREEN = pygame.display.set_mode((GW_globals.WIDTH,GW_globals.HEIGHT))
    running = True
    main_font = pygame.font.SysFont('Courier 10', 50)

    level = 1

    #Load Images
    PLAYER_SHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship.png')), (20, 20))
    OTHER_SHIP = pygame.image.load(os.path.join('assets/imgs', 'crescent.png'))
    BG = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'background.png')), (GW_globals.WIDTH, GW_globals.HEIGHT))
    PLANET = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'planet.png')), (GW_globals.PLANET_SIZE, GW_globals.PLANET_SIZE))
    ROCK = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'rock.png')), (20, 20))
    game_label = main_font.render(f'Level {level}', 1, (255, 255, 255))
    static_images = [
        [BG, (0, 0)],
        [game_label, (GW_globals.WIDTH//2 - 100, GW_globals.HEIGHT//40)],
    ]

    player_ship = Player(GW_globals.WIDTH//4, GW_globals.WIDTH//4, 100, -100, PLAYER_SHIP)
    planet = Planet(PLANET)
    enemies = [
        Rock(600, random.randint(300, 500) ,40, 200, ROCK, 0)
    ]
    projectiles = []

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
            enemies = [
                Rock(600, random.randint(300, 500) ,40, 200, ROCK, 0),
                Rock(550, random.randint(300, 500),40, 200, ROCK, 0),
                Rock(500, random.randint(300, 500),40, 200, ROCK, 0)
            ]
            level += 1
            game_label = main_font.render(f'Level {level}', 1, (255, 255, 255))
            static_images = [
                [BG, (0, 0)],
                [game_label, (GW_globals.WIDTH//2 - 100, GW_globals.HEIGHT//40)],
            ]
        for p in projectiles:
            p.move(dt)
        for e in enemies:
            e.move(dt)
        check_collisions(player_ship, projectiles, planet, enemies)
        if player_ship.dead:
            running = False

    print('Explosions! Pew pew pew!')
