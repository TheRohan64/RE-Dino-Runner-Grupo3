from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING

class Dinosaur(Sprite):
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 60
        self.dino_rect.y = 310
        self.step_index = 0

    def update(self):
        if self.step_index > 4:
            self.image = RUNNING[1]
        else:
            self.image = RUNNING[0]
        self.step_index += 1

        if self.step_index >= 8:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
 