import math
import random
import pygame


# TODO: Minimax with alpha-beta prune
# TODO: See the final board after the game is over

class Game:
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __init__(self):
        pygame.init()
        self.player = 1
        self.__difficulty = "Easy"
        self.scores = {1: -1000, 2: 1000, 0: 0}

    def set_difficulty(self, difficulty):
        if difficulty == "I love my life":
            self.__difficulty = "Easy"
        elif difficulty == "I hate my life":
            self.__difficulty = "Hard"

    def get_difficulty(self):
        return self.__difficulty

    def reset_game(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.player = 1

    def select_board_position(self, row, column, player):
        self.board[row][column] = player
        self.draw_figures(row, column)

    def unselect_board_position(self, row, column):
        self.board[row][column] = ""

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

    def get_blank_positions(self):
        blank_positions = []
        for row in range(3):
            for column in range(3):
                if self.is_blank_position(row, column):
                    blank_positions.append((row, column))
        return blank_positions

    def is_board_full(self):
        for row in range(3):
            for column in range(3):
                if self.is_blank_position(row, column):
                    return False
        return True

    def draw_figures(self, board_row, board_column):
        o_color = (17, 25, 245)
        x_color = (245, 235, 42)
        board_screen = pygame.display.get_surface()

        if self.board[board_row][board_column] == 1:
            pygame.draw.circle(
                board_screen,
                o_color,
                (
                    int(board_column * (226) + (226 / 2)),
                    int(board_row * 226 + (226 / 2))
                ),
                226 / 3.5,
                15
            )

        elif self.board[board_row][board_column] == 2:
            pygame.draw.line(
                board_screen,
                x_color,
                (
                    int(board_column * (226) + (226 / 4)),
                    int(board_row * 226 + (226 / 4))
                ),
                (
                    int(board_column * (226) + (226 / 4)) + 226 / 2,
                    int(board_row * 226 + (226 / 4)) + 226 / 2
                ),
                20
            )

            pygame.draw.line(
                board_screen,
                x_color,
                (
                    int(board_column * (226) + (226 / 4)),
                    int(board_row * 226 + (226 / 4)) + 226 / 2
                ),
                (
                    int(board_column * (226) + (226 / 4)) + 226 / 2,
                    int(board_row * 226 + (226 / 4))
                ),
                20
            )

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

    def get_best_move(self):
        best_score = -math.inf
        best_move = None
        for row in range(3):
            for column in range(3):
                if self.is_blank_position(row, column):
                    self.board[row][column] = 2
                    score = self.minimax(0, False)
                    self.board[row][column] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (row, column)
        return best_move

    def get_best_move_alphabeta(self):
        best_score = -math.inf
        best_move = None
        for row in range(3):
            for column in range(3):
                if self.is_blank_position(row, column):
                    self.board[row][column] = 2
                    score = self.minimax_alphabeta(
                        0, -math.inf, math.inf, False)
                    self.board[row][column] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (row, column)
        return best_move

    def minimax_alphabeta(self, depth, alpha, beta, is_maximizing):
        result = self.check_winner()
        if result != None:
            return self.scores[result]

        if is_maximizing:
            best_score = -math.inf
            for row in range(3):
                for column in range(3):
                    if self.is_blank_position(row, column):
                        self.board[row][column] = 2
                        score = self.minimax_alphabeta(
                            depth + 1, alpha, beta, False)
                        self.board[row][column] = 0
                        best_score = max(best_score, score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = math.inf
            for row in range(3):
                for column in range(3):
                    if self.is_blank_position(row, column):
                        self.board[row][column] = 1
                        score = self.minimax_alphabeta(
                            depth + 1, alpha, beta, True)
                        self.board[row][column] = 0
                        best_score = min(best_score, score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score

    def minimax(self, depth, is_maximizing):
        result = self.check_winner()
        if result != None:
            return self.scores[result]

        if is_maximizing:
            best_score = -math.inf
            for row in range(3):
                for column in range(3):
                    if self.is_blank_position(row, column):
                        self.board[row][column] = 2
                        score = self.minimax(depth + 1, False)
                        self.board[row][column] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for row in range(3):
                for column in range(3):
                    if self.is_blank_position(row, column):
                        self.board[row][column] = 1
                        score = self.minimax(depth + 1, True)
                        self.board[row][column] = 0
                        best_score = min(score, best_score)
            return best_score
