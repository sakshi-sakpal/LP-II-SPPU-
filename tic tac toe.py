def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print()

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # row
            return True
        if all([board[j][i] == player for j in range(3)]):  # column
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):  # top-left to bottom-right
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # top-right to bottom-left
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def play_game():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")

        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        move = int(move)
        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] in ["X", "O"]:
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
