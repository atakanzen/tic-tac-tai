
import pygame
from game import Game
from gui import GUI
from minmax import Minmax


def main():
    """
    Main function
    """
    game = Game()
    minmax = Minmax(game, game.board, 0, True)
    gui = GUI(game)

    gui.display_start_menu()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                click_x = event.pos[0]
                click_y = event.pos[1]

                board_row = int(click_y // (gui.height / 3))
                board_column = int(click_x // (gui.width / 3))

                if game.player == 1:
                    if game.is_blank_position(board_row, board_column):
                        game.select_board_position(board_row, board_column, 1)
                        winner = game.check_winner()
                        if winner is not None:
                            gui.display_game_over(winner)
                            continue
                        game.player = 2

                        if (game.get_difficulty() == "Easy"):
                            game.select_random_board_position()
                            winner = game.check_winner()
                            if winner is not None:
                                gui.display_game_over(winner)
                                continue

                        elif game.get_difficulty() == "Hard":
                            # TODO: Implement Hard AI
                            best_move = minmax.get_best_move()
                            # print(best_move)
                            # game.select_board_position(
                            #     best_move[0], best_move[1], 2)

                            winner = game.check_winner()
                            if winner is not None:
                                gui.display_game_over(winner)
                                continue
                            pass

                        game.player = 1

        gui.updateScreen()


if __name__ == "__main__":
    main()
