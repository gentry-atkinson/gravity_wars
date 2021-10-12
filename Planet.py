import GW_utils
import GW_globals
import pygame
import os
import math


class Planet:
    def __init__(self,icon):
        self.x = GW_globals.WIDTH//2 - GW_globals.PLANET_SIZE//2
        self.y = GW_globals.HEIGHT//2 - GW_globals.PLANET_SIZE//2
        self.icon = icon
        self.mask = pygame.mask.from_surface(self.icon)
    def draw(self, screen):
        screen.blit(self.icon, (self.x, self.y))
    def get_width(self):
        return self.icon.get_width()
    def get_height(self):
        return self.icon.get_height()
