# Stickman, postavička hráča
# Pohybuje sa po hracej ploche a požiera hranolky
import pygame

#rozmer je (sirka, vyska) v pixeloch
STICKMAN_SIZE = (100, 100)

class stickman_c:
    def __init__(self, x, y, arena_size) -> None:
        # Objekt sa používa na zistenie, či sa hráč nachádza presne tam, kde sú hranolky
        self.object = pygame.Rect(x, y, STICKMAN_SIZE[0], STICKMAN_SIZE[1])
        # Hranice kde sa môže pohybovať
        self.min_x = arena_size[0]
        self.max_x = arena_size[1]
        self.min_y = arena_size[2]
        self.max_y = arena_size[3]

    # Metódy ktoré pohybujú hráča po hracej ploche
    # Rešpektuje to hranice hracej plochy, ale vie sa pohybovať kúsok za hranicami hracej plochy( je to tak naschvál pre zjednodušenie)
    # Tieto metódy sa volaj́ú v hlavnej aplikácii, podľa kláves
    def move_up(self, steps):
        self.object.y -= steps
        if(self.object.y < self.min_y):
            self.object.y = self.min_y 
    
    def move_down(self, steps):    
        self.object.y += steps
        if(self.object.y > self.max_y):
            self.object.y = self.max_y 

    def move_right(self, steps):    
        self.object.x += steps
        if(self.object.x > self.max_x):
            self.object.x = self.max_x 

    def move_left(self, steps):    
        self.object.x -= steps
        if(self.object.x < self.min_x):
            self.object.x = self.min_x 
    
    # Nakoniec sa vykreslí obrázok stickmana tam kde sa nachádza
    def get_position(self):
        return (self.object.x, self.object.y)
    

