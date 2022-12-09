from pygame.sprite import Sprite
import pygame

from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING_HAMMER, DUCKING_SHIELD, DUCKING_THUNDERBOLT, HAMMER_TYPE, JUMPING, JUMPING_HAMMER, JUMPING_SHIELD, JUMPING_THUNDERBOLT, RUNNING, DUCKING, RUNNING_HAMMER, RUNNING_SHIELD, RUNNING_THUNDERBOLT, SHIELD_TYPE, THUNDERBOLT_TYPE 

RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, THUNDERBOLT_TYPE: RUNNING_THUNDERBOLT}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, THUNDERBOLT_TYPE: JUMPING_THUNDERBOLT}
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, THUNDERBOLT_TYPE: DUCKING_THUNDERBOLT}

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCKING = 340
    JUMP_VELOCITY = 8

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS 
        self.step_index = 0

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_velocity = self.JUMP_VELOCITY
        self.has_power_up = False
        self.power_up_time_up = 0

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
        self.image = JUMP_IMG[self.type]
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8

        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_jump = False
            self.dino_rect.y = self.Y_POS
            self.jump_velocity = self.JUMP_VELOCITY

    def duck(self):
        self.image = DUCK_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCKING
        if self.step_index > 4:
            self.image = DUCK_IMG[self.type][1]
        else:
            self.image = DUCK_IMG[self.type][0]
        self.step_index += 1

    def run(self):
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        if self.step_index > 4:
            self.image = RUN_IMG[self.type][1]
        else:
            self.image = RUN_IMG[self.type][0]
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
 
    def reset_dinosaur(self):
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS 
        self.step_index = 0

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_velocity = self.JUMP_VELOCITY
        self.has_power_up = False
        self.power_up_time_up = 0

    def on_pick_power_up(self, start_time, duration, type):
        self.has_power_up = True
        self.power_up_time_up = start_time + (duration * 1000)
        self.type = type