import pygame
import sys
import numpy as np


pygame.init()

# create the screen:
screen_color = (12, 12, 13)
screen_display = pygame.display.set_mode((300, 300))
pygame.display.set_caption("TIC TAC TOE GAME")
screen_display.fill(screen_color)


# create a board:
board = np.zeros((3, 3))
player = 1


def screen_lines():

    line_color = (255, 0, 0)
    line_width = 7

    # create horizontal lines in the screen
    pygame.draw.line(screen_display, line_color, (0, 0), (300, 0), line_width)
    pygame.draw.line(screen_display, line_color, (0, 100), (300, 100), line_width)
    pygame.draw.line(screen_display, line_color, (0, 200), (300, 200), line_width)
    pygame.draw.line(screen_display, line_color, (0, 300), (300, 300), line_width)

    # create vertical lines in the screen
    pygame.draw.line(screen_display, line_color, (0, 0), (0, 600), line_width)
    pygame.draw.line(screen_display, line_color, (100, 0), (100, 300), line_width)
    pygame.draw.line(screen_display, line_color, (200, 0), (200, 300), line_width)
    pygame.draw.line(screen_display, line_color, (300, 0), (300, 300), line_width)


def select_board_position(row, column, player):
    board[row][column] = player


def blank_position(row, column):
    if board[row][column] == 0:
        return True
    else:
        return False


def full_board():
    if (board[0][0] == 0 or board[0][1] == 0 or board[0][2] == 0 or board[1][0] == 0 or board[1][1] == 0 or
            board[1][2] == 0 or board[2][0] == 0 or board[2][1] == 0 or board[2][2] == 0):
        return False
    else:
        return True


def draw_figures(screen_display):
    circle_color = (17, 25, 245)
    x_color = (245, 235, 42)
    if board[board_row][board_column] == 2:
        pygame.draw.circle(screen_display, circle_color, (int(board_column * 100 + 50),
                                                          int(board_row * 100 + 50)), 30, 8)
    elif board[board_row][board_column] == 1:
        pygame.draw.line(screen_display, x_color, (board_column * 100 + 25, board_row * 100 + 100 - 25),
                                                  (board_column * 100 + 100 - 25, board_row * 100 + 25), 10)

        pygame.draw.line(screen_display, x_color, (board_column * 100 + 25, board_row * 100 + 25),
                                                  (board_column * 100 + 100 - 25, board_row * 100 + 100 - 25), 10)


screen_lines()

# main loop:
while True:

    for event in pygame.event.get():
        # check if af I clic on "x" of the screen to exit
        if event.type == pygame.QUIT:
            sys.exit()

           # check other clicks in the screen and get the coordinates of that clic:
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x = event.pos[0]
            click_y = event.pos[1]

            print(click_x)
            print(click_y)

            # divide the coordinates between 100 in order to get the properly board coordinates(1,1),(1,2)...
            board_row = int(click_y // 100)
            board_column = int(click_x // 100)

            # use the blank_position to check if the space clicked is available:
            if blank_position(board_row, board_column):
                if player == 1:
                    # place in the selected space in the board 1 for player one.
                    select_board_position(board_row, board_column, 1)
                    player = 2

                elif player == 2:
                    # place in the selected space in the board 2 for player two.
                    select_board_position(board_row, board_column, 2)
                    player = 1
                draw_figures(screen_display)
    pygame.display.update()