def button_List(button_name, posX, posY, scale):
    import pygame
    import button
    from pygameWindow import SCREEN_WIDTH
    from pygameWindow import SCREEN_HEIGHT

    _button = button.Button(SCREEN_WIDTH*(posX/10)/100, SCREEN_HEIGHT*(posY/10)/100, pygame.image.load('images/' + button_name + '_btn.png').convert_alpha(), scale)

    return _button