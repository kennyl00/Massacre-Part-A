# This file contains functions that deals with movements of the Pieces
# Created by JiaWei and Kenny (20/3/18)



def count_legal_move(new_board, color):
    count = 0
    for piece in new_board.pieces:
        if piece.color is color:
            if piece.left:
                if isinstance(piece.left, Square):
                    count += 1
                else:
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
