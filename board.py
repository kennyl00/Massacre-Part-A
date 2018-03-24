# This File defines Global Variables and Classes used for the
# Project Part A
# Created by JiaWei and Kenny (20/3/18)
BOARD_COL_NUM = 8
BOARD_ROW_NUM = 8
LEFT = 0
TOP = 1
RIGHT = 2
BOTTOM = 3
TOP_LEFT = 4
TOP_RIGHT = 5
BOTTOM_LEFT = 6
BOTTOM_RIGHT = 7
CORNER = 'X'
BLACK = 'B'
WHITE = 'W'
YES = 'Y'
NO = 'N'
JUMP = 'J'


class Goals:
    piece1 = None
    piece2 = None

    def __init__(self):
        assert 1 == 1

    def set_piece1(self, piece1):
        self.piece1 = piece1

    def set_piece2(self, piece2):
        self.piece2 = piece2



class Board:
    # List of Squares and Pieces
    squares = []
    pieces = []

    # Initialises the Board with Squares, with the Dimensions provided (8,8)
    def __init__(self):
        for x in range(0, BOARD_ROW_NUM):
            for y in range(0, BOARD_COL_NUM):
                self.squares.append(Square(x, y))

    # Adds a Piece to the Board's List
    def add_to_pieces(self, piece):
        self.pieces.append(piece)


class Square:
    # Coordinates of each Square
    x = None
    y = None

    # the priority of each square to be placed on by a piece
    priority = 0

    # Initialises the Square with it's own coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Piece:
    # Coordinates of each Piece
    x = None
    y = None

    # The Objects surroundings of this Piece
    left = None
    right = None
    top = None
    bottom = None
    color = None
    top_left = None
    top_right = None
    bottom_left = None
    bottom_right = None
    removable = False
    priority = 0
    cost_to_move = 0

    # Piece could either be Black or White
    color = None

    # Can the Piece be removed
    removable = False

    # Initialises the Piece by its own coordinates and color
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    # Returns the Object at that particular Direction
    def square_at(self, dir):
        if dir == LEFT:
            return self.left
        if dir == RIGHT:
            return self.right
        if dir == TOP:
            return self.top
        if dir == BOTTOM:
            return self.bottom


    # If there's an Object at the specified Direction,
    # return the Object opposite of said Direction
    def opposite_of(self, dir):
        if dir == LEFT and self.left:
            return self.right
        if dir == RIGHT and self.right:
            return self.left
        if dir == TOP and self.top:
            return self.bottom
        if dir == BOTTOM and self.bottom:
            return self.top

    # This function sets the Piece's Direction (TOP, BOTTOM, LEFT, RIGHT) to
    # to a given object (Piece, Square)
    def set_neighbour(self, dir, neighbour):
        if dir == LEFT:
            self.left = neighbour
        if dir == RIGHT:
            self.right = neighbour
        if dir == TOP:
            self.top = neighbour
        if dir == BOTTOM:
            self.bottom = neighbour

        if dir == TOP_LEFT:
            self.top_left = neighbour

        if dir == TOP_RIGHT:
            self.top_right = neighbour

        if dir == BOTTOM_LEFT:
            self.bottom_left = neighbour

        if dir == BOTTOM_RIGHT:
            self.bottom_right = neighbour

    # This function assigns each Square and Piece to a priority relative to the individual Piece
    def manhattan(self, new_board):
        for square in new_board:
            square.priority = abs(self.x - square.x) + abs(self.y - square.y)

        for piece in new_board:
            piece.priority = abs(self.x - piece.x) + abs(self.y - piece.y)
