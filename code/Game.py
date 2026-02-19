import pygame

from code.Menu import Menu
from code.Const import *

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIND_HEIGHT))

    def run (self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


