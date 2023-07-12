import pygame
from ScamOrNotScam.the_markets import Spinner

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

spinner = pygame.image.load("sprites/the_markets.png")
spinnerrect = spinner.get_rect(topleft=(100, 150))

pin = pygame.image.load("sprites/ping_triangle.png")
pinrect = pin.get_rect(topleft=(424, 75))

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # GAME RENDER
    screen.blit(spinner, spinnerrect)
    screen.blit(pin, pinrect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
