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




    # Find the neighbours of every Pieces
    find_neighbour(board)

    goal_list = []

    goal_list = get_goal_list(board, BLACK)


    Massacre(board, BLACK, goal_list)



main()
