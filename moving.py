

def check_move(piece, dir, target_color):

    # First check if the move is possible
    if check_valid_move(piece, dir):
        # Check if move could be eliminated
        if check_elimination_move(piece, dir, target_color):
            return YES

    else:
        # Check if a jump move is possible
        if check_valid_jump_move(piece, dir):
            return JUMP

    return NO


# This function checks if the a move results in the elimination of the Piece
def check_elimination_move(piece, dir, target_color):

    if dir == RIGHT:
        if isinstance(piece.top_right, Piece) and isinstance(piece.bottom_right, Piece):
            if piece.top_right.color == target_color and piece.bottom_right == target_color:
                return False

    if dir == LEFT:
        if isinstance(piece.top_left, Piece) and isinstance(piece.bottom_left, Piece):
            if piece.top_left.color == target_color and piece.bottom_left.color == target_color:
                return False

    if dir == TOP:
        if isinstance(piece.top_left, Piece) and isinstance(piece.top_right, Piece):
            if piece.top_left.color == target_color and piece.top_right.color == target_color:
                return False

    if dir == BOTTOM:
        if isinstance(piece.bottom_left, Piece) and isinstance(piece.bottom_right, Piece):
            if piece.bottom_left.color == target_color and piece.bottom_right.color == target_color:
                return False

    return True

# This function returns if a specific direction could jumped over
def check_valid_jump_move(piece, dir):

    if dir == LEFT and isinstance(piece.left.left, Square):
        return True

    if dir == RIGHT and isinstance(piece.right.right, Square):
        return True

    if dir == TOP and isinstance(piece.top.top, Square):
        return True

    if dir == BOTTOM and isinstance(piece.bottom.bottom, Square):
        return True


    return False


# This function returns if a specific direction is a valid move
# Valid moves are determined by Squares
def check_valid_move(piece, dir):

    if dir == LEFT and isinstance(piece.left, Square):
        return True

    if dir == RIGHT and isinstance(piece.right, Square):
        return True

    if dir == TOP and isinstance(piece.top, Square):
        return True

    if dir == BOTTOM and isinstance(piece.bottom, Square):
        return True


    return False
