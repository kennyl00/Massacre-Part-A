from board import *

def astar(start_piece, start_square, goal_square, new_board):
    openset = set()
    closedset = set()
    path = [] # to print the path to current state
    openset.add(start_square)

    while not len(openset) == 0:
        # pop a square from openset
        current_square = openset.pop()

        start_piece.x = current_square.x
        start_piece.y = current_square.y

        if start_piece.x == goal_square.x and start_piece.y == goal_square.y:
            while current_square.parent:
                path.append(current_square)
                current_square = current_square.parent
            path.append(current_square)
            return path

        openset.add(get_available_neighbours(start_piece, current_square, new_board, openset, closedset))

        closedset.add(current_square)

        for square in path:
            print(square.x, square.y)
    return


def get_available_neighbours(start_piece, current_square, new_board, openset, closedset):
    # a list of neghbours to be added to openset
    neighbours_to_add = []
    for dir in range(LEFT, BOTTOM + 1):
        # if current_square can move to a neighbour
        if get_square(start_piece, dir, BLACK):
            neighbour = get_square(start_piece, dir, BLACK)
            neighbour.cost_to_move = current_square.cost_to_move + 1
            # if neighbour in the openset and neighbour has a bigger f
            if bigger_than_in_set(neighbour, openset):
                continue
            # if neighbour in the closedset and neighbour has a bigger f
            if bigger_than_in_set(neighbour, closedset):
                continue
            else:
                # set parent and add to openset
                neighbour.parent = current_square
                neighbours_to_add.append(neighbour)

        return neighbours_to_add


def bigger_than_in_set(neighbour, set):
    for square in set:
        # if they have same location and neighbour has a higher f, return True
        if neighbour.x == square.x and neighbour.y == square.y:
            if neighbour.cost_to_move + neighbour.priority >= square.cost_to_move + square.priority:
                return True

    return False


def clear_priority(new_board):
    for piece in new_board.pieces:
        piece.priority = 0

    for square in new_board.pieces:
        square.priority = 0


def clear_parent(new_board):

    for square in new_board.pieces:
        square.parent = None
