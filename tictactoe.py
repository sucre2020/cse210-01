'''
Tic-Tac-Toe: Tic-Tac-Toe
Author: Efita Effiom
'''
import sys

def main():

    while True:

        print('''
        ### WELCOME! FOLLOW THE PROMPT TO PLAY THE GAME ###
        ...................................................
        
        To play or exit the tic-tac-toe game, please press\n

        1. Play Game
        2. Exit
        ''')
        
        selection = input('Please type a number:')
        
        if selection == '1':
            new_game()
        elif selection == '2':
            sys.exit()
        else:
            print('You did not make a valid selection')



#Function to start a new game        
def new_game():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print(f" player {player} You've done well. Thanks for playing!") 



#function to create board
def create_board():
    board = []
    for i in range(9):
        board.append(i + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def is_draw(board):
    for i in range(9):
        if board[i] != "x" and board[i] != "o":
            return False
    return True 
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    i = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[i - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()