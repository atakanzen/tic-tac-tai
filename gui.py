
import pygame
import pygame_menu

from game import Game


class GUI:

    # Constructor
    def __init__(self, game: Game):
        pygame.init()
        pygame.display.set_caption('Tic-Tac-Tai')
        self.game = game
        self.width = 680
        self.height = 680
        self.__menu = None
        self.__game_over_menu = None
        self.__board_screen = None
        self.__screen = pygame.display.set_mode((self.width, self.height))
        self.__clock = pygame.time.Clock()

    def set_difficulty(self, selection, _):
        self.game.set_difficulty(selection[0][0])

    def display_start_menu(self):
        theme = pygame_menu.themes.THEME_DARK.copy()
        theme.title_font = pygame_menu.font.FONT_BEBAS
        theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_ADAPTIVE

        self.__menu = pygame_menu.Menu('Tic-Tac-Tai', self.width, self.height,
                                       theme=theme)

        self.__menu.add.selector('Difficulty: ',
                                 [('Easy', 1), ('Medium', 2), ('Hard', 3)],
                                 onchange=self.set_difficulty)
        self.__menu.add.button('Start game', self.display_board)
        self.__menu.add.button('Quit', pygame_menu.events.EXIT)
        self.__menu.mainloop(self.__screen)

    def display_board(self):
        if self.__menu != None:
            self.__menu.disable()

        if self.__game_over_menu != None:
            self.__game_over_menu.disable()

        self.__board_screen = pygame.display.set_mode(
            (self.width, self.height), vsync=1)
        self.__board_screen.fill((12, 12, 13))

        line_color = pygame.color.Color(158, 12, 12, 15)
        line_width = 10

        for i in range(4):
            pygame.draw.line(self.__board_screen, line_color,
                             (0, i * (self.height / 3)), (self.width, i * (self.height / 3)), line_width)
            for j in range(4):
                pygame.draw.line(self.__board_screen, line_color,
                                 (j * (self.width / 3), 0), (j * (self.height / 3), self.height), line_width)

        pygame.display.flip()

    def display_game_over(self, winner):
        self.game.reset_game()
        self.__game_over_screen = pygame.display.set_mode(
            (self.width, self.height))
        self.__game_over_menu = pygame_menu.Menu('Game Over', self.width, self.height,
                                                 theme=pygame_menu.themes.THEME_DARK)
        if winner == 0:
            self.__game_over_menu.add.label(
                "Tie", font_size=45, font_color=(255, 0, 0), padding=(0, 0, 10, 0))
        else:
            winner = 'X' if winner == 1 else 'O'
            self.__game_over_menu.add.label(str(winner) + " wins!",
                                            font_size=45, font_color=(255, 0, 0), padding=(0, 0, 10, 0))
        pygame.display.flip()

        self.__game_over_menu.add.button('Play again', self.display_board)
        self.__game_over_menu.add.button('Exit game', pygame_menu.events.EXIT)
        self.__game_over_menu.mainloop(self.__game_over_screen)

    # 60 frames per second
    def updateScreen(self):
        self.__clock.tick(60)
        pygame.display.flip()
