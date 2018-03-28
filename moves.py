# This file contains functions that deals with movements of the Pieces
# Created by JiaWei and Kenny (20/3/18)

from board import *

# This Function returns all the available moves (including Jumps) of a
# particular colored Piece
def count_legal_moves(new_board, color):
    count = 0
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
    for piece in board.pieces:
        if piece.color == target_color:
            for dir in range(LEFT, TOP+1):

                if isinstance(piece.square_at(dir), Piece) and isinstance(piece.opposite_of(dir), Square):
                    if piece.square_at(dir).color == WHITE:
                        goal_squares.append(Goal(piece.square_at(dir), piece.opposite_of(dir), piece))

                    elif piece.square_at(dir).color == CORNER:
                        goal_squares.append(Goal(piece.opposite_of(dir), None, piece))

                elif isinstance(piece.square_at(dir), Square) and isinstance(piece.opposite_of(dir), Piece):
                    if piece.opposite_of(dir).color == WHITE:
                        goal_squares.append(Goal(piece.square_at(dir), piece.opposite_of(dir), piece))

                    elif piece.opposite_of(dir).color == CORNER:
                        goal_squares.append(Goal(piece.square_at(dir), None, piece))


                elif isinstance(piece.square_at(dir), Square) and isinstance(piece.opposite_of(dir), Square):
                    goal_squares.append(Goal(piece.square_at(dir), piece.opposite_of(dir), piece))
                    break

    return goal_squares

# This function will return a Square in any given Direction unless
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

# This function checks if a move is possible for a Piece at any given Direction
def check_move(piece, dir, target_color):
    if check_valid_move(piece, dir):
        if not move_is_eliminated(piece, dir, target_color):
            return YES

    else:
        if check_valid_jump_move(piece, dir, target_color):
            return JUMP

    return NO


# This Function check if a given direction leads to the
# elimination of the given Piece
def move_is_eliminated(piece, dir, target_color):
    if dir == RIGHT:

        if isinstance(piece.top_right, Piece) and isinstance(piece.bottom_right, Piece):
            if piece.top_right.color == target_color or piece.top_right.color == CORNER and \
                piece.bottom_right.color == target_color or piece.bottom_right.color == CORNER:

                if isinstance(piece.top_right.top, Piece):
                    if piece.top_right.top.color == WHITE or piece.top_right.top.color == CORNER:
                        return False

                elif isinstance(piece.bottom_right.bottom, Piece):
                    if piece.bottom_right.bottom.color == WHITE or piece.bottom_right.bottom.color == CORNER:
                        return False


                else:
                    return True

        if isinstance(piece.right.right, Piece):
            if piece.right.right.color == BLACK or piece.right.right.color == CORNER:
                if piece.color == BLACK or piece.color == CORNER:
                    return True

    if dir == LEFT:
        if isinstance(piece.top_left, Piece) and isinstance(piece.bottom_left, Piece):
            if piece.top_left.color == target_color or piece.top_left.color == CORNER and \
                piece.bottom_left.color == target_color or piece.bottom_left.color == CORNER:

                if isinstance(piece.top_left.top, Piece):
                    if piece.top_left.top.color == WHITE or piece.top_left.color == CORNER:
                        return False

                elif isinstance(piece.bottom_left.bottom, Piece):
                    if piece.bottom_left.bottom.color == WHITE or piece.bottom_left.bottom.color == CORNER:
                        return False

                else:
                    return True

        if isinstance(piece.left.left, Piece):
            if piece.left.left.color == BLACK or piece.left.left.color == CORNER:
                if piece.color == BLACK or piece.color == CORNER:
                    return True


    if dir == TOP:
        if isinstance(piece.top_left, Piece) and isinstance(piece.top_right, Piece):
            if piece.top_left.color == target_color or piece.top_left.color == CORNER \
                and piece.top_right.color == target_color or piece.top_right.color == CORNER:

                if isinstance(piece.top_left.left, Piece):
                    if piece.top_left.left.color == WHITE or piece.top_left.left.color == CORNER:

                        return False

                if isinstance(piece.top_right.right, Piece):
                    if piece.top_right.right.color == WHITE or piece.top_right.right.color == CORNER:
                        return False
                else:
                    return True

        if isinstance(piece.top.top, Piece):
            if piece.top.top.color == BLACK or piece.top.top.color == CORNER:
                if piece.color == BLACK or piece.color == CORNER:
                    return True



    if dir == BOTTOM:
        if isinstance(piece.bottom_left, Piece) and isinstance(piece.bottom_right, Piece):
            if piece.bottom_left.color == target_color or piece.bottom_left.color == CORNER \
                and piece.bottom_right.color == target_color or piece.bottom_right.color == CORNER:

                if isinstance(piece.bottom_left.left, Piece):
                    if piece.bottom_left.left.color == WHITE or piece.bottom_left.left.color == CORNER:
                        return False

                if isinstance(piece.bottom_right.right, Piece):
                    if piece.bottom_right.right.color == WHITE or piece.bottom_right.right.color == CORNER:
                        return False
                else:
                    return True

        if isinstance(piece.bottom.bottom, Piece):
            if piece.bottom.bottom.color == BLACK or piece.bottom.bottom.color == CORNER:
                if piece.color == BLACK or piece.color == CORNER:
                    return True

    return False

# This Function returns if a given direction could be jumped over
# and not get eliminated
def check_valid_jump_move(piece, dir, target_color):
    if dir == LEFT:
        if piece.left and isinstance(piece.left.square_at(LEFT), Square):
            if not move_is_eliminated(piece.left, LEFT, target_color):
                return True

    if dir == RIGHT:
        if piece.right and isinstance(piece.right.square_at(RIGHT), Square):
            if not move_is_eliminated(piece.right, RIGHT, target_color):
                return True

    if dir == TOP:
        if piece.top and isinstance(piece.top.square_at(TOP), Square):
            if not move_is_eliminated(piece.top, TOP, target_color):
                return True

    if dir == BOTTOM:
        if piece.bottom and isinstance(piece.bottom.square_at(BOTTOM), Square):
            if not move_is_eliminated(piece.bottom, BOTTOM, target_color):
                return True

    return False


# This Function checks if a specific direction is a valid move
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
