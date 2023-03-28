import pygame, controls
from gun import gun

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 500))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)
    Gun = Gun(screen)
    
    while True:
        controls.events(gun)
        gun.update_gun()
       controls.update(bg_color, screen, gun)

run()