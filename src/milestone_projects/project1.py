#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# #############################################################################
# Milestone Project 1 
# #############################################################################

from IPython.display import clear_output # Specifically for IPython notebook environment for 
                                         # clearing output.
import random

CONST_LENGTH = 9
CONST_TEST_VALUES = ['O', 'X', 'X', 'X', 'O', 'O', 'X', 'O', 'X']

chance = ''

def draw_board(values):
    clear_output()
    for idx in range(0, CONST_LENGTH):
        if idx % 3 == 1:
            print(' {x[0]:^9} | {x[1]:^9} | {x[2]:^9} '
                .format(x=values[(CONST_LENGTH - idx - 2):CONST_LENGTH - idx + 1]))
        else:
            print('{i:>12} {i:>11}'.format(i='|'))

        if idx % 3 == 2 and idx + 1 < CONST_LENGTH:
            print('{i:->12}{i:->12}{e:->12}'.format(i='+', e=''))


def validate(player1):
    if player1 == 'X':
        return (True, 'O')
    elif player1 == 'O':
        return (True, 'X')
    else:
        return (False, None)


def player_input():
    '''
    Take in a player input and assign their marker as 'X' 
    or 'O'. Think about using while loops to continually 
    ask until you get a correct answer.
    '''
    player1 = input("\nPlayer 1 - Please pick a marker 'X' or 'O': ").upper()
        
    val = validate(player1)
    if val[0]:
        player2 = val[1]
    else:
        return False

    out = {'p1': [player1], 'p2': [player2]}

    global chance

    first = choose_first()
    if first == 0:
        print('Player 1 goes first', end='')
        out['p1'].append(0)
        out['p2'].append(1)

        chance = player1
    else:
        print('Player 2 goes first', end='')
        out['p1'].append(1)
        out['p2'].append(0)

        chance = player2
    
    return out


def choose_first():
    '''
    Uses the random module to randomly decide which player 
    goes first. Lookup random.randint() Return a string of 
    which player went first.
    '''
    return random.randint(0, 1)

def place_marker(board, marker, position):
    '''
    Takes in the board list object, a marker ('X' or 'O'), 
    and a desired position (number 1-9) and assigns it to 
    the board.
    '''
    pass


def player_choice(board):
    '''
    Asks for a player's next position (as a number 1-9) and 
    then uses @space_check(board, position) to check if it's 
    a free position. If it is, then return the position for 
    later use.
    '''
    global chance

    current = chance
    position = int(input(f'Enter the {chance}\'s next position (1-9): ')) - 10
    if space_check(board, position):
        if chance == 'X':
            board[position] = 'X'
            chance = 'O'
        else:
            board[position] = 'O'
            chance = 'X'

        draw_board(board)
        if win_check(board, current):
            print(f'Player with {current} mark, won!')
            return True
    else:
        return -1


def space_check(board, position):
    '''
    Returns a boolean indicating whether a space on the board 
    is freely available.
    '''
    return board[position] == ''


def full_board_check(board):
    '''
    Checks if the board is full and returns a boolean value. 
    True if full, False otherwise.
    '''
    return not '' in board


def win_check(board, mark):
    '''
    Takes in a board and a mark (X or O) and then checks to 
    see if that mark has won.
    '''
    possibilities = [
        board[0:3], 
        board[3:6], 
        board[6:9],
        board[0:7:3],
        board[1:8:3],
        board[2:9:3],
        board[0:9:4],
        board[2:8:2]]
    
    return [mark] * 3 in possibilities
 

def replay():
    '''
    Asks the player if they want to play again and returns a 
    boolean True if they do want to play again.
    '''
    while True:
        confirm = input('Do you want to replay ([Y]es/[N]o)? ')
        if confirm[0].lower() == 'y':
            return True
        elif confirm[0].lower() == 'n':
            return False
        else:
            print('Input not recognized, ', end='')
            continue



def main():
    print('\nWelcome to Tic Tac Toe!\n')

    board = [''] * 9
    draw_board(board)

    while True:
        players = player_input()
        if (not players):
            continue

        print(" (Player 1 is: {} and player 2 is: {})".format(players['p1'][0], players['p2'][0]))
        while True:
            result = player_choice(board)
            if result == -1:
                print("Position not available, try again")
                continue
            else:              
                if result:
                    break

                if full_board_check(board):
                    print("Game drawn. No one wins!")
                    break

        if not replay():
            break
        else:
            board = [''] * 9


main()

# #############################################################################
# Unit test functions
# #############################################################################

def draw_board_test():
    draw_board(CONST_TEST_VALUES)

# draw_board_test()
