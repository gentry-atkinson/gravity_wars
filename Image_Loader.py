import pygame
import os
import GW_globals

path = os.path.join('assets', 'imgs')

OTHER_SHIP = pygame.transform.scale(pygame.image.load(os.path.join(path, 'crescent.png')), (25, 25))
BG = pygame.transform.scale(pygame.image.load(os.path.join(path, 'background.png')), (GW_globals.WIDTH, GW_globals.HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load(os.path.join(path, 'planet.png')), (GW_globals.PLANET_SIZE, GW_globals.PLANET_SIZE))
ROCK = pygame.transform.scale(pygame.image.load(os.path.join(path, 'rock.png')), (30, 30))
SAT = pygame.transform.scale(pygame.image.load(os.path.join(path, 'sat.png')), (30, 30))
LAS = pygame.transform.scale(pygame.image.load(os.path.join(path, 'shot.png')), (10, 10))
ALERT = pygame.transform.scale(pygame.image.load(os.path.join(path, 'alert.png')), (40, 40))
SHIELD = pygame.transform.scale(pygame.image.load(os.path.join(path, 'shield.png')), (46, 58))
HEAVY_SAT = pygame.transform.scale(pygame.image.load(os.path.join(path, 'sat_heavy.png')), (30, 30))
PARTICLE = pygame.transform.scale(pygame.image.load(os.path.join(path, 'particle.png')), (3, 3))
ARROWS = pygame.transform.scale(pygame.image.load(os.path.join(path, 'arrows.png')), (150, 100))
SPACE = pygame.transform.scale(pygame.image.load(os.path.join(path, 'space_bar.png')), (200, 60))

PLAYER_SHIP = {
    "no shield no burn":  [
        pygame.transform.scale(pygame.image.load(os.path.join(path, 'player_ship_no_shield_1.png')), (50, 50)),
        pygame.transform.scale(pygame.image.load(os.path.join(path, 'player_ship_no_shield_1.png')), (50, 50))
    ],
    "with shield no burn": [
        pygame.transform.scale(pygame.image.load(os.path.join(path, 'player_ship_with_shield_1.png')), (50, 50)),
        pygame.transform.scale(pygame.image.load(os.path.join(path, 'player_ship_with_shield_2.png')), (50, 50))
    ],
    "no shield with burn": [
        pygame.transform.scale(pygame.image.load(os.path.join(path, 'player_ship_no_shield_burning_1.png')), (50, 50)),
        pygame.transform.scale(pygame.image.load(os.path.join(path, 'player_ship_no_shield_burning_2.png')), (50, 50))
    ],
    "with shield with burn": [
        pygame.transform.scale(pygame.image.load(os.path.join(path, 'player_ship_with_shield_burning_1.png')), (50, 50)),
        pygame.transform.scale(pygame.image.load(os.path.join(path, 'player_ship_with_shield_burning_2.png')), (50, 50))
    ]
}

HEAVY_SAT = {
    "no shield":  [
        pygame.transform.scale(pygame.image.load(os.path.join(path, 'sat_heavy_no_shield_1.png')), (50, 50)),
        pygame.transform.scale(pygame.image.load(os.path.join(path, 'sat_heavy_no_shield_1.png')), (50, 50))
    ],
    "with shield": [
        pygame.transform.scale(pygame.image.load(os.path.join(path, 'sat_heavy_with_shield_1.png')), (50, 50)),
        pygame.transform.scale(pygame.image.load(os.path.join(path, 'sat_heavy_with_shield_2.png')), (50, 50))
    ]
}
