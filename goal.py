
from board import *

# This function returns a List filled with Square positions that would lead to
# the elimination of a Target Piece
def determinate_goals(board, target_color):

    depth = None;

    # If the Target is Black
    if target_color is BLACK:
        # Get the number of White Pieces on the Board
        depth = num_pieces(board, WHITE)
        # Remove all the White Neighbours from Black Pieces
        remove_neighbours(board, BLACK, WHITE)

    # If the Target is White
    else:
        # Get the number of Black Pieces on the Board
        depth = num_pieces(board, BLACK)
        # Remove all the Black Neighbours from White Pieces
        remove_neighbours(board, WHITE, BLACK)

    # We need at most 2 Pieces to eliminate all targets
    if depth > 2:
        depth = 2

    # List of Goal Squares
    # They are defined as Squares the would lead to the elimination of a Piece
    goal_squares = []

    # For every Piece on the Board
    for piece in board.pieces:

        # If the Piece is Black
        if piece.color is BLACK:

            # Loop over all the Directions of said Piece
            for dir in range(LEFT, BOTTOM):

                # Get the Object at that Direction
                dir_obj = piece.square_at(dir)

            	# Check if the Direction is a Square
                if dir_obj and isinstance(dir_obj, Square):

                    # Use Limited Depth First Search
                    limited_dfs(board, depth, goal_squares, dir_obj, target_color)

    return goal_squares

# Checks the Board if the target Piece still exist
def find_solution(new_board, target_color):

    # For every Piece on the Board
    for piece in new_board.pieces:

        # If the Piece is Black
        if piece.color is target_color:

            # If there is still a target Piece
            return False

    # If all the target Piece has been eliminated from the Board
    # Return true
    return True


def limited_dfs(new_board, depth, visited_list, goal_squares, position, target_color):

    # If all target Piece has been wiped out from the Board
    if find_solution(new_board, target_color):
        return goal_squares

    # If Depth limit has not been met
    if not depth == 0:

        # Create a new White Piece at the Required Position
        position = Piece(position.v_location, position.h_location, WHITE)

        # construst neighbourhood for the white piece
        for piece in new_board.pieces:
            for dir in range(LEFT, LEFT2 + 1):
                if piece.square_at(dir):
                    if piece.square_at(dir).v_location == position.v_location and \
                            piece.square_at(dir).h_location == position.h_location:
                        piece.set_neighbour(dir, position)
                        position.set_neighbour(dir, piece)

        # balck pieces which are required to be removed
        reduced_pieces = []

        # if a black piece is removed
        for piece in new_board.pieces:
            if get_eliminated(piece) and piece.color is B:
            	# check this black piece's neighbours
                black_piece_reduced(piece, goal_squares)
                reduced_pieces.append(piece)

        # remove the black pieces
        new_board.pieces = list(set(new_board.pieces) - set(reduced_pieces))
        # remove all neighbourhood of these black pieses
        for piece in reduced_pieces:
            remove_neighbours(new_board, piece, B)

        # if the white piece is removed, return None
        if get_eliminated(position):
        	# remove neighbourhood of the white piece
            remove_neighbours(new_board, position, W)
            for i in reduced_pieces:
            	# recover everything
                new_board.pieces.append(i)
                goal_squares.pop()
            return

        for piece in new_board.pieces:
            if piece.color is B:
                for dir in range(LEFT, LEFT2 + 1):
                    if piece.square_at(dir) and isinstance(piece.square_at(dir), Square):
                        limited_dfs(new_board, depth - 1, goal_squares, piece.square_at(dir))

    # if reaches to limit, return None
    else:
        return


# Remove a Colored neighbour
def remove_neighbours(board, piece_color, neighbour_color):

    # For every Piece on the board
    for piece in board.pieces:

        if piece.color is piece_color:

            # For every Direction of the Piece
            for dir in range(LEFT, BOTTOM+1):

                # Get the Object at that Direction
                neighbour = piece.square_at(dir)

                # If the Object is a Piece and the Color is right
                if isinstance(neighbour, Piece) and neighbour.color is neighbour_color:

                    # Create a new Square at that location
                    if dir == LEFT:
                        new_square = Square(piece.left.v_location, piece.left.h_location)

                    if dir == TOP:
                        new_square = Square(piece.top.v_location, piece.top.h_location)

                    if dir == RIGHT:
                        new_square = Square(piece.right.v_location, piece.right.h_location)

                    if dir == BOTTOM:
                        new_square = Square(piece.bottom.v_location, piece.bottom.h_location)

                    # Replace the Piece's Direction from a Colored Piece to a Square
                    piece.set_neighbour(dir, new_square)



# This function returns the number of a Colored Piece on the Board
def num_white_pieces(board, color):
    num = 0
    for piece in board.pieces:
        if piece.color is color:
            num += 1
    return num

def set_neighbour(piece, dir, list):
    if dir == LEFT and piece.left is None:
        piece.left = occupied(piece, dir, list)
    if dir == RIGHT and piece.right is None:
        piece.right = occupied(piece, dir, list)
    if dir == TOP and piece.top is None:
        piece.top = occupied(piece, dir, list)
    if dir == BOTTOM and piece.bottom is None:
        piece.bottom = occupied(piece, dir, list)
