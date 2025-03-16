"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lukáš Svoboda
email: lukas.svobo1@seznam.cz
"""

import sys

def print_welcome():
    print("Welcome to Tic Tac Toe")
    print("=" * 40)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("=" * 40)
    print("Let's start the game\n")

def print_board(board):
    print("+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def get_move():
    while True:
        try:
            move = int(input("Please enter your move number (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Enter a number between 1 and 9.")
                continue
            return move
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    moves = {i: (i // 3, i % 3) for i in range(9)}
    players = ['O', 'X']
    turn = 0

    print_board(board)
    
    for _ in range(9):
        player = players[turn % 2]
        print(f"Player {player} | ", end="")
        move = get_move() - 1

        row, col = moves[move]
        if board[row][col] != ' ':
            print("This position is already occupied. Try again.")
            continue

        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print(f"Congratulations, the player {player} WON!")
            return
        
        turn += 1
    
    print("It's a tie!")

if __name__ == "__main__":
    print_welcome()
    play_game()