import pygame
from ScamOrNotScam.spin_button import Button

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Scam or Not Scam')
clock = pygame.time.Clock()
running = True

spinner = pygame.image.load("sprites/the_markets.png")
spinnerrect = spinner.get_rect(topleft=(100, 150))

pin = pygame.image.load("sprites/ping_triangle.png")
pinrect = pin.get_rect(topleft=(422, 75))

button_image = pygame.image.load("sprites/volatility.png")
button_pressed = pygame.image.load("sprites/volatility_pressed.png")
vol_button = Button(x=1000, y=400, unpressed_image=button_image, pressed_image=button_pressed)

while running:

    screen.fill(color=(203, 230, 159))

    if vol_button.draw(screen):
        print('SPIN!')

    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME RENDER
    screen.blit(spinner, spinnerrect)
    screen.blit(pin, pinrect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
