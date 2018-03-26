from board import *
from random import shuffle
from neighbour import *
from moves import *
from Astar import *

def Massacre(new_board, target_color, goal_list):



    # While the goal list is not empty

    while not isEliminated(new_board, BLACK):
        goal = goal_list.pop(0)

        while not is_goal_achievable(new_board, goal):
            goal_list.append(goal)
            goal = goal_list.pop(0)
            continue


        if goal.square1 and goal.square2:
            goal_square1 = goal.square1
            goal_square2 = goal.square2

            # Check Which Goal Squares to go first
            if goal.first_to_fit == 1:
                goal_square1.set_priority(new_board)
            elif goal.first_to_fit == 2:
                goal_square2.set_priority(new_board)


            # Get Closest White Piece and Square
            start_piece = get_nearest_piece(new_board, WHITE)
            print('start_piece', start_piece.y, start_piece.x)
            start_square = get_standing_square(start_piece, new_board)

            path = []

            if goal.first_to_fit == 1:
                path = astar(start_piece, start_square, goal_square1, new_board)
                print(path)
                start_piece.moveable = False
                path = astar(start_piece, start_square, goal_square2, new_board)
                print(path)
                start_piece.moveable = False
                eliminate(new_board, goal)



            elif goal.first_to_fit == 2:
                path = astar(start_piece, start_square, goal_square2, new_board)
                print(path)
                path = astar(start_piece, start_square, goal_square1, new_board)
                print(path)
                start_piece.moveable = False
                eliminate(new_board, goal)


        else:
            goal_square1 = goal.square1
            goal_square1.set_priority(new_board)
            start_piece = get_nearest_piece(new_board, WHITE)
            start_square = get_standing_square(start_piece, new_board)

            path = []
            path = astar(start_piece, start_square, goal_square1, new_board)
            print(path)
            start_piece.moveable = False
            eliminate(new_board, goal)

        refresh(new_board)


def eliminate(new_board, goal):

    target_piece = goal.piece_to_eliminate

    for dir in range(LEFT, TOP+1):

        if target_piece.square_at(dir) and target_piece.opposite_of(dir):
            if isinstance(target_piece.square_at(dir), Piece) and \
                target_piece.square_at(dir).color == CORNER:
                target_piece.square_at(dir).moveable = True

            if isinstance(target_piece.opposite_of(dir), Piece) and \
                target_piece.opposite_of(dir).color == CORNER:
                target_piece.opposite_of(dir).moveable = True


    new_board.pieces.remove(goal.piece_to_eliminate)



def refresh(new_board):
    clear_priority(new_board)
    clear_cost_to_move(new_board)
    clear_parent(new_board)
    find_neighbour(new_board)


def isEliminated(board, color):

    for piece in board.pieces:

        if piece.color == color:
            return False

    return True


def get_nearest_piece(board, color):

    min_priority = MAXINT;
    min_priority_piece = None

    for piece in board.pieces:
        if piece.color == color:
            if piece.priority < min_priority:
                min_priority_piece = piece
                min_priority = piece.priority

    return min_priority_piece


# check whether goal squares are already occupied by white piece on board
def occuppied_by_white(new_board, goal):
    for piece in new_board.pieces:
        if goal.square1 and goal.square1.x == piece.x and goal.square1.y == piece.y:
            goal.square1_occupied_by_white == True
        if goal.square2 and goal.square2.x == piece.x and goal.square2.y == piece.y:
            goal.square1_occupied_by_white == True

# check whether a set of squares are reachable
def is_goal_achievable(new_board, goal):

    eliminated_pieces = []
    # if both are not None
    if goal.square1 and goal.square2:
        # check wheter a goal square is occupied by a white piece
        occuppied_by_white(new_board, goal)

        # if both are not occupied by white piece, under this condition
        # one white piece will not be sufficient to remove black piece
        if not goal.square1_occupied_by_white and not goal.square2_occupied_by_white:
            # create two new pieces at goal square positions
            new_piece1 = Piece(goal.square1.x, goal.square1.y, WHITE)
            new_piece2 = Piece(goal.square2.x, goal.square2.y, WHITE)
            # put piece1 on board
            new_board.pieces.append(new_piece1)
            # get all pieces eliminated from board
            eliminated_black_and_white(new_board, eliminated_pieces)
            # if the piece1 is eliminated
            if eliminated_pieces_color(eliminated_pieces, WHITE):
                # reset board
                reset_board(new_piece1, new_piece2, eliminated_pieces, new_board)
                # put piece2
                new_board.pieces.append(new_piece2)
                # get all pieces eliminated from board
                eliminated_black_and_white(new_board, eliminated_pieces)
                # if the new_piece2 is eliminated
                if eliminated_pieces_color(eliminated_pieces, WHITE):
                    # reset board
                    reset_board(new_piece1, new_piece2, eliminated_pieces, new_board)

                    return False
                # if piece2 is not eliminated
                else:
                    # put piece1 again in board
                    new_board.pieces.append(new_piece1)
                    # get all pieces eliminated from board
                    eliminated_black_and_white(new_board, eliminated_pieces)
                    # if the piece1 is eliminated again
                    if eliminated_pieces_color(eliminated_pieces, WHITE):
                        #reset the whole board
                        reset_board(new_piece1, new_piece2, eliminated_pieces, new_board)

                        return False
                        # if piece1 is not eliminated
                    else:
                        #reset the whole board
                        reset_board(new_piece1, new_piece2, eliminated_pieces, new_board)
                        goal.first_to_fit = 2
                        return True

            # if piece1 is not eliminated
            else:
                # put piece2 on board
                new_board.pieces.append(new_piece2)
                # get all pieces eliminated from board
                eliminated_black_and_white(new_board, eliminated_pieces)
                # if the piece2 is eliminated
                if eliminated_pieces_color(eliminated_pieces, WHITE):
                    #reset the whole board
                    reset_board(new_piece1, new_piece2, eliminated_pieces, new_board)

                    return False
                # if the piece2 is not eliminated
                else:
                    #reset the whole board
                    reset_board(new_piece1, new_piece2, eliminated_pieces, new_board)
                    goal.first_to_fit = 1
                    return True

        # if square1 is already occupied by a whtie piece
        if goal.square1_occupied_by_white and not goal.square2_occupied_by_white:
            # consider only square2
            return one_square_solution(goal.square2, new_board, eliminated_pieces, goal, 2)

        # if square2 is already occupied by a whtie piece
        if not goal.square1_occupied_by_white and goal.square2_occupied_by_white:
            # consider only square1
            return one_square_solution(goal.square1, new_board, eliminated_pieces, goal, 1)

    # square2 is None
    else:
        # consider only square1
        return one_square_solution(goal.square1, new_board, eliminated_pieces, goal, 1)


# when only one square is need for consideration
def one_square_solution(goal_square, new_board, eliminated_pieces, goal, first_to_fit_in):
    # create a new piece at goal.square
    new_piece = Piece(goal_square.x, goal_square.y, WHITE)
    # put piece on board
    new_board.pieces.append(new_piece)
    # get all pieces eliminated from board
    eliminated_black_and_white(new_board, eliminated_pieces)
    # if the piece is eliminated
    if eliminated_pieces_color(eliminated_pieces, WHITE):
        #reset the whole board
        reset_board(new_piece, None, eliminated_pieces, new_board)

        return False

    else:
        #reset the whole board
        reset_board(new_piece, None, eliminated_pieces, new_board)
        goal.first_to_fit = first_to_fit_in
        return True


# reset all pieces on board
def reset_board(new_piece1, new_piece2, eliminated_pieces, new_board):
    # remove both
    if new_piece1 and new_piece1 in new_board.pieces:
        new_board.pieces.remove(new_piece1)
    if new_piece2 and new_piece2 in new_board.pieces:
        new_board.pieces.remove(new_piece2)
    # put all black_pieces back in
    # at most 64 black_pieces could be removed
    # remove balck pieces in eliminated_pieces
    for i in range(0, MAX_BLACK_REMOVABLE + 1):
        if eliminated_pieces_color(eliminated_pieces, BLACK):
            new_board.pieces.append(eliminated_pieces_color(eliminated_pieces, BLACK))
            eliminated_pieces.remove(eliminated_pieces_color(eliminated_pieces, BLACK))

    # clear list
    del eliminated_pieces[:]
    # reconstruct neighbourhood
    find_neighbour(new_board)


def eliminated_black_and_white(new_board, eliminated_pieces):
    # get all black pieces eliminated from board
    eliminated_pieces.extend(get_eliminated(new_board, BLACK))
    # get all white balck pieces eliminated from board
    eliminated_pieces.extend(get_eliminated(new_board, WHITE))

# find all eliminated_pieces of given color
def get_eliminated(new_board, target_color):
    eliminated_pieces = []
    # update neighbourhood
    find_neighbour(new_board)

    for piece in new_board.pieces:
        if piece.color == target_color:
            # only check 2 directions
            for dir in range(LEFT, TOP + 1):
                if isinstance(piece.square_at(dir), Piece) and \
                    isinstance(piece.square_at(opposite_dir(dir)), Piece):
                    # if it is surrounded colors are different from self
                    if not piece.square_at(dir).color == piece.color and \
                        not piece.square_at(opposite_dir(dir)).color == piece.color:
                        # add to list
                        eliminated_pieces.append(piece)

    # remove eliminated_pieces from board
    for piece in eliminated_pieces:
        if piece in new_board.pieces:
            new_board.pieces.remove(piece)
    find_neighbour(new_board)
    return eliminated_pieces

# if a piece in list has the same color as required
# return the piece
def eliminated_pieces_color(eliminated_pieces, target_color):
    for piece in eliminated_pieces:
        if piece.color == target_color:
            return piece
    return None

# find opposite direction of given direction
def opposite_dir(dir):
    if dir == LEFT:
        return RIGHT
    if dir == RIGHT:
        return LEFT
    if dir == TOP:
        return BOTTOM
    if dir == BOTTOM:
        return TOP
