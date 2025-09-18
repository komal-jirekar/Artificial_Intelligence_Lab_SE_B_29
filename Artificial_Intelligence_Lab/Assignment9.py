import math

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Check for winner
def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

# Check if moves are left
def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# Minimax implementation
def minimax(board, depth, is_max):
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ' '
        return best

# Find best move for AI (O)
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Main game loop
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human = 'X'
    ai = 'O'

    print("Tic Tac Toe! You are X, AI is O.")
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:  # Human turn
            x, y = map(int, input("Enter row and col (0-2 0-2): ").split())
            if board[x][y] == ' ':
                board[x][y] = human
            else:
                print("Invalid move, try again.")
                continue
        else:  # AI turn
            print("AI's Move:")
            x, y = find_best_move(board)
            board[x][y] = ai

        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Winner is {winner}!")
            return

    print("It's a draw!")

# Run the game
if __name__ == "__main__":
    play_game()

