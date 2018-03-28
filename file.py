# This File Handles the I/Os
# Created by JiaWei and Kenny (20/3/18)

from board import *
import sys

# This Function returns reads a given file's instruction and recreates
# the board accordingly
def read_file_from_stdin(new_board):

    # Reads from standard input line by line
    content = sys.stdin.readlines()

    OUTPUT_STATE = None

    # Gets rid of all the leading and trailing newline character
    content = [x.strip() for x in content]

    for x in range(len(content)):
        # Splits up the individual char
        content[x] = ''.join(content[x].split())

        if content[x] == MASSACRE or content[x] == MOVES:
            OUTPUT_STATE = content[x]

        else:
            for y in range(len(content[x])):
                if content[x][y] == 'X':
                    new_board.add_to_pieces(Piece(x, y, CORNER, False))

                elif content[x][y] == 'O':
                    new_board.add_to_pieces(Piece(x, y, WHITE, True))

                elif content[x][y] == '@':
                    new_board.add_to_pieces(Piece(x, y, BLACK, False))

        print(content[x])

    return OUTPUT_STATE
