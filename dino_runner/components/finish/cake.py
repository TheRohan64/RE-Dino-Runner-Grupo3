from pygame.sprite import Sprite
from random import randint
from dino_runner.utils.constants import CAKE, SCREEN_WIDTH

class Cake(Sprite):
    def __init__(self):
        self.image = CAKE
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + randint (900, 1200)
        self.rect.y = 200

    def update(self, game_speed, cakes):
        self.rect.x -= game_speed
        if  self.rect.x < -self.rect.width:
            cakes.pop()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))