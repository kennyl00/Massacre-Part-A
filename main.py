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

    file = sys.argv[1]

    # Read the file and set up the Board with Squares and Pieces
    OUTPUT_STATE = read_file(file, board)

    # Find the neighbours of every Pieces
    find_neighbour(board)

    square1 = None
    square2 = None
    piece_to_eliminate = None

    for piece in board.pieces:
        if piece.x == 7 and piece.y == 4:
            piece_to_eliminate = piece

    for square in board.squares:
        if square.x == 7 and square.y == 5:
            square1 = square

    for square in board.squares:
        if square.x == 7 and square.y == 3:
            square2 = square

    goal = Goal(square1, square2, piece_to_eliminate)

    print(is_goal_achievable(board, goal))



main()
