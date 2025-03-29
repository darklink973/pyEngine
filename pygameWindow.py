import pygame
import button_List
import os
import spriteManager
from pathlib import Path

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()

def fullscreen():
        fullscreen.toggle = 1 - fullscreen.toggle
        if fullscreen.toggle:
            return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        else:
            return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        
fullscreen.toggle = 0
screen = fullscreen()
clock = pygame.time.Clock()
running = True
guiNumber = 0

def drawGrid(color, size):
    blockSize = size
    for x in range(0, SCREEN_WIDTH, blockSize):
        for y in range(0, SCREEN_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, color, rect, 1)

def firstUse(name):
    

while running:
    SCREEN_WIDTH = pygame.display.get_surface().get_rect().w
    SCREEN_HEIGHT = pygame.display.get_surface().get_rect().h
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if(guiNumber == 0):
        screen.fill("white")
        if(button_List.button_List("start", 100, 200, 0.8).draw(screen)):
            try:
                file_path = os.path.join("game", "scene_1.py")
                directory_path = Path("game/image")
                f = open(file_path, "x")
                f.write('# Example file showing a basic pygame "game loop"\nimport pygame\n\n# pygame setup\npygame.init()\nscreen = pygame.display.set_mode((1280, 720))\nclock = pygame.time.Clock()\nrunning = True\n\nwhile running:\n    # poll for events\n    # pygame.QUIT event means the user clicked X to close your window\n    for event in pygame.event.get():\n        if event.type == pygame.QUIT:\n            running = False\n\n    # fill the screen with a color to wipe away anything from last frame\n    screen.fill("purple")\n\n    # RENDER YOUR GAME HERE\n\n    # flip() the display to put your work on screen\n    pygame.display.flip()\n\n    clock.tick(60)  # limits FPS to 60\n\npygame.quit()\n')
                f.close
                directory_path.mkdir()

            except FileExistsError:
                pass
            guiNumber = 1

    elif(guiNumber == 1):
        screen.fill("white")
        drawGrid("grey", 20)
        spriteManager.drawSprite(screen, 'doux.png', 1, 24, 24, 2)
        spriteManager.drawSprite(screen, 'doux.png', 2, 24, 24, 2)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()