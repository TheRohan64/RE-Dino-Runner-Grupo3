import pygame
import random
from dino_runner.components.obstacles import cactus, bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append[cactus(SMALL_CACTUS)]
            elif random.randint(0, 2) == 1:
                self.obstacles.append[cactus(LARGE_CACTUS)]
            elif random.randint(0, 2) == 2:
                self.obstacles.append[bird(BIRD)]

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []