from neighbour import *
from board import *
from file import *
from moves import *
from Astar import *
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


    

main()
