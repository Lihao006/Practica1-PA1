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
    taula = [[NO_PLAYER for y in range(BSIZ)] for x in range(BSIZ)]
    turn = 1 # Turn = 1 per al jugador 1 i 2 per al jugador 2.

    played_stones1 = []
    played_stones2 = []
    
    selected_stone = None

    def stones():
        "return iterable with the stones already played"
        nonlocal played_stones1, played_stones2
        for fila in range(BSIZ):
            for columna in range(BSIZ): # Això podria ser "for columna in range(BSIZ):" perquè al inicialitzar la taula les columnes són : "NO_PLAYER for y in range(BSIZ)"
                if taula[fila][columna] == 1:  
                    played_stones1.append(Stone(fila, columna, PLAYER_COLOR[0]))
                elif taula[fila][columna] == 2:
                    played_stones2.append(Stone(fila, columna, PLAYER_COLOR[1]))
        return played_stones1, played_stones2

    def select_st(i, j):
        '''
        Select stone that current player intends to move. 
        Player must select a stone of his own.
        To be called only after all stones played.
        Report success by returning a boolean;
        '''

        nonlocal selected_stone

        if len(played_stones1) == len(played_stones2) == stones_per_player:
            if 0 <= i < BSIZ and 0 <= j < BSIZ and taula[i][j] == turn:
                selected_stone = (Stone(i, j, PLAYER_COLOR[turn - 1]))
                return True
            return False   
        else:
            return False  

    def end(): 
        '''
        Aqui tinc una vaga idea: cada vegada que es mou una pedra,
        es comprova si hi ha 3 pedres alineades només en aquella columna 
        (comprovant que hi ha pedres del mateix color en (i, j),(i+1, j), ... , (i+(BSIZ-1), j)) 
        i fila (fins a i, j+(BSIZ-1)) que s'ha posat la pedra. 
        Per tant, no caldria analitzar totes les files i columnes perquè segur que no hi haurà 3 en ratlla en altres llocs.
        Després, si no hi ha 3 en raya, mirem si aquella pedra pertany a alguna casella de la diagonal principal, 
        que tots tenen forma de (0, 0), (1, 1), ... , (BSIZ - 1, BSIZ - 1). Mirem si hi ha 3 en ratlla a la diagonal principal.
        Si pertant a la diagonal primaria, segur que no pot pertànyer a la diagonal inversa a no ser que la pedra estigui
        en la casella central de la taula, que seria el (BSIZ // 2, BSIZ // 2). Per tant, examinarem les dues
        diagonals si la pedra està en la casella central. Sinó, doncs només la diagonal on estigui.
        Modifica alguna cosa si se t'acudeix algo millor.
        '''
        
        'Test whether there are 3 aligned stones'

        # Com és un algoritme de cerca utilitzo el while

        fila = 0
        columna = 0

        # Comprovar files
        while fila < BSIZ:
            if -1 != taula[fila][0] == taula[fila][1] == taula[fila][2]:
                return True 
            fila += 1
        
        # Comprovar columnes
        while columna < BSIZ:
            if -1 != taula[0][columna] == taula[1][columna] == taula[2][columna]:
                return True
            columna += 1

        # Comprovar les diagonals
        if (-1 != taula[0][0] == taula[1][1] == taula[2][2]) or (-1 != taula[0][2] == taula[1][1] == taula[2][0]):
            return True

        return False

    def move_st(i, j):
        '''If valid square, move there selected stone and unselect it,
        then check for end of game, then select new stone for next
        player unless all stones already played;
        if square not valid, do nothing and keep selected stone.
        Return 3 values: bool indicating whether a stone is
        already selected, current player, and boolean indicating
        the end of the game.
        '''
        '''
        nonlocal turn, selected_stone, played_stones1, played_stones2

        if len(played_stones2) != stones_per_player:
            if turn == 1:
                selected_stone = played_stones1
        '''    
    
        nonlocal turn, taula, selected_stone, played_stones1, played_stones2
        
        # Aquest codi només funciona per les 4 primeres
        if (0 <= i < BSIZ) and (0 <= j < BSIZ) and (taula[i][j] == -1): # Comprovar que la casella és valida i està buida
            if turn == 1:
                taula[i][j] = 1
                played_stones1.append(Stone(i, j, PLAYER_COLOR[0]))
                turn = 2
                return bool(len(played_stones1) < stones_per_player), turn, end()
            elif turn == 2:
                taula[i][j] = 2
                played_stones2.append(Stone(i, j, PLAYER_COLOR[1]))
                turn = 1
                return bool(len(played_stones2) < stones_per_player), turn, end()
        else:
            print ("La casella no és vàlida o està ocupada.")
            print ("Introdueix una casella vàlida.")
            return bool(len(played_stones2) < stones_per_player), turn, end()
        
        # He provat això però no funciona

        '''
        k = 0
        if len(played_stones2) < stones_per_player:
            if 0 <= i < BSIZ and 0 <= j < BSIZ and taula[i][j] == -1: # Comprovar que la casella és valida i està buida
                k += 1
                if turn == 1:
                    taula[i][j] = 1
                    turn = 2
                    return bool(k < 8), turn, end()
                elif turn == 2:
                    taula[i][j] = 2
                    turn = 1
                    return bool(k < 8), turn, end()
        else:
            if 0 <= i < BSIZ and 0 <= j < BSIZ and taula[i][j] == -1:
                if selected_stone != None:
                    si = selected_stone[0]
                    sj = selected_stone[1]
                    taula[si][sj] = NO_PLAYER
                    selected_stone = None
                    if turn == 1:
                        taula[i][j] = 1
                        turn = 2
                        return False, turn, end()
                    elif turn == 2:
                        taula[i][j] = 2
                        turn = 1
                        return False, turn, end()
        '''          

    def draw_txt(end = False):
        'Use ASCII characters to draw the board as a matrix.'
        if end:
            print("Ha guanyat el jugador ", turn)
            
        for fila in range(len(taula)):
                print("|", end="")
                for columna in range(len(taula[fila])):
                    if taula[fila][columna] == NO_PLAYER:
                        print(" - ", end="")
                    elif taula[fila][columna] == 1:
                        print(" X ", end="")
                    elif taula[fila][columna] == 2:
                        print(" O ", end="")
                print("|")
        if turn == 1:
            print("Ara li toca al jugador 1, que és el X")
        else:
            print("Ara li toca al jugador 2, que és el O")

    # return these 4 functions to make them available to the main program
    return stones, select_st, move_st, draw_txt