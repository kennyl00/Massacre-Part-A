def astar(start, goal, new_board):
    openset = set()
    closedset = set()

    current = start

    openset.append(current)

    for dir in range(LEFT, BOTTOM + 1):
        if check_move(current, dir, BLACK) is YES

        if current.square_at(dir).x == goal.x and \
            current.square_at(dir).y == goal.y

            goal.cost_to_move = current.square_at(dir).cost_to_move




    return


def clear_priority(new_board):
    for piece in new_board.pieces:
        piece.priority = 0

    for square in new_board.pieces:
        square.priority = 0
