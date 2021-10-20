import pygame
import os
import GW_globals

OTHER_SHIP = pygame.image.load(os.path.join('assets/imgs', 'crescent.png'))
BG = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'background.png')), (GW_globals.WIDTH, GW_globals.HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'planet.png')), (GW_globals.PLANET_SIZE, GW_globals.PLANET_SIZE))
ROCK = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'rock.png')), (30, 30))
SAT = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'sat.png')), (30, 30))
LAS = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'shot.png')), (10, 10))
ALERT = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'alert.png')), (40, 40))
SHIELD = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'shield.png')), (46, 58))
HEAVY_SAT = pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'sat_heavy.png')), (30, 30))

PLAYER_SHIP = {
    "no shield no burn":  [
        pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship_no_shield_1.png')), (50, 50)),
        pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship_no_shield_1.png')), (50, 50))
    ],
    "with shield no burn": [
        pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship_with_shield_1.png')), (50, 50)),
        pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship_with_shield_2.png')), (50, 50))
    ],
    "no shield with burn": [
        pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship_no_shield_burning_1.png')), (50, 50)),
        pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship_no_shield_burning_2.png')), (50, 50))
    ],
    "with shield with burn": [
        pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship_with_shield_burning_1.png')), (50, 50)),
        pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'player_ship_with_shield_burning_2.png')), (50, 50))
    ]
}

HEAVY_SAT = {
    "no shield":  [
        pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'sat_heavy_no_shield_1.png')), (50, 50)),
        pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'sat_heavy_no_shield_1.png')), (50, 50))
    ],
    "with shield": [
        pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'sat_heavy_with_shield_1.png')), (50, 50)),
        pygame.transform.scale(pygame.image.load(os.path.join('assets/imgs', 'sat_heavy_with_shield_2.png')), (50, 50))
    ]
}
