
from board import *


def determinate_goals(board):
    # Goal Squares are defined as Squares the would lead to the elimination of
    # Pieces

    # List of Goal Squares
    goal_squares = []

    # Get the number of White Pieces on the Board
    num_white = num_white_pieces(board)

    # Remove the White Pieces from the Board
    board.pieces = [piece for piece in board.pieces if piece.color != WHITE]

    # Create a List with the size of the number of White Pieces
    visited_list = [None] * (num_white + 1)

    limited_dfs(board, num_white, visited_list, goal_squares)



# This Function utilises Limited Depth First Search
def limited_dfs(new_board, depth, visited_list, goal_squares):

    if find_solution(new_board, visited_list):
        del goal_squares[:]
        for i in visited_list:
            if i and i not in goal_squares:
                goal_squares.append(i)

        return visited_list

    if not depth == 0:

        set_piece_neighbour(new_board)

        remove_white_neighbours(new_board)

        clear_priority(new_board)
        set_priority(new_board)

        for square in new_board.squares:
            if not square.priority == 0 and square not in visited_list:
                visited_list[depth] = square

                limited_dfs(new_board, depth - 1, visited_list, goal_squares)

    else:

        return


def find_solution(board, visited_list):
    # For every Piece on the Board, mark them Unremovable
    for piece in board.pieces:
        piece.removable = False

    # For every Piece on the Board
    for piece in board.pieces:

        # If the Piece is Black
        if piece.color is BLACK:

            # For every Direction of the Black Piece
            for dir in range(LEFT, BOTTOM + 1):

                # Get the Object at a Direction (TOP, BOTTOM, LEFT, RIGHT)
                dir_neighbour = peice.get_neighbour(dir)
                # Get the Object in the Opposite Direction (BOTTOM, TOP, RIGHT, LEFT)
                opp_neighbour = piece.get_opposite_neighbour(dir)

                # If the Piece is sandwhiched between 2 Objects
                if dir_neighbour and opp_neighbour:

                    # If the Object at that Direction is a Piece
                    if isinstance(dir_neighbour, Piece):

                        # Check if the Piece is a Corner
                        if dir_neighbour is CORNER:

                            # If the opposite Direction Piece is a Square
                            # and if it is in the visited_list
                            # mark the Piece removable and stop checking
                            # other Directions
                            if isinstance(opp_neighbour, Square) and opp_neighbour in visited_list:
                                piece.removable = True
                                break

                    # If the Object at that Direction is not a Piece
                    else:

                        # Check if it is in the visited_list
                        if dir_neighbour in visited_list:

                            # Check if the opposite Object is a Piece and if it is a Corner
                            if isinstance(opp_neighbour, Piece) and opp_neighbour.color is CORNER:

                                # Mark the Piece removable
                                piece.removable = True
                                break

                            # Check if the opposite Object is a Square and
                            # if it is in the visited_list
                            if isinstance(opp_neighbour, Square) and opp_neighbour in visited_list:
                                # Mark the piece removeable
                                piece.removable = True
                                break



    for piece in new_board.pieces:
        if piece.color is B and piece.removable is False:

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

def remove_white_neighbours(new_board):
    for piece in new_board.pieces:
        for dir in range(LEFT, BOTTOM + 1):
            if isinstance(piece.square_at(dir), Piece) and piece.square_at(dir).color is W:
                piece.set_neighbour(dir, None)


# these two priority methods slow down limited DFS a lot
def clear_priority(new_board):
    for piece in new_board.pieces:
        if piece.color is B or piece.color is X:
            for dir in range(LEFT, BOTTOM + 1):
                if isinstance(piece.square_at(dir), Square):
                    piece.square_at(dir).priority = 0


def set_priority(new_board):
    for piece in new_board.pieces:
        if piece.color is B or piece.color is X:
            for dir in range(LEFT, BOTTOM + 1):
                if isinstance(piece.square_at(dir), Square):
                    piece.square_at(dir).priority += 1

# This function returns the number of White Pieces on any given Board
def num_white_pieces(board):
    num = 0
    for piece in board.pieces:
        if piece.color is WHITE:
            num += 1
    return num
