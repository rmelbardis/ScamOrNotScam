import pygame
from ScamOrNotScam.contestant import Contestant

class Questions:
    def __init__(self, display, gameStateManager, cont_1, cont_2, cont_3):
        self.display = display
        self.gameStateManager = gameStateManager
        self.cont_1 = cont_1
        self.cont_2 = cont_2
        self.cont_3 = cont_3

        self.logo = pygame.image.load("sprites/sons_logo.png").convert_alpha()
        self.logorect = self.logo.get_rect(topleft=(100, 150))

    def run(self):

        self.display.fill(color=(203, 230, 159))

        self.display.blit(self.logo, self.logorect)

        # draw contestants
        self.cont_1.draw_questions(self.display)
        self.cont_2.draw_questions(self.display)
        self.cont_3.draw_questions(self.display)
