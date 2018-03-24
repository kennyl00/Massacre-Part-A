# This file contains functions that deals with movements of the Pieces
# Created by JiaWei and Kenny (20/3/18)

from board import *

def count_legal_move(new_board, color):
    count = 0

    # For every Piece in the Board's Piece List
    for piece in new_board.pieces:

        # Check if the Piece has the desired Color
        if piece.color is color:

            # Check the Piece's Direction (TOP, BOTTOM, LEFT, RIGHT)
            # has an Object
            # Since there are CORNERS and Pieces on the sides do not necessarily
            # have neighbours

            # If the Piece's LEFT has an Object
            if piece.left:

                # Check if the Object is a Square
                if isinstance(piece.left, Square):
                    count += 1

                else:
                    # If not, check if the Piece's Left Left is a Square
                    # Since they can jump
                    if piece.left.left and isinstance(piece.left.left, Square):
                        count += 1


            if piece.right:
                if isinstance(piece.right, Square):
                    count += 1
                else:
                    if piece.right.right and isinstance(piece.right.right, Square):
                        count += 1


            if piece.top:
                if isinstance(piece.top, Square):
                    count += 1
                else:
                    if piece.top.top and isinstance(piece.top.top, Square):
                        count += 1


            if piece.bottom:
                if isinstance(piece.bottom, Square):
                    count += 1
                else:
                    if piece.bottom.bottom and isinstance(piece.bottom.bottom, Square):
                        count += 1

    return count

def check_move(piece, dir, target_color):

    # First check if the move is possible
    if check_valid_move(piece, dir):
        # Check if move could be eliminated
        if check_elimination_move(piece, dir, target_color):
            return YES

    else:
        # Check if a jump move is possible
        if check_valid_jump_move(piece, dir):
            return JUMP

    return NO


# This function checks if the a move results in the elimination of the Piece
def check_elimination_move(piece, dir, target_color):

    if dir == RIGHT:
        if isinstance(piece.top_right, Piece) and isinstance(piece.bottom_right, Piece):
            if piece.top_right.color == target_color and piece.bottom_right == target_color:
                return False

    if dir == LEFT:
        if isinstance(piece.top_left, Piece) and isinstance(piece.bottom_left, Piece):
            if piece.top_left.color == target_color and piece.bottom_left.color == target_color:
                return False

    if dir == TOP:
        if isinstance(piece.top_left, Piece) and isinstance(piece.top_right, Piece):
            if piece.top_left.color == target_color and piece.top_right.color == target_color:
                return False

    if dir == BOTTOM:
        if isinstance(piece.bottom_left, Piece) and isinstance(piece.bottom_right, Piece):
            if piece.bottom_left.color == target_color and piece.bottom_right.color == target_color:
                return False

    return True

# This function returns if a specific direction could jumped over
def check_valid_jump_move(piece, dir):

    if dir == LEFT and isinstance(piece.left.left, Square):
        return True

    if dir == RIGHT and isinstance(piece.right.right, Square):
        return True

    if dir == TOP and isinstance(piece.top.top, Square):
        return True

    if dir == BOTTOM and isinstance(piece.bottom.bottom, Square):
        return True


    return False


# This function returns if a specific direction is a valid move
# Valid moves are determined by Squares
def check_valid_move(piece, dir):

    if dir == LEFT and isinstance(piece.left, Square):
        return True

    if dir == RIGHT and isinstance(piece.right, Square):
        return True

    if dir == TOP and isinstance(piece.top, Square):
        return True

    if dir == BOTTOM and isinstance(piece.bottom, Square):
        return True


    return False
