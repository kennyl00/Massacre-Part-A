# This File Handles the Inputs and Outputs
# Created by JiaWei and Kenny (20/3/18)

from board import *

# Reads the board configuration from a file and recreates the actual Board
def read_file(file_name, new_board):

    # Opens up the file and read the lines of the data (Board Config)
    # Fitting each row of data to an Array (content[i])
    with open(file_name) as f:
        content = f.readlines()

    # Gets rid of all the '\n' char from the data
    content = [x.strip() for x in content]

    # For every row in the data (Board Config)
    for i in range(len(content)):

        # Split up the individual characters e.g. '-, X, O, @' of each row
        content[i] = ''.join(content[i].split())

        # For every character within a row
        for j in range(len(content[i])):

            # Place the appropriate Pieces on the Board accordingly
            if content[i][j] == 'X':
                new_board.add_to_pieces(Piece(j, i, CORNER))

            elif content[i][j] == 'O':
                new_board.add_to_pieces(Piece(j, i, WHITE))

            elif content[i][j] == '@':
                new_board.add_to_pieces(Piece(j, i, BLACK))

        print(content[i])
