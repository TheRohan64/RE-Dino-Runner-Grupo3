import pygame
from dino_runner.components.cloud import Cloud

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.finish.cake_manager import CakeManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import BG, CLICK, CONGRATULATIONS, DEFAULT_TYPE, DINO_DEAD, EMOJI, HAMMER_TYPE, HYPNO, ICON, MICKEY, PAUSE, POWER, RESET, SANIC, SCREEN_HEIGHT, SCREEN_WIDTH, RUNNING, SHIELD_TYPE, SUNKY, THE_DIE, THUNDERBOLT_TYPE, TITLE, FONT_STYLE, FPS, TROLL

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
        self.power_up_manager = PowerUpManager()
        self.cloud = Cloud()
        self.cake_manager = CakeManager()
        self.paused = False
        self.finalized = False

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        #pygame.mixer.music.load("fnf_singularity_instrumental.wav")
        #pygame.mixer.music.play(-1)
        self.obstacle_manager.reset_obstacles()
        self.player.reset_dinosaur()
        self.cloud.reset_cloud()
        self.score.reset_score()
        self.power_up_manager.reset_power_ups()
        self.cake_manager.reset_cakes()
        self.game_speed = 20
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.show_menu_pause()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.cloud.update(self.game_speed)
        self.obstacle_manager.update(self)
        self.score.update(self)
        self.power_up_manager.update(self.game_speed, self.player, self.score.score)
        self.cake_manager.update(self.game_speed, self.player, self.score.score, self.show_menu_final)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.cloud.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.cake_manager.draw(self.screen)
        self.draw_power_up_activate()

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
        #pygame.mixer.music.load("fnf_memory_instrumental.wav")
        #pygame.mixer.music.play(-1)
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
            self.screen.blit(RUNNING[0], (half_screen_width - 35, half_screen_height + 110))
            self.screen.blit(SUNKY, (700, half_screen_height - 150))
        elif self.death_count > 0:
            text_component_1 = font.render("Press any key to replay", True, (0, 0, 0))
            font = pygame.font.Font(FONT_STYLE, 20)
            score = font.render(f"Points: {self.get_score}", True, (0, 0, 0))
            score_rect = score.get_rect()
            score_rect.center = (half_screen_width, half_screen_height + 50)
            self.screen.blit(score, score_rect)
            font = pygame.font.Font(FONT_STYLE, 25)
            deaths = font.render(f"Deaths: {self.death_count}", True, (0, 0, 0))
            deaths_rect = deaths.get_rect()
            deaths_rect.center = (half_screen_width, half_screen_height - 50)
            self.screen.blit(deaths, deaths_rect)
            self.screen.blit(DINO_DEAD, (half_screen_width - 35, half_screen_height + 110))
            self.screen.blit(RESET, (half_screen_width - 35, half_screen_height - 150))
            self.screen.blit(TROLL, (120, half_screen_height - 150))
            self.screen.blit(SANIC, (650, half_screen_height + 100))
            self.screen.blit(THE_DIE, (600, half_screen_height - 200))
            self.screen.blit(EMOJI, (750, 120))
        text_rect = text_component_1.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        self.screen.blit(text_component_1, text_rect)
        pygame.display.update()
        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu_pause(self):
        self.screen.fill((64, 64, 255))
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        font = pygame.font.Font(FONT_STYLE, 30)
        text_component = font.render("Press mouse to play", True, (255, 255, 255)) 
        text_rect = text_component.get_rect()
        text_rect.center = (half_screen_width, half_screen_height + 30)
        self.screen.blit(text_component, text_rect)
        self.screen.blit(PAUSE, (half_screen_width - 140, half_screen_height - 120))
        self.screen.blit(CLICK, (half_screen_width + 140, half_screen_height - 20))
        self.screen.blit(HYPNO, (120, 470))
        self.screen.blit(MICKEY, (800, 60))
        pygame.display.update()
        self.handle_key_events_on_menu_pause() 

    def handle_key_events_on_menu_pause(self):
        self.paused = True
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.paused = False
                    self.playing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.paused = False             

    def on_death(self):
        is_invencible = self.player.type == SHIELD_TYPE or self.player.type == HAMMER_TYPE or self.player.type == THUNDERBOLT_TYPE
        if not is_invencible:
            self.playing = False
            self.death_count += 1
        return is_invencible

    def draw_power_up_activate(self):
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())) / 1000
            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 25)
                power_up = font.render(f"Power up: {time_to_show}", True, (0, 0, 0))
                power_up_rect = power_up.get_rect()
                power_up_rect.center = (half_screen_width, half_screen_height + 130)
                self.screen.blit(power_up, power_up_rect)
                self.screen.blit(POWER, (half_screen_width - 300, half_screen_height + 130))
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def show_menu_final(self):
        self.screen.fill((64, 64, 255))
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        font = pygame.font.Font(FONT_STYLE, 30)
        text_component_1 = font.render("Press any key to replay", True, (0, 0, 0))
        text_rect = text_component_1.get_rect()
        text_rect.center = (half_screen_width, half_screen_height + 150)
        self.screen.blit(text_component_1, text_rect)
        font = pygame.font.Font(FONT_STYLE, 20)
        score = font.render(f"Points: {self.get_score}", True, (0, 0, 0))
        score_rect = score.get_rect()
        score_rect.center = (half_screen_width, half_screen_height + 200)
        self.screen.blit(score, score_rect)
        font = pygame.font.Font(FONT_STYLE, 25)
        deaths = font.render(f"Deaths: {self.death_count}", True, (0, 0, 0))
        deaths_rect = deaths.get_rect()
        deaths_rect.center = (half_screen_width, half_screen_height + 100)
        self.screen.blit(deaths, deaths_rect)
        self.screen.blit(CONGRATULATIONS, (90, 40))
        
        pygame.display.update()
        self.handle_key_events_on_menu_final()

    def handle_key_events_on_menu_final(self):
        self.finalized = True
        while self.finalized:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finalized = False
                    self.executing = False
                elif event.type == pygame.KEYDOWN:  
                    self.run()