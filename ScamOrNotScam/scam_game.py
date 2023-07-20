import pygame
from ScamOrNotScam.button import Button
from ScamOrNotScam.spinner import Spinner
from ScamOrNotScam.gameStateManager import GameStateManager
from ScamOrNotScam.questions import Questions
from ScamOrNotScam.the_markets import Markets

# set up the game
pygame.init()
pygame.font.init()
# set up clock for fps
clock = pygame.time.Clock()
# draw the screen
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Scam or Not Scam')

# set up states
game_state_manager = GameStateManager('questions')
questions = Questions(screen, game_state_manager)
markets = Markets(screen, game_state_manager)

states = {'questions': questions, 'markets': markets}

running = True

right_arrow = pygame.image.load("sprites/forward.png")
left_arrow = pygame.image.load("sprites/back.png")
forward_button = Button(x=1800, y=40, unpressed_image=right_arrow, pressed_image=right_arrow)
back_button = Button(x=1700, y=40, unpressed_image=left_arrow, pressed_image=left_arrow)

while running:

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # states
    states[game_state_manager.get_state()].run()

    if forward_button.draw(screen):
        game_state_manager.set_state('markets')

    if back_button.draw(screen):
        game_state_manager.set_state('questions')

    # update display and fix fps
    pygame.display.update()
    clock.tick(50)

pygame.quit()
