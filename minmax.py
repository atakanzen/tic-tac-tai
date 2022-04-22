

from game import Game


class Minmax:

    def __init__(self, game: Game, board, depth, is_maximizing_player):
        self.game = game
        self.board = board
        self.depth = depth
        self.is_maximizing_player = is_maximizing_player
        self.scores = {1: 100, 2: -100, 0: 0}

    def get_best_move(self):
        best_move = None
        best_score = -10000
        for row, column in self.game.get_blank_positions():

            if self.game.is_blank_position(row, column):

                self.game.select_board_position(row, column, 2)

                score = self.minimax(self.depth, False)

                self.game.unselect_board_position(row, column)

                best_score = max(best_score, score)
                best_move = self.board[row][column]
        return best_move

    def minimax(self, depth, is_maximizing_player):
        if self.game.check_winner() is not None:
            return self.scores.get(self.game.check_winner())
        if is_maximizing_player:
            best_score = -10000
            for row, column in self.game.get_blank_positions():
                self.game.select_board_position(row, column, 2)
                score = self.minimax(depth + 1, False)
                self.game.unselect_board_position(row, column)
                print(f"{score} IS_MAX")
                print(f"{best_score} IS_MAX")
                best_score = max(best_score, score)

            return best_score
        else:
            best_score = 10000
            for row, column in self.game.get_blank_positions():
                self.game.select_board_position(row, column, 1)
                print(depth)
                score = self.minimax(depth + 1, True)

                self.game.unselect_board_position(row, column)
                print(f"{score} IS_MIN")
                print(f"{best_score} IS_MIN")
                best_score = min(best_score, score)

            return best_score
