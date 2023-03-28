import pygame, controls
from gun import gun
from pygame.sprite import Group

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 500))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)
    Gun = Gun(screen)
    bullets = Group
    
    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, bullets)
        controls.update_bullets(bullets)

run()