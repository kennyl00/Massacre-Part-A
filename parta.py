from neighbour import *
from board import *
from file import *
from moves import *
from Astar import *
from Massacre import *

import sys

# This is the main file
# Created by JiaWei and Kenny (20/3/18)

def main():

    # Create a new Board
    board = Board()

    # Reads the file from input and fills up the board
    OUTPUT_STATE = read_file_from_stdin(board)

    Massacre(board, BLACK)
'''
    piece1 = None
    for piece in board.pieces:
        if piece.x == 7 and piece.y == 3:
            piece1 = piece


    print(get_square(piece1, TOP, BLACK).y, get_square(piece1, TOP, BLACK).x)

'''



main()
