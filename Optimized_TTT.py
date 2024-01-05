def print_board(board):
    for row in board:
        print('  '.join(['⬛' if cell == 0 else '🟥' if cell == 1 else '🟩' for cell in row]))
        print()

def check_win(board):
    for i in range(3):
        if all(board[i][j] == 1 for j in range(3)) or all(board[j][i] == 1 for j in range(3)):
            return 1
        if all(board[i][j] == 2 for j in range(3)) or all(board[j][i] == 2 for j in range(3)):
            return 2
    if all(board[i][i] == 1 for i in range(3)) or all(board[i][2 - i] == 1 for i in range(3)):
        return 1
    if all(board[i][i] == 2 for i in range(3)) or all(board[i][2 - i] == 2 for i in range(3)):
        return 2
    return 0

def take_turn(board, player):
    while True:
        try:
            number = int(input(f"{['Red', 'Green'][player - 1]}, enter a number (1-9): "))
            picked_col = (number - 1) % 3
            picked_row = (number - 1) // 3
            if board[picked_row][picked_col] == 0:
                board[picked_row][picked_col] = player
                break
            else:
                print("Cell already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    board = [[0] * 3 for _ in range(3)]
    players = [1, 2]
    
    for _ in range(9):
        print_board(board)
        take_turn(board, players[_ % 2])
        winner = check_win(board)
        if winner:
            print(f"{['Red', 'Green'][winner - 1]} Won!")
            break
    else:
        print_board(board)

if __name__ == "__main__":
    main()
