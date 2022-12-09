import pygame
import random
from dino_runner.components.obstacles.cloud_ray import CloudRay
from dino_runner.components.obstacles.small_cactus import SmallCactus
from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import CLOUD_RAY, SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 3) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 3) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 3) == 2:
                self.obstacles.append(Bird(BIRD))
            elif random.randint(0, 3) == 3:
                self.obstacles.append(CloudRay(CLOUD_RAY))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.on_death():
                    self.obstacles.remove(obstacle)
                else:
                   game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []