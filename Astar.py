from board import *
from moves import *
from neighbour import *
from elimination import *

def astar(start_piece, start_square, goal_square, new_board, target_color):
    openset = []
    closedset = []
    path = [] # to print the path to current state
    openset.append(start_square)

    # while there are more squares that can be expanded
    while not len(openset) == 0:
        # get the square with smallest f in openset
        current_square = find_min_f(openset)
        # move the piece to that square
        move(start_piece, current_square, new_board)
        get_eliminated(new_board, target_color)
        # if a solution is found
        if start_piece.x == goal_square.x and start_piece.y == goal_square.y:
            # track back all parents and put these squares in path
            while current_square.parent:

                path.append(current_square)
                current_square = current_square.parent

            path.append(current_square)
            return path

        # find all neighbours that meet requirements
        openset.extend(get_available_neighbours(start_piece, current_square, \
        new_board, openset, closedset))

        # add the current_square to closedset
        closedset.append(current_square)

    return


# return all neighbours that meet requirements
def get_available_neighbours(start_piece, current_square, new_board, openset, closedset):
    # a list of neghbours to be added to openset
    neighbours_to_add = []

    for dir in range(LEFT, BOTTOM + 1):
        neighbour = get_square(start_piece, dir, BLACK)
        # if current_square can move to a neighbour
        if neighbour:
            # update cost_to_move
            neighbour.cost_to_move = current_square.cost_to_move + 1
            # set f of neighbour square
            neighbour.f = neighbour.cost_to_move + neighbour.priority
            # if a neighbour with same location is in the openset
            # and this neighbour has a bigger f, skip this neighbour
            if bigger_than_in_set(neighbour, openset):
                continue
            # if a neighbour with same location is in the closedset
            # and this neighbour has a bigger f, skip this neighbour
            if bigger_than_in_set(neighbour, closedset):
                continue
            else:
                print('H')
                # set parent and add to openset
                neighbour.parent = current_square
                neighbours_to_add.append(neighbour)

    return neighbours_to_add

# check if there is a neighbour in set with same location and lower f
def bigger_than_in_set(neighbour, set):
    for square in set:

        if neighbour.x == square.x and neighbour.y == square.y:
            if neighbour.cost_to_move + neighbour.priority >= \
                square.cost_to_move + square.priority:
                return True

    return False


# clear all priority
def clear_priority(new_board):
    for piece in new_board.pieces:
        piece.priority = 0

    for square in new_board.squares:
        square.priority = 0


# clear all parent
def clear_parent(new_board):
    for square in new_board.squares:
        square.parent = None


# clear all cost_to_move
def clear_cost_to_move(new_board):
    for square in new_board.squares:
        square.cost_to_move = 0


# put target piece to the location of current_square
def move(start_piece, current_square, new_board):
    start_piece.x = current_square.x
    start_piece.y = current_square.y

    find_neighbour(new_board)


# find square with the smallest f in set
def find_min_f(openset):
    min = MAXINT
    index = 0
    for i in range(0, len(openset)):
        buffer = openset[i].f
        if buffer < min:
            min = buffer
            index = i

    return openset.pop(index)
