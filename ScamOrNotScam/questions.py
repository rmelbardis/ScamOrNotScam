import pygame
from ScamOrNotScam.contestant import Contestant

class Questions:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        self.logo = pygame.image.load("sprites/sons_logo.png").convert_alpha()
        self.logorect = self.logo.get_rect(topleft=(100, 150))

    def run(self):

        self.display.fill(color=(203, 230, 159))

        self.display.blit(self.logo, self.logorect)
