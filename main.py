
import pygame
from game import Game
from gui import GUI


def main():
    """
    Main function
    """
    game = Game()
    gui = GUI()

    gui.display_start_menu()

    player = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_x = event.pos[0]
                click_y = event.pos[1]

                board_row = int(click_y // (gui.height / 3))
                board_column = int(click_x // (gui.width / 3))

                if player == 1:
                    if game.is_blank_position(board_row, board_column):
                        game.select_board_position(board_row, board_column, 1)
                        winner = game.check_winner()
                        if winner is not None:
                            gui.display_game_over(winner)
                        player = 2

                        # if (game.difficulty == "EASY"):
                        game.select_random_board_position()
                        winner = game.check_winner()
                        if winner is not None:
                            gui.display_game_over(winner)
                        player = 1
        gui.updateScreen()


if __name__ == "__main__":
    main()
