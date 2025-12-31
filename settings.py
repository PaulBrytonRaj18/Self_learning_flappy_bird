import pygame
import os

# Initialize font/display modules for loading
pygame.font.init()

# Constants
WIN_WIDTH = 500
WIN_HEIGHT = 800
STAT_FONT = pygame.font.SysFont("comicsans", 50)

# Load Assets Function
def load_asset(name):
    return pygame.transform.scale2x(pygame.image.load(os.path.join("assets", name)))

# Load Images
BIRD_IMGS = [load_asset("bird1.png"), load_asset("bird2.png"), load_asset("bird3.png")]
PIPE_IMG = load_asset("pipe.png")
BASE_IMG = load_asset("base.png")
BG_IMG = load_asset("bg.png")