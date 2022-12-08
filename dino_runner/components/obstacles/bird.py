from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH

class Bird(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = 260
        self.step_index = 0
        
    def draw(self, screen):
        if self.step_index >= 8:
            self.step_index = 0
        screen.blit(self.images[self.step_index // 4], self.rect)
        self.step_index += 1 