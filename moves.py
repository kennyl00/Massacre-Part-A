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
