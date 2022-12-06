from pygame.sprite import Sprite
import pygame

from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VELOCITY = 6

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.y_pos_bg - 70 
        self.step_index = 0

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_velocity = self.JUMP_VELOCITY

    def update(self, user_input):

        if self.dino_run:
            self.run()

        elif self.dino_jump:
            self.jump()

        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False

        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True

        elif not (self.dino_jump or self.dino_duck):
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

        if self.step_index >= 8:
            self.step_index = 0

    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.6

        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_jump = False
            self.dino_rect.y = self.Y_POS
            self.jump_velocity = self.JUMP_VELOCITY

    def duck(self):
        self.image = DUCKING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        if self.step_index > 4:
            self.image = DUCKING[1]
        else:
            self.image = DUCKING[0]
        self.step_index += 1

    def run(self):
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        if self.step_index > 4:
            self.image = RUNNING[1]
        else:
            self.image = RUNNING[0]
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
 