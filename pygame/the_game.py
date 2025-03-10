# Hra, kde Američan požiera hranoly
# Detom sa veľmi páčila. 
# Snažil som sa tam viac venovať OOP, bolo to vcelku náročné vysvetľovať

import pygame
import os
from fries_class import *
from stickman_class import *

pygame.font.init()

MAX_FPS = 35

WHITE = (255, 255, 255)
BLACK = ( 0,   0,   0)
BLUE =  ( 0,   0,  255)
RED =   (255,  0,   0)
GREEN = ( 0,  255,  0)
# Veľkosť okna hry v pixeloch
DISPLAY_SIZE = (900, 500)
GAMEPLAY_ARENA = (5, 895, 50, 450)
SPEED = 5
# Vytvorí okno hry v požadovanej veľkosti
window = pygame.display.set_mode(DISPLAY_SIZE)
# Nastaví titulok hry 
pygame.display.set_caption("my weird game")

#nacitanie obrazku zltej lode
# os.path.join zloží cestu k súboru nezávisle na operačnom systéme
STICKMAN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('obrazky', 'stickman.png')), STICKMAN_SIZE)
FRIES_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('obrazky', 'fries.png')), FRIES_SIZE)

# Podla stlačenej klávesy posunie objekt, v tomto prípada stickmana( Američana ) 
def move_object(object, key_pressed):
    if key_pressed[pygame.K_LEFT]:
        object.move_left(SPEED)

    if key_pressed[pygame.K_RIGHT]:
        object.move_right(SPEED)

    if key_pressed[pygame.K_UP]:
        object.move_up(SPEED)

    if key_pressed[pygame.K_DOWN]:
        object.move_down(SPEED)

# Zaisťuje čo sa stane po kolízii stickmana s hranolkami
def catch_fries(stickman, fries, score):
    if(stickman.object.colliderect(fries.object)):
        # Hranolky sa presunú na novú náhodnú pozíciu
        fries.reposition()
        return score + 1
    else:
        return score

def draw_window(stickman, fries, score):
    score_text = pygame.font.SysFont('comicsans', 40).render("Score: " + str(score), 1, BLACK)

    window.fill(WHITE)
    window.blit(STICKMAN_IMAGE, stickman.get_position())
    window.blit(FRIES_IMAGE, fries.get_position())
    window.blit(score_text, (350, 10))
    pygame.display.update()

def main():
    run = True
    # hodiny na zaistenie maximálnych fps
    clock = pygame.time.Clock()
    
    stickman = stickman_c(100, 100, GAMEPLAY_ARENA)
    fries = fries_c(500, 200, GAMEPLAY_ARENA)

    score = 0
    while run:
        clock.tick(MAX_FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False

        # zisti aké klávesy boli stlačené
        keys_pressed = pygame.key.get_pressed()
        # Na základe toho posuň stickmana
        move_object(stickman, keys_pressed)
        # Zisti, či nekoliduje stickman s hranolkami, ak áno príčitaj skóre a presuň hranolky na novú pozíciu
        score = catch_fries(stickman, fries, score)
        # Vykresli skóre, stickmana a hranolky
        draw_window(stickman, fries, score)
    pygame.quit()

if(__name__ == "__main__"):
    main()