from random import randint

from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH

class Cloud:
    def __init__(self):
        self.image = CLOUD
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + randint(600, 800)
        self.rect.y = randint(100, 180)
        
    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            self.rect.x = SCREEN_WIDTH + randint(2500, 3000)
            self.rect.y = randint(100, 180)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def reset_cloud(self):
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + randint(600, 800)
        self.rect.y = randint(100, 180)