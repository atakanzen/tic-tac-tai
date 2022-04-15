
import pygame
from game import Game


def main():
    """
    Main function
    """
    game = Game()
    game.display_menu()
    player = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_x = event.pos[0]
                click_y = event.pos[1]

                # divide the coordinates between 100 in order to get the properly board coordinates(1,1),(1,2)...
                board_row = int(click_y // 100)
                board_column = int(click_x // 100)

                # use the blank_position to check if the space clicked is available
                if player == 1:
                    if game.is_blank_position(board_row, board_column):
                        # place in the selected space in the board for human
                        game.select_board_position(board_row, board_column, 1)
                        winner = game.check_winner()
                        if winner is not None:
                            game.display_game_over(winner)

                        player = 2
                        if (game.difficulty == "easy"):
                            game.select_random_board_position()
                            winner = game.check_winner()
                            if winner is not None:
                                game.display_game_over(winner)
                            player = 1
            game.updateScreen()


if __name__ == "__main__":
    main()
