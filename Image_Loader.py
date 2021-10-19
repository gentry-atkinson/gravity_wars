import pygame
import os
import GW_globals

PLAYER_SHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship.png')), (30, 40))
OTHER_SHIP = pygame.image.load(os.path.join('assets/imgs', 'crescent.png'))
BG = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'background.png')), (GW_globals.WIDTH, GW_globals.HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'planet.png')), (GW_globals.PLANET_SIZE, GW_globals.PLANET_SIZE))
ROCK = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'rock.png')), (30, 30))
SAT = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'sat.png')), (30, 30))
LAS = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'shot.png')), (10, 10))
ALERT = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'alert.png')), (40, 40))
PLAYER_SHIP_BURN = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship_burning.png')), (30, 40))
SHIELD = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'shield.png')), (46, 58))
