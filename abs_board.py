"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Headers for functions in abstract board for simple tic-tac-toe-like games, 2021.
Intended for Grau en Intel-ligencia Artificial, Programacio i Algorismes 1.
I would prefer to do everything in terms of object-oriented programming though.
"""

# Import: 
# color GRAY; PLAYER_COLOR, NO_PLAYER
# board dimension BSIZ
from constants import PLAYER_COLOR, BSIZ, NO_PLAYER, GRAY

# Data structure for stones
from collections import namedtuple

Stone = namedtuple('Stone', ('x', 'y', 'color'))

def set_board_up(stones_per_player = 4):
    'Init stones and board, prepare functions to provide, act as their closure'

    # init board and game data here

    def stones(taula):
        "return iterable with the stones already played"
        played_stones1 = []
        played_stones2 = []
        for fila in range(len(taula)):
            for columna in range(len(taula[fila])):
                if taula[fila][columna] == "X":  
                    played_stones1.append((fila, columna, taula[fila][columna]))
                    nonlocal stone1 = Stone(fila, columna, PLAYER_COLOR)
                elif taula[fila][columna] == "O":
                    played_stones2.append((fila, columna, taula[fila][columna]))
                    nonlocal stone2 = Stone(fila, columna, PLAYER_COLOR)
        return played_stones1, played_stones2

    def select_st(i, j):
        '''
        Select stone that current player intends to move. 
        Player must select a stone of his own.
        To be called only after all stones played.
        Report success by returning a boolean;
        '''
        

    def end():
        'Test whether there are 3 aligned stones'
        

    def move_st(i, j):
        '''If valid square, move there selected stone and unselect it,
        then check for end of game, then select new stone for next
        player unless all stones already played;
        if square not valid, do nothing and keep selected stone.
        Return 3 values: bool indicating whether a stone is
        already selected, current player, and boolean indicating
        the end of the game.
        '''
        pass

    def draw_txt(end = False):
        'Use ASCII characters to draw the board.'
        for fila in range(BSIZ):
            print("|", end = "")
            for columna in range(BSIZ):
                if taula[fila][columna] == 0:
                    print(" - ", end = "")
                elif taula[fila][columna] == 1 and stone1:
                    print(" X ", end = "")
                else:
                    print(" O ", end = "")
            print("|")

    # return these 4 functions to make them available to the main program
    return stones, select_st, move_st, draw_txt