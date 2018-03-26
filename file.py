# This File Handles the Inputs and Outputs
# Created by JiaWei and Kenny (20/3/18)
from board import *
import sys

# Reads the board configuration from a file and recreates the actual Board
def read_file_from_stdin(new_board):

    # Reads from standard input line by line
    content = sys.stdin.readlines()

    # Gets rid of all the leading and trailing newline character
    content = [x.strip() for x in content]

    # For every row in the data
    for x in range(len(content)):

        # Split up the individuals
        content[x] = ''.join(content[x].split())

        # Check the last
        if content[x] == MASSACRE or content[x] == MOVES:
            OUTPUT_STATE = content[x]

        else:

            for y in range(len(content[x])):
                # Fill up the Board
                if content[x][y] == 'X':
                    new_board.add_to_pieces(Piece(x, y, CORNER))

                elif content[x][y] == 'O':
                    new_board.add_to_pieces(Piece(x, y, WHITE))

                elif content[x][y] == '@':
                    new_board.add_to_pieces(Piece(x, y, BLACK))


        print(content[x])

    return OUTPUT_STATE
