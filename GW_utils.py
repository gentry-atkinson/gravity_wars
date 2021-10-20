import pygame
import math

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
    return rotated_image, new_rect

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect)

def directionAtoB(ax, ay, bx, by):
    direction = math.atan2((ax-bx), (ay - by))
    direction %= 2*math.pi
    return math.degrees(direction)

def check_collisions(ps, projectiles, planet, enemies):
    #Did player hit planet
    ship_rect = ps.icon.get_rect(center=(ps.x + ps.get_width()//2, ps.y+ps.get_height()//2))
    planet_rect = \
        planet.icon.get_rect(center=(planet.x+planet.get_width()//2, planet.y+planet.get_height()//2))
    off_x = planet_rect.x - ship_rect.x
    off_y = planet_rect.y - ship_rect.y
    if ps.mask.overlap(planet.mask, (int(off_x), int(off_y))) != None:
        ps.dead = True
        #print("Kaboom!")

    #Did a bullet hit anyone
    for p in projectiles:
        p_rect = p.icon.get_rect(center=(p.x + p.get_width()//2, p.y+p.get_height()//2))
        off_x = ship_rect.x - p_rect.x
        off_y = ship_rect.y - p_rect.y
        if p.mask.overlap(ps.mask, (int(off_x), int(off_y))) != None:
            if ps.shield:
                #print("Shield Down!")
                pygame.mixer.Sound.play(ps.shield_sound)
                ps.shield = False
                p.dead = True
            else:
                ps.dead = True
                #print("Zap!")
        for e in enemies:
            e_rect = e.icon.get_rect(center=(e.x + e.get_width()//2, e.y+e.get_height()//2))
            off_x = e_rect.x - p_rect.x
            off_y = e_rect.y - p_rect.y
            if p.mask.overlap(e.mask, (int(off_x), int(off_y))) != None:
                e.die(ps)
                p.dead = True
                #print("Score!")

    #Did a player crash into an enemy
    for e in enemies:
        e_rect = e.icon.get_rect(center=(e.x + e.get_width()//2, e.y+e.get_height()//2))
        off_x = e_rect.x - ship_rect.x
        off_y = e_rect.y - ship_rect.y
        if ps.mask.overlap(e.mask, (int(off_x), int(off_y))) != None:
            e.die(ps)
            ps.dead = True
            #print("Wrecked!")
