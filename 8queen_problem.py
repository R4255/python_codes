def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row):
    n = len(board)

    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_n_queens_util(board, row + 1):
                return True

            # If placing the queen in board[row][col] doesn't lead to a solution
            board[row][col] = 0

    return False

def solve_n_queens(n):
    # Initialize the chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0):
        print("No solution exists")
        return None

    return board

def print_board(board):
    for row in board:
        print(' '.join(['Q' if cell == 1 else '.' for cell in row]))

if __name__ == "__main__":
    n = 8  # Number of queens

    # Solve the 8-queen problem
    solution = solve_n_queens(n)

    if solution:
        print("Solution for the 8-queen problem:")
        print_board(solution)
