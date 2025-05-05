def is_safe(board, row, col, n):
    # Check the column for the same queen
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queen(board, row, n):
    # If all queens are placed, return True
    if row >= n:
        return True

    # Consider this row and try placing queens in all columns one by one
    for col in range(n):
        # Check if it's safe to place the queen
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen

            # Recur to place the next queen
            if solve_n_queen(board, row + 1, n):
                return True

            # If placing queen in current position doesn't lead to a solution, backtrack
            board[row][col] = 0

    # If the queen can't be placed in any column, return False
    return False

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print('Q' if board[i][j] else '.', end=' ')
        print()

def n_queen(n):
    # Initialize the chessboard
    board = [[0] * n for _ in range(n)]

    # Try to solve the N-Queen problem
    if solve_n_queen(board, 0, n):
        print_solution(board, n)
    else:
        print("Solution does not exist")

# Example usage
n = 4  # You can change this value to any N
n_queen(n)