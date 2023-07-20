import pygame
from ScamOrNotScam.contestant import Contestant

class Questions:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # create contestants
        cont_1_img = pygame.image.load("sprites/cont_1.png").convert_alpha()
        self.cont_1 = Contestant(x = 1600, y = 60, unpressed_image=cont_1_img, pressed_image=cont_1_img, name='Anatol')
        cont_2_img = pygame.image.load("sprites/cont_2.png").convert_alpha()
        self.cont_2 = Contestant(x = 1600, y = 390, unpressed_image=cont_2_img, pressed_image=cont_2_img, name='C2')
        cont_3_img = pygame.image.load("sprites/cont_3.png").convert_alpha()
        self.cont_3 = Contestant(x = 1600, y = 720, unpressed_image=cont_3_img, pressed_image=cont_3_img, name='C3')

    def run(self):
        self.display.fill(color=(203, 230, 159))

        # draw contestants and switch to markets if pressed
        if self.cont_1.draw(self.display):
            self.gameStateManager.set_state('markets')
        if self.cont_2.draw(self.display):
            self.gameStateManager.set_state('markets')
        if self.cont_3.draw(self.display):
            self.gameStateManager.set_state('markets')

        # self.display.blit(self.cont_1.image, self.cont_1.rect)
        # self.display.blit(self.cont_1.name_text, self.cont_1.name_rect)
        # self.display.blit(self.cont_1.score_text, self.cont_1.score_rect)

        # self.display.blit(self.cont_2.image, self.cont_2.rect)
        # self.display.blit(self.cont_2.name_text, self.cont_2.name_rect)
        # self.display.blit(self.cont_2.score_text, self.cont_2.score_rect)

        # self.display.blit(self.cont_3.image, self.cont_3.rect)
        # self.display.blit(self.cont_3.name_text, self.cont_3.name_rect)
        # self.display.blit(self.cont_3.score_text, self.cont_3.score_rect)
