from board import *
from goal import *
from random import shuffle

def Massacre(new_board, target_color):

    # While the goal list is not empty
    while not isEliminated(new_board, target_color):
        goal_list = get_goal_list(board, target_color)
        goal = goal_list.pop(0)

        while not is_goal_achievable(goal):
            goal_list.append(goal)
            goal = goal_list.pop(0)


        if goal.square1 and goal.square2:
            goal_square1 = goal.square1
            goal_square2 = goal.square2

            if start_piece1 and start_square1:

                 # Moving one White Piece to a Goal position 1
                goal_square1.set_priority(new_board)
                start_piece1 = get_nearest_piece(new_board, WHITE)
                start_square1 = get_standing_square(start_piece1, new_board)
                path = astar(start_piece1, start_square1, goal_square1, new_board)

                # Refresh
                clear_priority(new_board)
                clear_cost_to_move(new_board)
                clear_parent(new_board)
                find_neighbour(new_board)
                start_piece1.moveable = False

                # Moving another White Piece to a Goal Position 2
                goal_square2.set_priority(new_board)
                start_piece2 = get_nearest_piece(new_board, WHITE)
                start_square2 = get_standing_square(start_piece2, new_board)
                # Moving a second White Piece to another Goal position 2
                path = astar(start_piece2, start_square2, goal_square2, new_board)

                #refresh
                clear_priority(new_board)
                clear_cost_to_move(new_board)
                clear_parent(new_board)
                find_neighbour(new_board)
                start_piece2.moveable = False

        else:
            goal_square1 = goal.square1



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
            if piece.priorty < min_priority:
                min_priority_piece = piece
                min_priority = piece.priority

    return min_priority_piece
