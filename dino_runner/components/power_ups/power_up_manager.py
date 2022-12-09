import random

import pygame
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.thunderbolt import Thunderbolt

class PowerUpManager():
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        self.when_appears = score
        if len(self.power_ups) == 0 and (self.when_appears % 300) == 0:
            if random.randint(0, 2) == 0:
                self.power_ups.append(Shield())
            elif random.randint(0, 2) == 1:
                self.power_ups.append(Hammer())
            elif random.randint(0, 2) == 2:
                self.power_ups.append(Thunderbolt())             

    def update(self, game_speed, player, score):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.on_pick_power_up(power_up.start_time, power_up.duration, power_up.type)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = 0