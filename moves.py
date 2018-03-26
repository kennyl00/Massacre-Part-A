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

# This function returns a list of Goals
def get_goal_list(board, target_color):

    goal_squares = []

    for piece in board.pieces:
        if piece.color == target_color:
            for dir in range(LEFT, TOP+1):
                # Check Left and Right
                if dir == LEFT:
                    # If LEFT and RIGHT of the Target Piece are Squares
                    if check_move(piece, LEFT, target_color) == YES and check_move(piece, RIGHT, target_color) == YES:
                        goal_squares.append(Goal(piece.square_at(LEFT), piece.square_at(RIGHT), piece))


                    # If the LEFT of Target Piece is Square and the RIGHT is a Piece
                    elif check_move(piece, LEFT, target_color) == YES and isinstance(piece.square_at(RIGHT), Piece):
                        # and if the RIGHT Piece is not a Target
                        if piece.square_at(RIGHT).color == WHITE:
                            goal_squares.append(Goal(piece.square_at(LEFT), piece.square_at(RIGHT), piece))


                        elif piece.square_at(RIGHT).color == CORNER:
                            goal_squares.append(Goal(piece.square_at(LEFT), None, piece))


                    # If the RIGHT of the Target Piece is Square and the LEFT is a Piece
                    elif check_move(piece, RIGHT, target_color) == YES and isinstance(piece.square_at(LEFT), Piece):
                        if piece.square_at(LEFT).color == WHITE:
                            goal_squares.append(Goal(piece.square_at(RIGHT), piece.square_at(LEFT), piece))

                        elif piece.square_at(LEFT).color == CORNER:
                            goal_squares.append(Goal(piece.square_at(RIGHT), None, piece))


                if dir == TOP:
                    if check_move(piece, TOP, target_color) == YES and check_move(piece, BOTTOM, target_color) == YES:
                        goal_squares.append(Goal(piece.square_at(TOP), piece.square_at(BOTTOM), piece))


                    elif check_move(piece, TOP, target_color) == YES and isinstance(piece.square_at(BOTTOM), Piece):
                        if piece.square_at(BOTTOM).color == WHITE:
                            goal_squares.append(Goal(piece.square_at(TOP), piece.square_at(BOTTOM), piece))

                        elif piece.square_at(BOTTOM).color == CORNER:
                            goal_squares.append(Goal(piece.square_at(TOP), None, piece))

                    elif check_move(piece, BOTTOM, target_color) == YES and isinstance(piece.square_at(TOP), Piece):
                        if piece.square_at(TOP).color == WHITE:
                            goal_squares.append(Goal(piece.square_at(BOTTOM), piece.square_at(TOP), piece))

                        elif piece.square_at(TOP).color == CORNER:
                            goal_squares.append(Goal(piece.square_at(BOTTOM), None, piece))

    return goal_squares

# This function will return a Square in any Direction unless it is Blocked by
# a Piece and can't be Jumped Over
def get_square(piece, dir, target_color):
    if check_move(piece, dir, target_color) == YES:
        return piece.square_at(dir)

    elif check_move(piece, dir, target_color) == JUMP:
        return piece.square_at(dir).square_at(dir)

    elif check_move(piece, dir, target_color) == NO:
        return  None

def get_standing_square(piece, board):

    for square in board.squares:
        if piece.x == square.x and piece.y == square.y:
            return square

    return None


def check_move(piece, dir, target_color):
    # First check if the move is possible
    if check_valid_move(piece, dir):
        # Check if move could be eliminated
        if not move_is_eliminated(piece, dir, target_color):
            return YES

    else:
        # Check if a jump move is possible
        if check_valid_jump_move(piece, dir, target_color):
            return JUMP

    return NO


# This function checks if the a move results in the elimination of the Piece
def move_is_eliminated(piece, dir, target_color):
    if dir == RIGHT:
        if isinstance(piece.top_right, Piece) and isinstance(piece.bottom_right, Piece):
            if piece.top_right.color == target_color and piece.bottom_right == target_color:
                return True

    if dir == LEFT:
        if isinstance(piece.top_left, Piece) and isinstance(piece.bottom_left, Piece):
            if piece.top_left.color == target_color and piece.bottom_left.color == target_color:
                return True

    if dir == TOP:
        if isinstance(piece.top_left, Piece) and isinstance(piece.top_right, Piece):
            if piece.top_left.color == target_color and piece.top_right.color == target_color:
                return True

    if dir == BOTTOM:
        if isinstance(piece.bottom_left, Piece) and isinstance(piece.bottom_right, Piece):
            if piece.bottom_left.color == target_color and piece.bottom_right.color == target_color:
                return True

    return False

# This function returns if a specific direction could be jumped over
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
