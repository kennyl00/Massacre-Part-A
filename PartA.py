import re

BOARD_COL_NUM = 8
BOARD_ROW_NUM = 8
LEFT = 0
RIGHT = 1
TOP = 2
BOTTOM = 3
W = 'W'
B = 'B'
X = 'X'


class Square:
    v_location = None
    h_location = None
    priority = 0

    def __init__(self, v, h):
        self.v_location = v
        self.h_location = h


class Piece:
    v_location = None
    h_location = None
    left = None
    right = None
    top = None
    bottom = None
    color = None
    removable = False

    def __init__(self, v, h, color):
        self.v_location = v
        self.h_location = h
        self.color = color

    def square_at(self, dir):
        if dir == LEFT:
            return self.left
        if dir == RIGHT:
            return self.right
        if dir == TOP:
            return self.top
        if dir == BOTTOM:
            return self.bottom

    def opposite_of(self, dir):
        if dir == LEFT and self.left:
            return self.right
        if dir == RIGHT and self.right:
            return self.left
        if dir == TOP and self.top:
            return self.bottom
        if dir == BOTTOM and self.bottom:
            return self.top

    def set_neighbour(self, dir, neighbour):
        if dir == LEFT:
            self.left = neighbour
        if dir == RIGHT:
            self.right = neighbour
        if dir == TOP:
            self.top = neighbour
        if dir == BOTTOM:
            self.bottom = neighbour


class Board:
    squares = []
    pieces = []

    def __init__(self):

        for i in range(0, BOARD_COL_NUM):
            for j in range(0, BOARD_ROW_NUM):
                self.squares.append(Square(i, j))

    def add_to_pieces(self, piece):
        self.pieces.append(piece)


def read_file(file_name, new_board):
    with open(file_name) as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    for i in range(len(content)):
        content[i] = ''.join(content[i].split())

        for j in range(len(content[i])):

            if content[i][j] == 'X':
                new_board.add_to_pieces(Piece(j, i, X))

            if content[i][j] == 'O':
                new_board.add_to_pieces(Piece(j, i, W))

            if content[i][j] == '@':
                new_board.add_to_pieces(Piece(j, i, B))

        print(content[i])


def delta_v(dir):
    if dir == TOP:
        return 1
    if dir == BOTTOM:
        return -1
    return 0


def delta_h(dir):
    if dir == RIGHT:
        return 1
    if dir == LEFT:
        return -1
    return 0


def set_piece_neighbour(new_board):
    for piece in board.pieces:

        for dir in range(LEFT, BOTTOM + 1):
            if occupied(piece, dir, new_board.pieces):
                set_neighbour(piece, dir, new_board.pieces)

            if occupied(piece, dir, new_board.squares):
                set_neighbour(piece, dir, new_board.squares)


def set_neighbour(piece, dir, list):
    if dir == LEFT and piece.left is None:
        piece.left = occupied(piece, dir, list)
    if dir == RIGHT and piece.right is None:
        piece.right = occupied(piece, dir, list)
    if dir == TOP and piece.top is None:
        piece.top = occupied(piece, dir, list)
    if dir == BOTTOM and piece.bottom is None:
        piece.bottom = occupied(piece, dir, list)


def occupied(p, dir, list):
    for p2 in list:
        if (p.v_location + delta_v(dir)) == p2.v_location and (p.h_location + delta_h(dir)) == p2.h_location:
            return p2

    return None


def count_legal_move(new_board, color):
    count = 0
    for piece in new_board.pieces:
        if piece.color is color:
            if piece.left:
                if isinstance(piece.left, Square):
                    count += 1
                else:
                    if piece.left.left and isinstance(piece.left.left, Square):
                        count += 1
            if piece.right:
                if isinstance(piece.right, Square):
                    count += 1
                else:
                    if piece.right.right and isinstance(piece.right.right, Square):
                        count += 1
            if piece.top:
                if isinstance(piece.top, Square):
                    count += 1
                else:
                    if piece.top.top and isinstance(piece.top.top, Square):
                        count += 1
            if piece.bottom:
                if isinstance(piece.bottom, Square):
                    count += 1
                else:
                    if piece.bottom.bottom and isinstance(piece.bottom.bottom, Square):
                        count += 1

    return count


def find_solution(new_board, visited_list):

    for piece in new_board.pieces:
        piece.removable = False

    for piece in new_board.pieces:
        if piece.color is B:
            for dir in range(LEFT, BOTTOM + 1):
                if piece.square_at(dir) and piece.opposite_of(dir):
                    if isinstance(piece.square_at(dir), Piece):
                        if piece.square_at(dir).color is X:
                            if isinstance(piece.opposite_of(dir), Square) and piece.opposite_of(dir) in visited_list:
                                piece.removable = True
                                break

                    else:
                        if piece.square_at(dir) in visited_list:
                            if isinstance(piece.opposite_of(dir), Piece) and piece.opposite_of(dir).color is X:
                                piece.removable = True
                                break

                            if isinstance(piece.opposite_of(dir), Square) and piece.opposite_of(dir) in visited_list:
                                piece.removable = True
                                break

    for piece in new_board.pieces:
        if piece.color is B and piece.removable is False:

            return False

    return True


def remove_white_pieces(new_board):


    white_pieces = []
    for piece in new_board.pieces:
        if piece.color is W:
            white_pieces.append(piece)


    return list(set(new_board.pieces) - set(white_pieces))


def num_white_pieces(new_board):
    num = 0
    for piece in new_board.pieces:
        if piece.color is W:
            num += 1
    return num


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


def determinate_goals(new_board):

    goal_squares = []

    num_white = num_white_pieces(new_board)
    new_board.pieces = remove_white_pieces(new_board)
    visited_list = [None] * (num_white + 1)

    limited_dfs(new_board, num_white, visited_list, goal_squares)

    if goal_squares.__len__() == 0:
        print('no solution is found')
        exit(0)

    for i in goal_squares:
        if i:
            print('location', i.v_location, i.h_location)
            print('priority = ', i.priority,)
            print()

    return goal_squares


board = Board()

read_file('sample3.txt', board)

set_piece_neighbour(board)

print(count_legal_move(board, W))
print(count_legal_move(board, B))

goal_squares = determinate_goals(board)

# created a new board cause pieces in the old has been changed
board2 = Board()
read_file('sample3.txt', board2)

# sort the object in goal_squares and pick the square with lowest priority to be occupied first
# X - - - - - - X
# - - - - - - - -
# - - - - - O - -
# - - - - @ O - W
# - - - - - - O @
# - - - - - O - Q
# - - - - - - - @
# X - - - - - - X
# already set the priority of goal_squares, Q has a priority of 2, if it is occupied before W(has priority 1),
# it will instantly be removed

# just suggestion, maybe should use A* or BFS for the search algorithm, since we must print the path
