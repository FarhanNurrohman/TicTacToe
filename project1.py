from IPython.display import clear_output
from varname.helpers import Wrapper
import random

def display_board(board):
    clear_output()
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')

def player_input():
    r1 = ''
    r2 = ''

    while r1.upper() not in ['X','0']:
        r1 = input("Pilih marker 'X' atau '0': ")
        if r1.upper() not in ['X', '0']:
            print('Masukkan yang anda berikan tidak sesuai')

    if r1.upper() == 'X':
        r2 = '0'
    else:
        r2 = 'X'
    return (r1.upper(), r2)


def place_marker(board, marker, position):
    board[position] = marker

    return board

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


def full_board_check(board):
    if ' ' not in board:
        return True
    else:
        return False

def player_choice(board):
    r = ''
    while r not in range(1,10):
        r = int(input('Pilih dimana anda akan meletakkan tanda anda(1-9) :'))
        if r in range(1,10):
            if space_check(board, r):
                return r
            else:
                r = ' '
        else:
            print('Masukkan anda salah')

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark or board[7] == board[8] == board[9] == mark:
        print(f'Pemain {mark} menang')
        return True
    elif board[1] == board[4] == board[7]  == mark or board[2] == board[5] == board[8] == mark or board[3] == board[6] == board[9] == mark:
        print(f'Pemain {mark} menang')
        return True
    elif board[1] == board[5] == board[9] == mark or board[3] == board[5] == board[7] == mark:
        print(f'Pemain {mark} menang')
        return True
    elif full_board_check(board):
        return True
    else:
        return False

def replay():
    r = ''

    while r.upper() not in ['Y', 'N']:
        r = input("Apakah anda mau bermain lagi ['Y'/'N']: ")
        if r.upper() not in ['Y', 'N']:
            print('Masukkan yang anda berikan tidak sesuai')
    if r.upper() == 'Y':
        return True
    else:
        return False

def choose_first():
    pass

board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player1 = ''
player2 = ''

player1, player2 = player_input()

print('Welcome to Tic Tac Toe!')



while True:
    gameOn = True


    while gameOn:
        display_board(board)
        # Player 1 Turn
        board = place_marker(board, player1, player_choice(board))
        if win_check(board, player1):
            break

        # Player2's turn.
        board = place_marker(board, player2, player_choice(board))
        if win_check(board, player2):
            break



    if not replay():
        break