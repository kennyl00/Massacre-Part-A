def astar(start_square, goal_square, new_board):
    openset = set()
    closedset = set()
    path = [] # to print the path to current state
    openset.add(start_square)

    while not openset._len_() = 0:

        # pop a square from openset
        current_square = openset.pop()
        # add square to openset
        openset.add(get_available_neighbours(current_square, new_board, openset, closedset, goal_square, path))
        # if solution is found, break
        if not path._len_() == 0
            break

        closedset.add(current_square)

        for square in path:
            print(square.x, square.y)
    return


def get_available_neighbours(current_square, new_board, openset, closedset, goal_square, path):
    # a list of neghbours to be added to openset
    neighbours_to_add = []
    for dir in range(LEFT, BOTTOM + 1):
        # find the neighbour of current square
        neighbour = find_square_neighbour(square, dir, new_board)
        # find the second square in the requried direction
        jumped_neighbour = find_square_neighbour(neighbour, dir, new_board)
        # if neighbour is the goal, add to path
        if neighbour.x = goal_square.x and neighbour.y = goal_square.y:
            while neighbour.parent:
                path.append(neighbour)
                neighbour = neighbour.parent
            path.append(neighbour)
        # if junped_neighbour is the goal, add to path
        if jumped_neighbour.x = goal_square.x and jumped_neighbour.y = goal_square.y:
            while jumped_neighbour.parent:
                path.append(jumped_neighbour)
                jumped_neighbour = jumped_neighbour.parent
            path.append(jumped_neighbour)

        # if current_square can move to a neighbour
        if neighbour and check_move(neighbour) is YES:
            # update the cost_to_move
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

        # if current_square can jump to a neighbour
        if check_valid_move(neighbour) is JUMP:
            # update the cost_to_move
            jumped_neighbour.cost_to_move = current_square.cost_to_move + 1
            # if jumped_neighbour in the openset and neighbour has a bigger f
            if bigger_than_in_set(jumped_neighbour, openset):
                continue
            # if jumped_neighbour in the closedset and neighbour has a bigger f
            if bigger_than_in_set(jumped_neighbour, closedset):
                continue
            else:
                # set parent and add to openset
                jumped_neighbour.parent = current_square
                neighbours_to_add.append(jumped_neighbour)

        return neighbours_to_add


def bigger_than_in_set(neighbour, set):
    for square in set:
        # if they have same location and neighbour has a higher f, return True
        if neighbour.x = square.x and neighbour.y = square.y:
            if neighbour.cost_to_move + neighbour.priority >= square.cost_to_move + square.priority
                return True

    return False


def clear_priority(new_board):
    for piece in new_board.pieces:
        piece.priority = 0

    for square in new_board.pieces:
        square.priority = 0
