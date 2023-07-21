import pygame
from ScamOrNotScam.button import Button
from ScamOrNotScam.spinner import Spinner

class Markets:
    def __init__(self, display, gameStateManager, cont_1, cont_2, cont_3):
        self.display = display
        self.gameStateManager = gameStateManager
        self.cont_1 = cont_1
        self.cont_2 = cont_2
        self.cont_3 = cont_3

        vol_button_image = pygame.image.load("sprites/volatility.png").convert_alpha()
        vol_button_pressed = pygame.image.load("sprites/volatility_pressed.png").convert_alpha()
        self.vol_button = Button(x=1000, y=400, unpressed_image=vol_button_image, pressed_image=vol_button_pressed)

        self.pin = pygame.image.load("sprites/pin.png").convert_alpha()
        self.pinrect = self.pin.get_rect(topleft=(411, 15))

        spinner_image = pygame.image.load("sprites/the_markets.png").convert_alpha()
        self.spinner = Spinner(x=100, y=150, spinner_image=spinner_image, display=self.display)

    def run(self):

        self.display.fill(color=(254, 150, 183))

        # blitting
        self.display.blit(self.spinner.image, self.spinner.rect)
        self.display.blit(self.spinner.textimg, self.spinner.textrect)
        self.display.blit(self.pin, self.pinrect)

        if self.vol_button.draw(self.display):
            self.spinner.spinning = True
        self.spinner.update()

        # draw contestants
        self.cont_1.draw_markets(self.display)
        self.cont_2.draw_markets(self.display)
        self.cont_3.draw_markets(self.display)
