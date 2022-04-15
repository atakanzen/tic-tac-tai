import random
import time
import pygame
import pygame_menu

# TODO: Minimax with alpha-beta prune
# TODO: Play Again button to reset the game
# TODO: Diffuculty difference, easy, medium, hard ?????
# TODO: See the final board after the game is over


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Tic-Tac-Toe')
        self.screen = pygame.display.set_mode((300, 300))
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.difficulty = None
        self.clock = pygame.time.Clock()
        pass

    def updateScreen(self):
        self.clock.tick(60)
        pygame.display.flip()

    def display_menu(self):
        self.menu = pygame_menu.Menu('Tic-Tac-Toe', 300, 300,
                                     theme=pygame_menu.themes.THEME_DARK)
        self.menu.add.button(
            'Easy', self.display_board, "easy")
        self.menu.add.button('Medium', self.display_board, "medium")
        self.menu.add.button('Hard', self.display_board, "hard")
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.screen)

    def display_board(self, difficulty):
        self.difficulty = difficulty
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

    # Display the winner and ask for a new game

    def display_game_over(self, winner):
        self.game_over_screen = pygame.display.set_mode((300, 300))
        menu = pygame_menu.Menu('GAME OVER', 300, 300,
                                theme=pygame_menu.themes.THEME_DARK)

        if winner == 0:
            menu.add.label("Draw", font_size=45, font_color=(255, 0, 0))
            pygame.display.flip()
        else:
            menu.add.label("Winner is: " + str(winner),
                           font_size=45, font_color=(255, 0, 0))
            pygame.display.flip()

        menu.add.button('Play again', print('Play again'))
        menu.add.button('Exit game', pygame_menu.events.EXIT)
        menu.mainloop(self.game_over_screen)

    def select_board_position(self, row, column, player):
        self.board[row][column] = player
        self.draw_figures(row, column)

    def select_random_board_position(self):
        while True:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            if self.is_blank_position(row, column):
                self.board[row][column] = 2
                self.draw_figures(row, column)
                break

    def is_blank_position(self, row, column):
        return self.board[row][column] == 0

    def is_board_full(self):
        for row in range(3):
            for column in range(3):
                if self.is_blank_position(row, column):
                    return False
        return True

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

    def is_equal(self, a, b, c):
        return a == b and b == c and a != 0

    def check_winner(self):
        winner = None
        print(self.board)
        # Horizontal
        for row in range(3):
            if self.is_equal(self.board[row][0],
                             self.board[row][1],
                             self.board[row][2]):
                winner = self.board[row][0]

        # Vertical
        for column in range(3):
            if self.is_equal(self.board[0][column],
                             self.board[1][column],
                             self.board[2][column]):
                winner = self.board[0][column]

        # Diagonal
        if self.is_equal(self.board[0][0], self.board[1][1], self.board[2][2]):
            winner = self.board[0][0]
        if self.is_equal(self.board[0][2], self.board[1][1], self.board[2][0]):
            winner = self.board[0][2]

        if winner == None and self.is_board_full():
            return 0
        else:
            return winner
