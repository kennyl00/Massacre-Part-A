from board import *

# This function returns a List filled with Square positions that would lead to
# the elimination of a Target Piece
def determinate_goals(board, target_color):
    depth = None

    # If the Target is Black
    if target_color is BLACK:
        # Get the number of White Pieces on the Board
        depth = num_pieces(board, WHITE)
        # Remove all the White Neighbours from Black Pieces
        for piece in board.pieces:
            remove_neighbours(board, piece, WHITE)

       # Get the number of Black Pieces on the Board
        num_black = num_pieces(board, BLACK)

        # We need at most 2 Pieces to eliminate all targets
        if depth > 2:
            depth = 2

        # List of Goal Squares
        # They are defined as Squares the would lead to the elimination of a Piece
        goal_squares = []
        # attemp to remove all black pieces on board
        while num_black != 0:
            # For every Piece on the Board
            for piece in board.pieces:

                # If the Piece is Black
                if piece.color is BLACK:

                    # Loop over all the Directions of said Piece
                    for dir in range(LEFT, BOTTOM + 1):

                        # Get the Object at that Direction
                        dir_obj = piece.square_at(dir)

                        # Check if the Direction is a Square
                        if dir_obj and isinstance(dir_obj, Square):
                            # Use Limited Depth First Search
                            position = Piece(dir_obj.x, dir_obj.y, WHITE)
                            limited_dfs(board, depth, goal_squares, position, None, target_color)
                            remove_neighbours(board, position, BLACK)
                            # check how many black piece left on board
                            num_black = num_pieces(board, BLACK)


        print('result')
        for i in goal_squares:

            print(i.piece1.x, i.piece1.y)
            print(i.piece2.x, i.piece2.y)

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



# goes limited dfs on all required positions
def limited_dfs(new_board, depth, goal_squares, position, old_position, target_color):

    # If all target Piece has been wiped out from the Board
    if find_solution(new_board, target_color):
        return goal_squares

    # If Depth limit has not been met
    if not depth == 0:

        # construct neighbourhood for the white piece
        for piece in new_board.pieces:
            # loop over every direction of every piece
            for dir in range(LEFT, BOTTOM + 1):
                if piece.square_at(dir):
                    # if the constructed piece has the same location as one of the goal_square
                    if piece.square_at(dir).x == position.x and \
                            piece.square_at(dir).y == position.y:
                        # build neighbourhood
                        piece.set_neighbour(dir, position)
                        position.set_neighbour(dir, piece)

        # black pieces which are required to be removed
        reduced_pieces = []

        # if a black piece is removed
        for piece in new_board.pieces:
            if get_eliminated(piece) and piece.color is BLACK:
                # check this black piece's neighbours
                black_piece_reduced(piece, goal_squares)
                reduced_pieces.append(piece)

        # remove the black pieces
        new_board.pieces = list(set(new_board.pieces) - set(reduced_pieces))
        # remove all neighbourhood of these black pieses
        for piece in reduced_pieces:
            remove_neighbours(new_board, piece, BLACK)
            # remove neighbourhood of black pieces from position piece
            for dir in range(LEFT, BOTTOM + 1):
                if position.square_at(dir) == piece:
                    position.set_neighbour(dir, Square(piece.x, piece.y))

        # if the white piece is removed, return None
        if get_eliminated(position) or get_eliminated(old_position) and depth == 1:
            # remove neighbourhood of the position piece
            remove_neighbours(new_board, position, BLACK)
            # remove neighbourhood of another position piece
            if old_position:
                remove_neighbours(new_board, old_position, BLACK)

            for i in reduced_pieces:

                goal_squares.pop()
                # reset neighbourhood of previousely removed piece
                for piece in new_board.pieces:
                    for dir in range(LEFT, BOTTOM + 1):
                        if piece.square_at(dir):
                            if piece.square_at(dir).x == i.x and \
                                    piece.square_at(dir).y == i.y:
                                piece.set_neighbour(dir, i)
                new_board.pieces.append(i)
            return


        # go to the second piece
        for piece in new_board.pieces:
            if piece.color is BLACK:
                for dir in range(LEFT, BOTTOM + 1):
                    if piece.square_at(dir) and isinstance(piece.square_at(dir), Square):
                        dir_obj = piece.square_at(dir)

                        # Create a new White Piece at the Required Position
                        position2 = Piece(dir_obj.x, dir_obj.y, WHITE)

                        limited_dfs(new_board, depth - 1, goal_squares, position2, position, target_color)
                        remove_neighbours(new_board, position2, BLACK)

    # if reaches to limit, return None
    else:
        return

# Remove a Colored neighbour
def remove_neighbours(board, this_piece, color_to_remove):

    # For every Piece on the board
    for piece in board.pieces:
        if piece.color is color_to_remove:
            for dir in range(LEFT, BOTTOM + 1):
                # if the removed piece has the same location as a neighbour of a piece
                if piece.square_at(dir) and piece.square_at(dir).x == this_piece.x and \
                        piece.square_at(dir).y == this_piece.y:
                        # set the square of the same location on board as a neighbour
                        for square in board.squares:
                            if square and square.x == this_piece.x and \
                                    square.y == this_piece.y:
                                piece.set_neighbour(dir, square)


# This function returns the number of a Colored Piece on the Board
def num_pieces(board, color):
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


# if a black piece is removed
def black_piece_reduced(piece, visited_list):
    goal = Goals()
    for dir in range(LEFT, BOTTOM + 1):
        # if both neighbour pieces are white add both to list
        if isinstance(piece.square_at(dir), Piece) and isinstance(piece.opposite_of(dir), Piece):
            if piece.square_at(dir).color is WHITE and piece.opposite_of(dir).color is WHITE:
                goal.set_piece1(Piece(piece.square_at(dir).x, piece.square_at(dir).y, WHITE))
                goal.set_piece2(Piece(piece.opposite_of(dir).x, piece.opposite_of(dir).y, WHITE))

            if piece.square_at(dir).color is CORNER and piece.opposite_of(dir).color is WHITE:
                goal.set_piece1(Piece(piece.opposite_of(dir).x, piece.opposite_of(dir).y, WHITE))

            if piece.square_at(dir).color is WHITE and piece.opposite_of(dir).color is CORNER:
                goal.set_piece2(Piece(piece.square_at(dir).x, piece.square_at(dir).y, WHITE))

    visited_list.append(goal)


# check if one piece can be eliminated
def get_eliminated(piece):
    if piece:
        for dir in range(LEFT, BOTTOM + 1):
            if isinstance(piece.square_at(dir), Piece) and isinstance(piece.opposite_of(dir), Piece):
                col1 = piece.square_at(dir)
                col2 = piece.opposite_of(dir)
                if piece.color is not col1.color and piece.color is not col2.color:

                    return True
    return False


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
