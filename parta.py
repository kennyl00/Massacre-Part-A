# This is the Main File
# Created by JiaWei and Kenny (20/3/18)

from neighbour import *
from board import *
from file import *
from moves import *
from Astar import *
from Massacre import *
import sys

def main():

    # Create a new Board
    board = Board()

    # Reads the file from input and fills up the board
    OUTPUT_STATE = read_file_from_stdin(board)

    find_neighbour(board)

    if OUTPUT_STATE == MASSACRE:
        Massacre(board, BLACK)

    elif OUTPUT_STATE == MOVES:
        print(count_legal_moves(board, WHITE))
        print(count_legal_moves(board, BLACK))

    else:
        print("No Instructions Given")

main()
