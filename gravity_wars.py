import pygame
import os
import time
import random
import math
from Ship import Ship, Player
import GW_globals
from Planet import Planet


def draw_screen(screen, static_images, ps, projectiles, planet):
    for i in static_images:
        screen.blit(i[0], i[1])
    ps.draw(screen)
    planet.draw(screen)
    for i in projectiles:
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

if __name__ == '__main__':

    #Setup and Initialize
    print('Launching Gravity Wars')
    pygame.init()
    SCREEN = pygame.display.set_mode((GW_globals.WIDTH,GW_globals.HEIGHT))
    running = True
    main_font = pygame.font.SysFont('Courier 10', 50)

    #Load Images
    PLAYER_SHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship.png')), (20, 20))
    OTHER_SHIP = pygame.image.load(os.path.join('assets/imgs', 'crescent.png'))
    BG = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'background.png')), (GW_globals.WIDTH, GW_globals.HEIGHT))
    PLANET = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'planet.png')), (GW_globals.PLANET_SIZE, GW_globals.PLANET_SIZE))
    game_label = main_font.render('Gravity Wars', 1, (255, 255, 255))
    static_images = [
        [BG, (0, 0)],
        [game_label, (GW_globals.WIDTH//2 - 100, GW_globals.HEIGHT//40)],
    ]

    player_ship = Player(GW_globals.WIDTH//4, GW_globals.WIDTH//4, 100, -100, PLAYER_SHIP)
    planet = Planet(PLANET)
    enemies = []
    projectiles = []

    #Game Loop
    clock = pygame.time.Clock()
    while running:
        clock.tick(GW_globals.FPS)
        dt = clock.get_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_screen(SCREEN, static_images, player_ship, projectiles, planet)
        keys = pygame.key.get_pressed()
        player_ship.move(keys, projectiles, dt)
        projectiles = [p for p in projectiles if not p.dead]
        for p in projectiles:
            p.move(dt)
        check_collisions(player_ship, projectiles, planet, enemies)
        if player_ship.dead:
            running = False

    print('Explosions! Pew pew pew!')
