from dino_runner.components.obstacles.obstacle import Obstacle


class CloudRay(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = 150