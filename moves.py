# This file contains functions that deals with movements of the Pieces
# Created by JiaWei and Kenny (20/3/18)

from board import *

# This Function returns all the available moves (including Jumps) of a
# particular colored Piece
def count_legal_moves(new_board, color):
    count = 0

    # For every given Colored Piece, check all 4 directions and see
    # if they could jump or move
    for piece in new_board.pieces:
        if piece.color is color:
            for dir in range(LEFT, BOTTOM+1):
                piece_at_dir = piece.square_at(dir)
                if piece_at_dir:
                    if isinstance(piece_at_dir, Square):
                        count+=1

                    else:
                        piece_at_dir_dir = piece_at_dir.square_at(dir)
                        if piece_at_dir_dir and \
                        isinstance(piece_at_dir_dir, Square):
                            count+=1

    return count


# This Function returns a List of Goals that needs to filled by Pieces
def get_goal_list(board, target_color):

    goal_squares = []

    # For every piece on the Board, check the Piece's X and Y direction and
    # create a Goal Object if the Piece could be eliminated
    for piece in board.pieces:
        if piece.color == target_color:
            for dir in range(LEFT, TOP+1):

                # The Piece's side is filled with a Piece and a Square
                if isinstance(piece.square_at(dir), Piece) and \
                isinstance(piece.opposite_of(dir), Square):
                    if piece.square_at(dir).color == WHITE:
                        goal_squares.append(Goal(piece.square_at(dir), \
                        piece.opposite_of(dir), piece))

                    elif piece.square_at(dir).color == CORNER:
                        goal_squares.append(Goal(piece.opposite_of(dir), \
                        None, piece))

                # The Piece's side is filled with a Square and a Piece
                elif isinstance(piece.square_at(dir), Square) and \
                isinstance(piece.opposite_of(dir), Piece):
                    if piece.opposite_of(dir).color == WHITE:
                        goal_squares.append(Goal(piece.square_at(dir), \
                        piece.opposite_of(dir), piece))

                    elif piece.opposite_of(dir).color == CORNER:
                        goal_squares.append(Goal(piece.square_at(dir), None, \
                        piece))

                # The Piece's side is filled with a Square and a Square
                elif isinstance(piece.square_at(dir), Square) and \
                isinstance(piece.opposite_of(dir), Square):
                    goal_squares.append(Goal(piece.square_at(dir), \
                    piece.opposite_of(dir), piece))

    return goal_squares


# This Function will return a Square in any given Direction unless
# it is Blocked by a Piece or can't be Jumped Over
def get_square(piece, dir, target_color):
    if check_move(piece, dir, target_color) == YES:
        return piece.square_at(dir)

    elif check_move(piece, dir, target_color) == JUMP:
        return piece.square_at(dir).square_at(dir)

    elif check_move(piece, dir, target_color) == NO:
        return  None


# This Function will return a Square that a Piece is standing on
def get_standing_square(piece, board):
    for square in board.squares:
        if piece.x == square.x and piece.y == square.y:
            return square

    return None


# This Function checks if a move is possible for a Piece at any given Direction
def check_move(piece, dir, target_color):
    # If a move is valid
    if check_valid_move(piece, dir):
        # If the move will not eliminate the piece
        if not move_is_eliminated(piece, dir, target_color):
            return YES

    else:
        # If you could jump over
        if check_valid_jump_move(piece, dir, target_color):
            return JUMP

    return NO


# This Function check if a given direction leads to the
# elimination of the given Piece
def move_is_eliminated(piece, dir, target_color):

    if dir == RIGHT or dir == LEFT:
        piece_top_dir = piece.top.square_at(dir)
        piece_bottom_dir = piece.bottom.square_at(dir)
        piece_dir_dir = piece.square_at(dir).square_at(dir)

        if isinstance(piece_top_dir, Piece) and \
        isinstance(piece_bottom_dir, Piece):
            if piece_top_dir.color == target_color or \
            piece_top_dir.color == CORNER and \
            piece_bottom_dir.color == target_color or \
            piece_bottom_dir.color == CORNER:

                if isinstance(piece_top_dir.top, Piece):
                    if piece_top_dir.top.color == WHITE or \
                    piece_top_dir.top.color == CORNER:
                        return False

                elif isinstance(piece_bottom_dir.bottom, Piece):
                    if piece_bottom_dir.bottom.color == WHITE or \
                    piece_bottom_dir.bottom.color == CORNER:
                        return False

                else:
                    return True

        if isinstance(piece_dir_dir, Piece):
            if piece_dir_dir.color == BLACK or piece_dir_dir.color == CORNER:
                if piece.color == BLACK or piece.color == CORNER:
                    return True


    if dir == TOP or dir == BOTTOM:

        piece_dir_left = piece.square_at(dir).left
        piece_dir_right = piece.square_at(dir).right
        piece_dir_dir = piece.square_at(dir).square_at(dir)

        if isinstance(piece_dir_left, Piece) and \
        isinstance(piece_dir_right, Piece):
            if piece_dir_left.color == target_color or \
            piece_dir_left.color == CORNER and \
            piece_dir_right.color == target_color or \
            piece_dir_right.color == CORNER:

                if isinstance(piece_dir_left.left, Piece):
                    if piece_dir_left.left.color == WHITE or \
                    piece_dir_left.left.color == CORNER:
                        return False

                if isinstance(piece_dir_right.right, Piece):
                    if piece_dir_right.right.color == WHITE or \
                    piece_dir_right.right.color == CORNER:
                        return False

                else:
                    return True

        if isinstance(piece_dir_dir, Piece):
            if piece_dir_left.color == BLACK or piece_dir_left.color == CORNER:
                if piece.color == BLACK or piece.color == CORNER:
                    return True

    return False


# This Function returns if a given direction could be jumped over
# and not get eliminated
def check_valid_jump_move(piece, dir, target_color):

    if piece.square_at(dir) and \
    isinstance(piece.square_at(dir).square_at(dir), Square):
        if not move_is_eliminated(piece.square_at(dir), dir, target_color):
            return True

    return False


# This Function checks if a specific direction is a valid move
# Valid moves are determined by Squares
def check_valid_move(piece, dir):

    piece_at_dir = piece.square_at(dir)

    if isinstance(piece_at_dir, Square):
        return True

    return False
