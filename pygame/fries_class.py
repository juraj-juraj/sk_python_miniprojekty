# Objekt, ktorý reprezentuje hranolky v hre
# Je to v podstate obalený pygame Rect, ktorý vie kde sú hranice hracej plochy a vie si sám meniť svoju polohu

import pygame
from random import randrange

FRIES_SIZE = (40, 40)

class fries_c:
    def __init__(self, x, y, arena_size) -> None:
        # Tento objekt vyuzǐvame aby sme zistili, či sa američan nenachádza presne tam, kde hranolky
        self.object = pygame.Rect(x, y, FRIES_SIZE[0], FRIES_SIZE[1])
        # Hranice hracej plochy
        self.min_x = arena_size[0]
        self.max_x = arena_size[1]
        self.min_y = arena_size[2]
        self.max_y = arena_size[3]

    
    # Náhodne premiestni hranolky inde na hracej ploche
    # Používa sa, keď Američan zožral hranolky aby sa premiestnili na novú pozíciu
    def reposition(self):
        self.object.x = randrange(self.min_x, self.max_x)
        self.object.y = randrange(self.min_y, self.max_y)
    
    def get_position(self):
        return (self.object.x, self.object.y)
