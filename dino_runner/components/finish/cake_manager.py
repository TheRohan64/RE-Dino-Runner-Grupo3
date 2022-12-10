from dino_runner.components.finish.cake import Cake

class CakeManager():
    def __init__(self):
        self.cakes = []
        self.when_appears = 0

    def generate_cake(self, score):
        self.when_appears = score
        if len(self.cakes) == 0 and self.when_appears == 300:
            self.cakes.append(Cake())
        
    def update(self, game_speed, player, score):
        self.generate_cake(score)
        for cake in self.cakes:
            cake.update(game_speed, self.cakes)
            if player.dino_rect.colliderect(cake.rect):
                self.cakes.remove(cake)

    def draw(self, screen):
        for cake in self.cakes:
            cake.draw(screen)

    def reset_cakes(self):
        self.cakes = []
        self.when_appears = 0