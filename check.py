import random

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the board is full
def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

# Function to check for a win condition
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function for the computer's move
def computer_move(board, computer, human):
    # Simple random move by the computer (replace this with your AI algorithm)
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = computer
            break

# Function for the main game loop
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human = 'X'
    computer = 'O'
    current_player = human

    while True:
        print_board(board)

        if current_player == human:
            # Human's turn
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            if board[row][col] == ' ':
                board[row][col] = human
                current_player = computer
        else:
            # Computer's turn
            computer_move(board, computer, human)
            current_player = human

        if check_winner(board, human):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif check_winner(board, computer):
            print_board(board)
            print("Computer wins! Try again.")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

# Start the game
play_game()
