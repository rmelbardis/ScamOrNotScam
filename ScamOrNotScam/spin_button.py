import pygame

class Button():
    def __init__(self, x, y, unpressed_image, pressed_image):
        self.x = x
        self.y = y
        self.unpressed = unpressed_image
        self.pressed = pressed_image
        self.image = self.unpressed
        self.rect = self.image.get_rect(topleft=(x, y))

        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                self.image = self.pressed

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            self.image = self.unpressed

        surface.blit(self.image, self.rect)

        return action
