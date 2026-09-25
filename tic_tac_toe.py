# Tic-Tac-Toe Game
# Human = X
# Computer = O

board = [" " for _ in range(9)]


# Display the board
def display_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


# Check whether a player has won
def check_winner(player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if (board[position[0]] == player and
            board[position[1]] == player and
            board[position[2]] == player):
            return True

    return False


# Check whether the board is full
def board_full():
    return " " not in board


# Computer chooses an empty position
def computer_move():
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return


# Main game
print("TIC-TAC-TOE")
print("You are X")
print("Computer is O")

print("\nPositions:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:

    # Human move
    try:
        choice = int(input("\nEnter your position (1-9): "))
    except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

    if choice < 1 or choice > 9:
        print("Invalid position. Choose between 1 and 9.")
        continue

    if board[choice - 1] != " ":
        print("Position already occupied. Choose another position.")
        continue

    board[choice - 1] = "X"

    display_board()

    # Check human winner
    if check_winner("X"):
        print("Congratulations! You won!")
        break

    # Check draw
    if board_full():
        print("Game is a draw!")
        break

    # Computer move
    computer_move()
    print("Computer's move:")
    display_board()

    # Check computer winner
    if check_winner("O"):
        print("Computer wins!")
        break

    # Check draw
    if board_full():
        print("Game is a draw!")
        break