import pygame
from ScamOrNotScam.button import Button

class Contestant(Button):
    def __init__(self, x, y, unpressed_image, pressed_image, name):
        # initiate all characteristics of a button
        super().__init__(x, y, unpressed_image=unpressed_image, pressed_image=pressed_image)

        # font for test
        self.font = pygame.font.Font('fonts/cooper.ttf', 40)

        # set name
        self.name_text = self.font.render(name, True, (0, 0, 0))
        self.name_rect = self.name_text.get_rect(center=(self.rect.center[0], self.rect.bottom + 20))

        # set initial score to zero
        self.score = 0
        self.score_text = self.font.render(str(self.score), True, (0, 0, 0))
        self.score_rect = self.score_text.get_rect(center=(self.name_rect.center[0], self.name_rect.bottom + 20))

        # create score add and remove buttons
        score_up_image = pygame.image.load("sprites/score_up.png").convert_alpha()
        score_down_image = pygame.image.load("sprites/score_down.png").convert_alpha()
        self.score_up_button = Button(x=self.rect.center[0] + 110, y=self.rect.center[1] - 30,
                                      unpressed_image=score_up_image, pressed_image=score_up_image)
        self.score_down_button = Button(x=self.rect.center[0] + 110, y=self.rect.center[1] + 10,
                                        unpressed_image=score_down_image, pressed_image=score_down_image)

        # create scam and not scam selection buttons & states
        scam_image = pygame.image.load("sprites/scam.png").convert_alpha()
        not_scam_image = pygame.image.load("sprites/not_scam.png").convert_alpha()
        self.scam_button = Button(x=self.rect.center[0] - 350, y=self.rect.topleft[1] + 50,
                                      unpressed_image=scam_image, pressed_image=scam_image)
        self.scam = False
        self.not_scam_button = Button(x=self.rect.center[0] - 225, y=self.rect.topleft[1] + 50,
                                        unpressed_image=not_scam_image, pressed_image=not_scam_image)
        self.not_scam = False

        # create selection square for scam & not scam buttons
        self.scam_select_image = pygame.image.load("sprites/scam_selection.png").convert_alpha()
        self.scam_select_rect = self.scam_select_image.get_rect(center = (self.scam_button.rect.center[0],
                                                                          self.scam_button.rect.center[1]))
        self.not_scam_select_rect = self.scam_select_image.get_rect(center = (self.not_scam_button.rect.center[0],
                                                                          self.not_scam_button.rect.center[1]))

        # create portrait selection circle
        self.selected = False
        self.select_image = pygame.image.load("sprites/selection.png").convert_alpha()
        self.select_rect = self.select_image.get_rect(center = (self.rect.center[0] + 2, self.rect.center[1] - 2))

    def draw_questions(self, display):

        # draw score buttons
        if self.score_up_button.draw(display):
            self.score += 10
        if self.score_down_button.draw(display):
            self.score = max(0, self.score - 10)

        # update score to current & center again
        self.score_text = self.font.render(str(self.score), True, (0, 0, 0))
        self.score_rect = self.score_text.get_rect(center=(self.name_rect.center[0], self.name_rect.bottom + 20))

        # draw name and score
        display.blit(self.name_text, self.name_rect)
        display.blit(self.score_text, self.score_rect)

        # create scam and not scam selection buttons
        # turn off other button, then switch current button state
        if self.scam_button.draw(display):
            self.not_scam = False
            if self.scam == False:
                self.scam = True
            else:
                self.scam = False

        if self.not_scam_button.draw(display):
            self.scam = False
            if self.not_scam == False:
                self.not_scam = True
            else:
                self.not_scam = False

        if self.scam:
            display.blit(self.scam_select_image, self.scam_select_rect)
        if self.not_scam:
            display.blit(self.scam_select_image, self.not_scam_select_rect)

        super().draw(display)

    def draw_markets(self, display):

        # draw text and score
        self.score_text = self.font.render(str(self.score), True, (0, 0, 0))
        self.score_rect = self.score_text.get_rect(center=(self.name_rect.center[0], self.name_rect.bottom + 20))

        display.blit(self.name_text, self.name_rect)
        display.blit(self.score_text, self.score_rect)

        if self.selected:
            display.blit(self.select_image, self.select_rect)

        return super().draw(display)
