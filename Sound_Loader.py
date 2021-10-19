import pygame
import os
import GW_globals

pygame.mixer.init()
pygame.mixer.music.load('assets/music/8bit-Dungeon01_loop.ogg')

PLAYER_SHOOT = pygame.mixer.Sound('assets/sounds/player_shoot.wav')
ENEMY_EXPLODE = pygame.mixer.Sound('assets/sounds/enemy_explode.wav')
ENEMY_SHIP_SHOOT = pygame.mixer.Sound('assets/sounds/enemy_ship_shoot.wav')
PLAYER_DIE = pygame.mixer.Sound('assets/sounds/player_die.wav')
PLAYER_SHIELD_DOWN = pygame.mixer.Sound('assets/sounds/player_shield_down.wav')
SAT_SHOOT = pygame.mixer.Sound('assets/sounds/sat_shoot.wav')

def music_on():
    pygame.mixer.music.play(-1)

def music_off():
    pygame.mixer.music.stop()
