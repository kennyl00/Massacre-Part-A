from neighbour import *
from board import *
from file import *
from moves import *
from goal import *
import sys

# This is the main file
# Created by JiaWei and Kenny (20/3/18)

def main():

    # Create a new Board
    board = Board()

    file = sys.argv[1]

    # Read the file and set up the Board with Squares and Pieces
    OUTPUT_STATE = read_file(file, board)

    # Find the neighbours of every Pieces
    find_neighbour(board)

    # Output depending on the Messsage
    if OUTPUT_STATE == MASSACRE:
        determinate_goals(board, BLACK)

    elif OUTPUT_STATE == MOVES:
        print(count_legal_move(board, WHITE))
        print(count_legal_move(board, BLACK))



main()
