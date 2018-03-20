from neighbour import *
from board import *
from file import *


# This is the main file
# Created by JiaWei and Kenny (20/3/18)

def main():
    print("HELLO")
    board = Board()

    read_file('sample3.txt', board)

    find_neighbour(board)
