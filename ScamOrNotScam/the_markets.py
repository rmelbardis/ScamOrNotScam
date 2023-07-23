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
        self.active_cont = self.cont_1

        vol_button_image = pygame.image.load("sprites/volatility.png").convert_alpha()
        vol_button_pressed = pygame.image.load("sprites/volatility_pressed.png").convert_alpha()
        self.vol_button = Button(x=1000, y=400, unpressed_image=vol_button_image, pressed_image=vol_button_pressed)

        self.pin = pygame.image.load("sprites/pin.png").convert_alpha()
        self.pinrect = self.pin.get_rect(topleft=(411, 15))

        self.spinner_image = pygame.image.load("sprites/the_markets.png").convert_alpha()
        self.spinner = Spinner(x=100, y=150, spinner_image=self.spinner_image,
                               display=self.display, contestant=self.active_cont)

    def run(self):

        self.display.fill(color=(254, 150, 183))

        # draw contestants & allow selection
        if self.cont_1.draw_markets(self.display):
            self.active_cont = self.cont_1
            self.cont_1.selected = True
            self.cont_2.selected = False
            self.cont_3.selected = False
            # create spinner for active contestant
            self.spinner = Spinner(x=100, y=150, spinner_image=self.spinner_image,
                               display=self.display, contestant=self.active_cont)

        if self.cont_2.draw_markets(self.display):
            self.active_cont = self.cont_2
            self.cont_1.selected = False
            self.cont_2.selected = True
            self.cont_3.selected = False
            # create spinner for active contestant
            self.spinner = Spinner(x=100, y=150, spinner_image=self.spinner_image,
                               display=self.display, contestant=self.active_cont)

        if self.cont_3.draw_markets(self.display):
            self.active_cont = self.cont_3
            self.cont_1.selected = False
            self.cont_2.selected = False
            self.cont_3.selected = True
            # create spinner for active contestant
            self.spinner = Spinner(x=100, y=150, spinner_image=self.spinner_image,
                               display=self.display, contestant=self.active_cont)

        # blitting
        self.display.blit(self.spinner.image, self.spinner.rect)
        self.display.blit(self.spinner.textimg, self.spinner.textrect)
        self.display.blit(self.pin, self.pinrect)

        if self.vol_button.draw(self.display):
            self.spinner.spinning = True
        self.spinner.update()
