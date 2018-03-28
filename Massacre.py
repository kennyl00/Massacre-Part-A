# This File contains functions that deploys each Piece to a Location

from board import *
from random import shuffle
from neighbour import *
from moves import *
from Astar import *
from elimination import *

# this function print all movement of whites that leads to
# elimination of all black pieces
def Massacre(new_board, target_color):
    # while there are black pieces on board
    while not isEliminated(new_board, target_color):
        # reconstruct neighbourhood of all pieces and squares
        find_neighbour(new_board)
        goal_list = []
        # get current avaliable squares that white pieces can move in
        goal_list = get_goal_list(new_board, BLACK)
        goal = goal_list.pop(0)

        # find the current goals from list can be occupied by white pieces
        # and it will not make white pieces removed
        while not is_goal_achievable(new_board, goal):
            goal_list.append(goal)
            goal = goal_list.pop(0)
            continue

        # if there are two goals, two white pieces are needed
        if goal.square1 and goal.square2:
            goal_square1 = goal.square1
            goal_square2 = goal.square2
            # if goal square1 needs to be occupied first
            if goal.first_to_fit == 1:
                # move one white piece to goal square1
                piece_to_square(new_board, goal_square1, target_color)

                if isEliminated(new_board, target_color):
                    break

                # move another white piece to goal square1
                piece_to_square(new_board,goal_square2, target_color)
                # eliminate this goal
                reset_piece(new_board, goal)
            # if goal square1 needs to be occupied first
            # move to goal square2 first
            elif goal.first_to_fit == 2:
                piece_to_square(new_board, goal_square2, target_color)
                if isEliminated(new_board, target_color):
                    break
                piece_to_square(new_board, goal_square1, target_color)
                reset_piece(new_board, goal)

        # if there is only one goal square
        else:
            goal_square1 = goal.square1
            piece_to_square(new_board,goal_square1, target_color)
            reset_piece(new_board, goal)


# make the nearest moveable white piece of a goal square to that square
def piece_to_square(new_board, goal_square, target_color):
    # set heuristics(priority) of the whole board
    goal_square.set_priority(new_board)
    # pick the nearest white piece
    start_piece = get_nearest_piece(new_board, WHITE)
    if start_piece:
        # find the start square according to start piece
        start_square = get_standing_square(start_piece, new_board)
        # find path with Astar search
        path = astar(start_piece, start_square, goal_square, new_board, \
        target_color)
        # print out path
        print_path(path)
        # set the moved white piece to be unmovable
        start_piece.moveable = False
        # refresh whole board
        refresh(new_board)


# print the move path of white piece
def print_path(path):
    square1 = None
    square2 = None
    if path:
        path.reverse()
        for square in path:

            if square1:
                square2 = square
            # print out one step of a white piece
            if square1 and square2:
                print('({},{}) -> ({},{})'.format(square1.y, square1.x, \
                square2.y, square2.x))
                square1 = None
                square2 = None

            square1 = square

        return True

    else:
        return False


# remove the target black piece from board
def reset_piece(new_board, goal):

    target_piece = goal.piece_to_eliminate

    for dir in range(LEFT, TOP + 1):
        if target_piece.square_at(dir) and target_piece.opposite_of(dir):

            if isinstance(target_piece.square_at(dir), Piece) and \
                not target_piece.square_at(dir).color == CORNER:
                # set piece to be moveable
                target_piece.square_at(dir).moveable = True

            if isinstance(target_piece.opposite_of(dir), Piece) and \
                not target_piece.opposite_of(dir).color == CORNER:

                target_piece.opposite_of(dir).moveable = True



def refresh(new_board):
    # reset priority of square
    clear_priority(new_board)
    # reset cost_to_move of square
    clear_cost_to_move(new_board)
    # reset parent of square
    clear_parent(new_board)
    # reconstruct neighbourhood
    find_neighbour(new_board)


# check if there is any piece of certain color on board
def isEliminated(board, color):

    for piece in board.pieces:

        if piece.color == color:
            return False

    return True


# find the nearest moveable piece of the target
def get_nearest_piece(board, color):

    min_priority = MAXINT;
    min_priority_piece = None

    for piece in board.pieces:
        # check color and if it can move
        if piece.color == color and piece.moveable == True:
            if piece.priority < min_priority:

                min_priority_piece = piece
                min_priority = piece.priority

    return min_priority_piece
