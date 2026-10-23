
import random

N = 4

# Calculate attacking pairs
def calculate_cost(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:
                conflicts += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Print the 4x4 grid
def display_board(board):
    for row in range(1, N + 1):
        for col in range(N):
            if board[col] == row:
                print("| Q ", end="")
            else:
                print("| . ", end="")
        print("|")
    print()


# Generate neighboring states
def get_neighbors(board):
    neighbors = []

    for col in range(N):
        for row in range(1, N + 1):
            if row != board[col]:
                new_board = board.copy()
                new_board[col] = row
                neighbors.append((col, row, new_board))

    return neighbors


def hill_climbing(initial_board):
    board = initial_board.copy()
    step = 1

    while True:
        current_cost = calculate_cost(board)

        print("\n========== STEP", step, "==========")
        print("Current State:", board)
        print("Current Cost:", current_cost)
        print("Current Grid:")
        display_board(board)

        if current_cost == 0:
            print("GOAL CONFIGURATION REACHED!")
            return board

        neighbors = get_neighbors(board)
        best_cost = float("inf")
        best_neighbors = []

        print("========== ALL NEIGHBORS ==========")

        for col, row, neighbor in neighbors:
            cost = calculate_cost(neighbor)

            print("Move column", col + 1, "to row", row)
            print("Neighbor State:", neighbor)
            print("Neighbor Cost:", cost)
            print("Neighbor Grid:")
            display_board(neighbor)

            if cost < best_cost:
                best_cost = cost
                best_neighbors = [neighbor]
            elif cost == best_cost:
                best_neighbors.append(neighbor)

        if best_cost < current_cost:
            board = random.choice(best_neighbors)

            print("========== SELECTED STATE ==========")
            print("Selected State:", board)
            print("Selected Cost:", calculate_cost(board))
            print("Selected Grid:")
            display_board(board)

        else:
            print("Local minimum reached.")
            print("Restarting with a new configuration.")

            board = [random.randint(1, N)
                     for _ in range(N)]

            print("Restart State:", board)
            print("Restart Cost:", calculate_cost(board))
            print("Restart Grid:")
            display_board(board)

        step += 1


# Initial configuration
initial_board = [1, 3, 2, 4]

random.seed(7)
solution = hill_climbing(initial_board)

print("\n========== FINAL RESULT ==========")
print("Final Solution:", solution)
print("Final Cost:", calculate_cost(solution))
print("Final Grid:")
display_board(solution)



