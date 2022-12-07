import random
from dino_runner.components.obstacles.obstacle import Obstacle

from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    Y_POS_BIRD = 260

    def __init__(self, images):
        self.type = BIRD[0]
        super().__init__(images, self.type)
        self.rect.y = self.Y_POS_BIRD
        self.step_index = 0

    def draw(self, screen):
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS_BIRD
        if self.step_index > 4:
            self.image = BIRD[1]
        else:
            self.image = BIRD[0]
        self.step_index += 1
