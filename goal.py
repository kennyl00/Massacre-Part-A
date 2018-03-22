
from board import *

def determinate_goals(board):
    # Goal Squares are defined as Squares the would lead to the elimination of
    # Pieces
    # Remove White Piece neighbours of all pieces
    num_white = num_white_pieces(new_board)
    for piece in new_board.pieces:
        remove_neighbours(new_board, piece, W)

    # two white pieces is sufficient to complete the all targets
    if num_white > 2:
        num_white = 2

    # List of Goal Squares
    goal_squares = []

    # loop over all neighbours of black pieces and use limited dps to search
    # desirable destinations
    for piece in new_board.pieces:
        if piece.color is B:
        	# loop over directions both on clockwise and anticlockwise
            for dir in range(LEFT, LEFT2 + 1):
            	# only squares could be destinations
                if piece.square_at(dir) and isinstance(piece.square_at(dir), Square):
                    limited_dfs(new_board, num_white, goal_squares, piece.square_at(dir))

    return goal_squares


# This Function utilises Limited Depth First Search
def limited_dfs(new_board, depth, visited_list, goal_squares, position):
	# if a solution if found, return the goal_squares
    if find_solution(new_board):
        return goal_squares

    # if haven't reach limit
    if not depth == 0:
    	# create a new white piece at the required position
        position = Piece(position.v_location, position.h_location, W)
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


# if all black pieces are eliminated
def find_solution(new_board):
    for piece in new_board.pieces:
        if piece.color is B:
            return False
    return True


def set_neighbour(piece, dir, list):
    if dir == LEFT and piece.left is None:
        piece.left = occupied(piece, dir, list)
    if dir == RIGHT and piece.right is None:
        piece.right = occupied(piece, dir, list)
    if dir == TOP and piece.top is None:
        piece.top = occupied(piece, dir, list)
    if dir == BOTTOM and piece.bottom is None:
        piece.bottom = occupied(piece, dir, list)


# remove all neighbourhood for a certain color or a certain piecee\
def remove_neighbours(new_board, this_piece, color):
    for piece in new_board.pieces:
    	# loop over directions both on clockwise and anticlockwise
        for dir in range(LEFT, LEFT2 + 1):
            if isinstance(piece.square_at(dir), Piece) and piece.square_at(dir).color is color:
                if piece.square_at(dir).v_location == this_piece.v_location and \
                        piece.square_at(dir).h_location == this_piece.h_location:
                        # create a square if a piece is reomved and construct neighbourhood
                        new_square = Square(piece.square_at(dir).v_location, piece.square_at(dir).h_location)
                        piece.set_neighbour(dir, new_square)


# This function returns the number of White Pieces on any given Board
def num_white_pieces(board):
    num = 0
    for piece in board.pieces:
        if piece.color is WHITE:
            num += 1
    return num
