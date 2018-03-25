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


    start_square = None
    goal_square = None
    start_piece = None
    for piece in board.squares:
        if piece.x == 2 and piece.y == 5:
            start_square = piece
        if piece.x ==  3 and piece.y == 3:
            goal_square = piece

    for piece in board.pieces:
        if piece.x == 2 and piece.y == 5:
            start_piece = piece



    goal_list = get_goal(board, BLACK)


    for goal in goal_list:
        print(goal.square1.y, goal.square1.x, "||||", goal.square2.y, goal.square2.x)

main()
