from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = 260
        self.step_index = 0
        
    def draw(self, screen):
        if self.step_index > 4:
            self.type = 1
        else:
            self.type = 0
            
        if self.step_index == 9:
            self.step_index = 0
        screen.blit(self.images[self.type], self.rect)
        self.step_index += 1 