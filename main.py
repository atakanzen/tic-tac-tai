
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

                print(board_row, board_column)

                if game.is_board_full():
                    print("The board is full")
                    exit()

                # use the blank_position to check if the space clicked is available:
                if game.is_blank_position(board_row, board_column):
                    print("Is Blank")
                    if player == 1:
                        # place in the selected space in the board 1 for player one.
                        game.select_board_position(board_row, board_column, 1)
                        player = 2

                    elif player == 2:
                        # place in the selected space in the board 2 for player two.
                        game.select_board_position(board_row, board_column, 2)
                        player = 1
                    game.draw_figures(board_row, board_column)
                print("Not Blank :(")
            game.updateScreen()


if __name__ == "__main__":
    main()
