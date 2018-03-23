# This File defines Global Variables and Classes used for the
# Project Part A
# Created by JiaWei and Kenny (20/3/18)

BOARD_COL_NUM = 8
BOARD_ROW_NUM = 8
LEFT = 0
TOP = 1
RIGHT = 2
BOTTOM = 3
WHITE = 'W'
BLACK = 'B'
CORNER = 'X'

# a class contains two pieces
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
        for i in range(0, BOARD_COL_NUM):
            for j in range(0, BOARD_ROW_NUM):
                self.squares.append(Square(i, j))

    # Adds a Piece to the Board's List
    def add_to_pieces(self, piece):
        self.pieces.append(piece)


class Move:
    v_location = None
    h_location = None

    utility = 0

    def __init__(self, v, h):
        self.v_location = v
        self.h_location = h

class Square:
    # Coordinates of each Square
    v_location = None
    h_location = None

    # the priority of each square to be placed on by a piece
    priority = 0

    # Initialises the Square with it's own coordinates
    def __init__(self, v, h):
        self.v_location = v
        self.h_location = h


class Piece:
    # Coordinates of each Piece
    v_location = None
    h_location = None

    # The Objects surroundings of this Piece
    left = None
    right = None
    top = None
    bottom = None

    # Piece could either be Black or White
    color = None

    # Can the Piece be removed
    removable = False

    # Initialises the Piece by its own coordinates and color
    def __init__(self, v, h, color):
        self.v_location = v
        self.h_location = h
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
