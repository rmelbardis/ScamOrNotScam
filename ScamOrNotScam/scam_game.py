import pygame
from ScamOrNotScam import ROOT

# import objects
from ScamOrNotScam.button import Button
from ScamOrNotScam.spinner import Spinner
from ScamOrNotScam.contestant import Contestant

# import state manager and states
from ScamOrNotScam.gameStateManager import GameStateManager
from ScamOrNotScam.questions import Questions
from ScamOrNotScam.the_markets import Markets

# set up the game
pygame.init()
pygame.font.init()
# set up clock for fps
clock = pygame.time.Clock()
# draw the screen & set caption
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Scam or Not Scam')

# create contestants
cont_1_img = pygame.image.load(ROOT / "sprites/cont_1.png").convert_alpha()
cont_1 = Contestant(x = 1450, y = 60, unpressed_image=cont_1_img, pressed_image=cont_1_img, name='C1')
cont_2_img = pygame.image.load(ROOT / "sprites/cont_2.png").convert_alpha()
cont_2 = Contestant(x = 1450, y = 390, unpressed_image=cont_2_img, pressed_image=cont_2_img, name='C2')
cont_3_img = pygame.image.load(ROOT / "sprites/cont_3.png").convert_alpha()
cont_3 = Contestant(x = 1450, y = 720, unpressed_image=cont_3_img, pressed_image=cont_3_img, name='C3')

# set up states
game_state_manager = GameStateManager('questions')
questions = Questions(screen, game_state_manager, cont_1, cont_2, cont_3)
markets = Markets(screen, game_state_manager, cont_1, cont_2, cont_3)

states = {'questions': questions, 'markets': markets}

# create buttons to switch between questions and markets

right_arrow = pygame.image.load(ROOT / "sprites/forward.png").convert_alpha()
left_arrow = pygame.image.load(ROOT / "sprites/back.png").convert_alpha()
forward_button = Button(x=1800, y=15, unpressed_image=right_arrow, pressed_image=right_arrow)
back_button = Button(x=1700, y=15, unpressed_image=left_arrow, pressed_image=left_arrow)

# start running the game
running = True

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
