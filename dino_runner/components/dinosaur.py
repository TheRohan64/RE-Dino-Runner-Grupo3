from pygame.sprite import Sprite
import pygame

from dino_runner.utils.constants import JUMPING, RUNNING
X_POS = 80
Y_POS = 310
JUMP_VELOCITY = 8
class Dinosaur(Sprite):
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0

        self.dino_run = True
        self.dino_jump = False
        self.jump_velocity = JUMP_VELOCITY

    def update(self, user_input):
        if self.dino_run:
            self.run()

        elif self.dino_jump:
            self.jump()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False

        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True

        if self.step_index >= 8:
            self.step_index = 0

    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8

        if self.jump_velocity < -JUMP_VELOCITY:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_velocity = JUMP_VELOCITY
        print(self.jump_velocity)

    def run(self):
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        if self.step_index > 4:
            self.image = RUNNING[1]
        else:
            self.image = RUNNING[0]
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
 