from neighbour import *
from board import *
from file import *
from moves import *
from goal import *

# This is the main file
# Created by JiaWei and Kenny (20/3/18)

def main():

    # Create a new Board
    board = Board()

    # Read the file and set up the Board with Squares and Pieces
    read_file('sample3.txt', board)

    # Find the neighbours of every Pieces
    find_neighbour(board)

    print(count_legal_move(board, WHITE))
    print(count_legal_move(board, BLACK))

    goal_squares = determinate_goals(board)



main()
