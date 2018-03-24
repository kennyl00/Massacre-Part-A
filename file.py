# This File Handles the Inputs and Outputs
# Created by JiaWei and Kenny (20/3/18)

from board import *

# Reads the board configuration from a file and recreates the actual Board
def read_file(file_name, new_board):

    # Opens up the file and read the lines of the data (Board Config)
    # Fitting each row of data to an Array (content[i])
    with open(file_name, 'r') as f:
        content = f.readlines()

    # Gets rid of all the '\n' char from the data
    content = [x.strip() for x in content]

    # For every row in the data (Board Config)
    for x in range(len(content)):

        # Split up the individual characters e.g. '-, X, O, @' of each row
        content[x] = ''.join(content[x].split())

        # check if the line contains Massacre or Moves
        if content[x] == MASSACRE or content[x] == MOVES:
            OUTPUT_STATE = content[x]
            break

        # For every character within a row
        for y in range(len(content[x])):

            # Place the appropriate Pieces on the Board accordingly
            # The CORNER is considered a Piece
            if content[x][y] == 'X':
                new_board.add_to_pieces(Piece(x, y, CORNER))

            elif content[x][y] == 'O':
                new_board.add_to_pieces(Piece(x, y, WHITE))

            elif content[x][y] == '@':
                new_board.add_to_pieces(Piece(x, y, BLACK))

    return OUTPUT_STATE
