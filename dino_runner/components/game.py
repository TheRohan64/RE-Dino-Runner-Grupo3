import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.score import Score
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, RUNNING, TITLE, FONT_STYLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.death_count = 0

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.player.reset_dinosaur()
        self.score.reset_score()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.screen.fill((64, 64, 255))
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        font = pygame.font.Font(FONT_STYLE, 30)
        if self.death_count == 0:
            text_component_1 = font.render("Press any key to play", True, (255, 255, 255)) 
            text_component_2 = font.render("Welcome to my game", True, (0, 0, 0))
            text_rect = text_component_2.get_rect()
            text_rect.center = (half_screen_width, half_screen_height - 50)
            self.screen.blit(text_component_2, text_rect)
        elif self.death_count > 0:
            text_component_1 = font.render("Press any key to replay", True, (0, 0, 0))
            font = pygame.font.Font(FONT_STYLE, 20)
            score = font.render(f"Points: {self.game_speed}", True, (0, 0, 0))
            score_rect = score.get_rect()
            score_rect.center = (half_screen_width, half_screen_height + 50)
            self.screen.blit(score, score_rect)
            font = pygame.font.Font(FONT_STYLE, 25)
            deaths = font.render(f"Deaths: {self.death_count}", True, (0, 0, 0))
            deaths_rect = deaths.get_rect()
            deaths_rect.center = (half_screen_width, half_screen_height - 50)
            self.screen.blit(deaths, deaths_rect)
        text_rect = text_component_1.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        self.screen.blit(text_component_1, text_rect)
        self.screen.blit(RUNNING[0], (half_screen_width - 35, half_screen_height + 140))
        pygame.display.update()
        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()