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
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

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

    # TODO: Update coordinates of the figures for new screen size
    def draw_figures(self, board_row, board_column):
        o_color = (17, 25, 245)
        x_color = (245, 235, 42)
        board_screen = pygame.display.get_surface()

        if self.board[board_row][board_column] == 2:
            pygame.draw.circle(board_screen, o_color, (int(board_column * 100 + 50),
                                                       int(board_row * 100 + 50)), 30, 8)
        elif self.board[board_row][board_column] == 1:
            pygame.draw.line(board_screen, x_color, (board_column * 100 + 25, board_row * 100 + 100 - 25),
                             (board_column * 100 + 100 - 25, board_row * 100 + 25), 10)

            pygame.draw.line(board_screen, x_color, (board_column * 100 + 25, board_row * 100 + 25),
                             (board_column * 100 + 100 - 25, board_row * 100 + 100 - 25), 10)

    def is_equal(self, a, b, c):
        return a == b and b == c and a != 0

    def check_winner(self):
        winner = None
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

        # Tie
        if winner == None and self.is_board_full():
            return 0
        else:
            return winner
