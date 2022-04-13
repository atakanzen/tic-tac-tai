import pygame
import pygame_menu


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Tic-Tac-Toe')
        self.screen = pygame.display.set_mode((300, 300))
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.clock = pygame.time.Clock()
        pass

    def updateScreen(self):
        self.clock.tick(60)
        pygame.display.flip()

    def display_menu(self):
        self.menu = pygame_menu.Menu('Tic-Tac-Toe', 300, 300,
                                     theme=pygame_menu.themes.THEME_DARK)
        self.menu.add.button('Easy', self.display_board)
        self.menu.add.button('Medium')
        self.menu.add.button('Hard')
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.screen)

    def display_board(self):
        self.menu.disable()
        line_color = (255, 0, 0)
        line_width = 7

        self.board_screen = pygame.display.set_mode((300, 300))
        self.board_screen.fill((12, 12, 13))
        # create horizontal lines in the screen
        pygame.draw.line(self.board_screen, line_color,
                         (0, 0), (300, 0), line_width)
        pygame.draw.line(self.board_screen, line_color,
                         (0, 100), (300, 100), line_width)
        pygame.draw.line(self.board_screen, line_color,
                         (0, 200), (300, 200), line_width)
        pygame.draw.line(self.board_screen, line_color,
                         (0, 300), (300, 300), line_width)

        # create vertical lines in the screen
        pygame.draw.line(self.board_screen, line_color,
                         (0, 0), (0, 600), line_width)
        pygame.draw.line(self.board_screen, line_color,
                         (100, 0), (100, 300), line_width)
        pygame.draw.line(self.board_screen, line_color,
                         (200, 0), (200, 300), line_width)
        pygame.draw.line(self.board_screen, line_color,
                         (300, 0), (300, 300), line_width)
        pygame.display.flip()
        self.updateScreen()
    pass

    def select_board_position(self, row, column, player):
        self.board[row][column] = player

    def is_blank_position(self, row, column):
        return self.board[row][column] == 0

    def is_board_full(self):
        return (self.board[0][0] != 0 and
                self.board[0][1] != 0 and
                self.board[0][2] != 0 and
                self.board[1][0] != 0 and
                self.board[1][1] != 0 and
                self.board[1][2] != 0 and
                self.board[2][0] != 0 and
                self.board[2][1] != 0 and
                self.board[2][2] != 0)

    def draw_figures(self, board_row, board_column):
        o_color = (17, 25, 245)
        x_color = (245, 235, 42)
        if self.board[board_row][board_column] == 2:
            pygame.draw.circle(self.board_screen, o_color, (int(board_column * 100 + 50),
                                                            int(board_row * 100 + 50)), 30, 8)
        elif self.board[board_row][board_column] == 1:
            pygame.draw.line(self.board_screen, x_color, (board_column * 100 + 25, board_row * 100 + 100 - 25),
                             (board_column * 100 + 100 - 25, board_row * 100 + 25), 10)

            pygame.draw.line(self.board_screen, x_color, (board_column * 100 + 25, board_row * 100 + 25),
                             (board_column * 100 + 100 - 25, board_row * 100 + 100 - 25), 10)
