import random
import sys
import pygame
from pygame.locals import *  # basic pygame import
from pygame import mixer
pygame.mixer.init()
#global variable

FPS = 64
SCREENWIDTH = 400
SCREENHEIGHT = 500
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT*0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'GAMES/bird.png'
BACKGROUND = 'GAMES/background.jpg'
PIPE = 'GAMES/pipe.jpg'


def welcomeScreen():
    """
    shows welcome screen
    """
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_height())/2)
    messagey = int(SCREENHEIGHT * 0.13)
    basex = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


if __name__ == "__main__":
    # this is where our game starts
    pygame.init  # intialize py game modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('flappy bird by sooraj')
    GAME_SPRITES['numbers'] = (
        pygame.image.load(
            'GAMES/0.png').convert_alpha(),
        pygame.image.load(
            'GAMES/1.png').convert_alpha(),
        pygame.image.load(
            'GAMES/2.png').convert_alpha(),
        pygame.image.load(
            'GAMES/3.png').convert_alpha(),
        pygame.image.load(
            'GAMES/4.png').convert_alpha(),
        pygame.image.load(
            'GAMES/5.png').convert_alpha(),
        pygame.image.load(
            'GAMES/6.png').convert_alpha(),
        pygame.image.load(
            'GAMES/7.png').convert_alpha(),
        pygame.image.load(
            'GAMES/8.png').convert_alpha(),
        pygame.image.load(
            'GAMES/9.png').convert_alpha(),
    )

    GAME_SPRITES['message'] = pygame.image.load(
        'GAMES/manage.jpg')
    GAME_SPRITES['base'] = pygame.image.load(
        'GAMES/manage.jpg')
    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE) .convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()
    )
    # game sound
    GAME_SOUNDS['die'] = pygame.mixer.Sound(
        'C:/Users/adish/Music/editting tones/die.mp3')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound(
        'C:/Users/adish/Music/editting tones/hit.mp3')
    GAME_SOUNDS['point'] = pygame.mixer.Sound(
        'C:/Users/adish/Music/editting tones/point.wav')
    GAME_SOUNDS['Swoosh'] = pygame.mixer.Sound(
        'C:/Users/adish/Music/editting tones/Swoosh.mp3')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound(
        'C:/Users/adish/Music/editting tones/wing.mp3')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()
