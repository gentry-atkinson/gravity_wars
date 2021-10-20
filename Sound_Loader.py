import pygame
import os
import GW_globals

pygame.mixer.init()
pygame.mixer.music.load('assets/music/8bit-Dungeon01_loop.ogg')
pygame.mixer.music.set_volume(0.1)

path = os.path.join('assets', 'sounds')

PLAYER_SHOOT = pygame.mixer.Sound(os.path.join(path, 'player_shoot.wav'))
ENEMY_EXPLODE = pygame.mixer.Sound(os.path.join(path, 'enemy_explode.wav'))
ENEMY_SHIP_SHOOT = pygame.mixer.Sound(os.path.join(path, 'enemy_ship_shoot.wav'))
PLAYER_DIE = pygame.mixer.Sound(os.path.join(path, 'player_die.wav'))
PLAYER_SHIELD_DOWN = pygame.mixer.Sound(os.path.join(path, 'player_shield_down.wav'))
SAT_SHOOT = pygame.mixer.Sound(os.path.join(path, 'sat_shoot.wav'))

PLAYER_SHOOT.set_volume(0.3)
ENEMY_EXPLODE.set_volume(0.3)
ENEMY_SHIP_SHOOT.set_volume(0.3)
PLAYER_DIE.set_volume(0.3)
PLAYER_SHIELD_DOWN.set_volume(0.3)
SAT_SHOOT.set_volume(0.3)

def music_on():
    pygame.mixer.music.play(-1)

def music_off():
    pygame.mixer.music.stop()
