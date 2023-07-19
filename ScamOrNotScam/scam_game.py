import pygame
from ScamOrNotScam.spin_button import Button
from ScamOrNotScam.the_markets import Spinner

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Scam or Not Scam')
clock = pygame.time.Clock()
running = True

arrow = pygame.image.load("sprites/arrow.png")
arrowrect = arrow.get_rect(topleft=(411, 15))

button_image = pygame.image.load("sprites/volatility.png")
button_pressed = pygame.image.load("sprites/volatility_pressed.png")
vol_button = Button(x=1000, y=400, unpressed_image=button_image, pressed_image=button_pressed)

spinner_image = pygame.image.load("sprites/the_markets.png")
spinner = Spinner(x=100, y=150, spinner_image=spinner_image, surface=screen)

while running:

    screen.fill(color=(203, 230, 159))

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME RENDER
    screen.blit(spinner.image, spinner.rect)
    screen.blit(spinner.text, spinner.textrect)
    screen.blit(arrow, arrowrect)


    if vol_button.draw(screen):
        # spinner.spin(screen)
        spinner.image = spinner.original_image
        spinner.spinning = True
    spinner.update()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
