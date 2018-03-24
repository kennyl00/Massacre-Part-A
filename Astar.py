def astar(start, goal, new_board):
    openset = set()
    closedset = set()

    current = start

    openset.append(current)

    current



def clear_priority(new_board):
    for piece in new_board.pieces:
        piece.priority = 0

    for square in new_board.pieces:
        square.priority = 0
