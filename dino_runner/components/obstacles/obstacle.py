from pygame.sprite import Sprite
from dino_runner.components import obstacles

class Obstacle(Sprite):
    def __init__(self, images, type):
        self.images = images
        self.type = type
        self.rect = self.images[self.type].get_rect()
        self.rect.x = 1100

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.images[self.type], self.rect)  
              