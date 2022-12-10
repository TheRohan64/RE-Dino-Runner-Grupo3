import pygame
import os

# Global Constants
TITLE = "Dino Run"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer.png")),
]

RUNNING_THUNDERBOLT = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Thunderbolt.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Thunderbolt.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_THUNDERBOLT = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpThunderbolt.png"))

DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead.png"))
DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

DUCKING_THUNDERBOLT = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Thunderbolt.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Thunderbolt.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD_RAY = [
    pygame.image.load(os.path.join(IMG_DIR, "Bad_cloud/CloudRay.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bad_cloud/CloudRay_2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
THUNDERBOLT = pygame.image.load(os.path.join(IMG_DIR, 'Other/thunderbolt.png'))
CAKE = pygame.image.load(os.path.join(IMG_DIR, "Other/Cake.png"))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))
RESET = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))
PAUSE = pygame.image.load(os.path.join(IMG_DIR, "Other/Pause.png"))
TROLL = pygame.image.load(os.path.join(IMG_DIR, "Other/Troll.png"))
CLICK = pygame.image.load(os.path.join(IMG_DIR, "Other/Click.png"))
POWER = pygame.image.load(os.path.join(IMG_DIR, "Other/Power.png"))
SANIC = pygame.image.load(os.path.join(IMG_DIR, "Other/Sanic.png"))
SUNKY = pygame.image.load(os.path.join(IMG_DIR, "Other/Sunky.png"))
THE_DIE = pygame.image.load(os.path.join(IMG_DIR, "Other/The_die.png"))
HYPNO = pygame.image.load(os.path.join(IMG_DIR, "Other/Hypno.gif"))
CONGRATULATIONS = pygame.image.load(os.path.join(IMG_DIR, "Other/Congratulations.png"))
MICKEY = pygame.image.load(os.path.join(IMG_DIR, "Other/Mickey.gif"))
EMOJI = pygame.image.load(os.path.join(IMG_DIR, "Other/Emoji.png"))
CRUSHED = pygame.image.load(os.path.join(IMG_DIR, "Other/Crushed.png"))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"

FONT_STYLE = "freesansbold.ttf"

SHIELD_TYPE = "shield"

HAMMER_TYPE = "hammer"

THUNDERBOLT_TYPE = "thunderbolt"