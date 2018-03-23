from board import *
from neighbour import *

def find_solution(board, target_color, fighter_color):

    # Fighters eliminates Targets
    # Get the number of Target Pieces (e.g. Black)
    target_num = num_pieces(board, target_color)
    target_list = get_pieces(board, target_color)

    # Get all the Fighter Pieces (e.g. White)
    fighter_list = get_pieces(board, fighter_color)


    while target_num > 0:

        # For every Piece in fighter_list
        for piece in fighter_list:

            # Get the available Moves or Jumps of a Piece
            move_list = []
            jump_list = []

            for dir in range(LEFT, BOTTOM+1):

                if check_valid_move(piece, dir):

                    move = Move(piece.square_at(dir).v_location, piece.square_at(dir.h_location))

                    move_list.append(move)

                else:
                    if check_valid_jump_move(piece, dir):
                        jump_list.append(get_jump_move(piece,dir))


            # For every Piece's valid Moves or Jumps, determine the utility of that Move
            for move in move_list + jump_list:
                # Check the surrounding of each Move
                for dir in range(LEFT, BOTTOM+1):
                    # Add the utility accordinly, the higher the utility, the more Target pieces is at the surrounding
                    if occupied(move, dir, target_list):
                        move.utility += 1;

            # Move the Piece to the highest Utility move
                # When moving create Piece at the Move and create Square at the Piece
                # Make sure the move doesn't get eliminated

            # Check the game if any of the Target has been eliminated





def get_jump_move(piece, dir):

    if dir == LEFT:
        return Move(piece.left.left.v_location, piece.left.left.h_location)

    if dir == RIGHT:
        return Move(piece.right.right.v_location, piece.right.right.h_location)

    if dir == TOP:
        return Move(piece.top.top.v_location, piece.top.top.h_location)

    if dir == BOTTOM:
        return Move(piece.bottom.bottom.v_location, piece.bottom.bottom.h_location)


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


# This function returns a list of required Pieces by Color
def get_pieces(board, color):

    list = []

    for piece in board.pieces:
        if piece.color is color:
            list.append(piece)

    return list



# This function returns the number of a Colored Piece on the Board
def num_pieces(board, color):
    num = 0
    for piece in board.pieces:
        if piece.color is color:
            num += 1

    return num
