import pygame
import pygame_menu


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Tic-Tac-Toe')
        self.screen = pygame.display.set_mode((400, 400))
        pass

    def display_menu(self):
        menu = pygame_menu.Menu('Tic-Tac-Toe', 400, 400,
                                theme=pygame_menu.themes.THEME_DARK)
        menu.add.button('Easy')
        menu.add.button('Medium')
        menu.add.button('Hard')
        menu.add.button('Quit')

        while True:
            menu.mainloop(self.screen)
