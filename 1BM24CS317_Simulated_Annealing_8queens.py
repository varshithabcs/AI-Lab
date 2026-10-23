
import random
import math

N = 8

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


# Display chessboard
def display_board(board):
    for row in range(1, N + 1):
        for col in range(N):
            if board[col] == row:
                print("| Q ", end="")
            else:
                print("| . ", end="")
        print("|")
    print()


def simulated_annealing():
    # Initial state
    board = [1, 5, 8, 6, 3, 7, 2, 2]
    current_cost = calculate_cost(board)

    # Store the best state found
    best_board = board.copy()
    best_cost = current_cost

    temperature = 100.0
    cooling_rate = 0.995
    min_temperature = 0.01
    max_iterations = 10000

    print("Initial State:", board)
    print("Initial Cost:", current_cost)
    display_board(board)

    for step in range(1, max_iterations + 1):

        # Generate a random neighboring state
        neighbor = board.copy()
        col = random.randint(0, N - 1)
        new_row = random.randint(1, N)

        while new_row == neighbor[col]:
            new_row = random.randint(1, N)

        neighbor[col] = new_row
        neighbor_cost = calculate_cost(neighbor)

        delta = neighbor_cost - current_cost

        # Decide whether to accept the new state
        if delta <= 0:
            accepted = True
        else:
            probability = math.exp(-delta / temperature)
            accepted = random.random() < probability

        print("\nIteration:", step)
        print("Temperature:", round(temperature, 3))
        print("Neighbor State:", neighbor)
        print("Neighbor Cost:", neighbor_cost)
        print("Change in Cost:", delta)

        if accepted:
            board = neighbor
            current_cost = neighbor_cost
            print("Move Accepted")
        else:
            print("Move Rejected")

        # Update best state
        if current_cost < best_cost:
            best_board = board.copy()
            best_cost = current_cost

        print("Current State:", board)
        print("Current Cost:", current_cost)
        print("Current Grid:")
        display_board(board)

        # Goal check after at least 5 iterations
        if step >= 5 and current_cost == 0:
            print("Goal configuration reached!")
            break

        # Reduce temperature
        temperature *= cooling_rate

        if temperature < min_temperature:
            temperature = 100.0

    print("\nBest State:", best_board)
    print("Best Cost:", best_cost)
    print("Total Iterations:", step)

    if best_cost == 0:
        print("Solution Found!")
        print("Final Chessboard:")
        display_board(best_board)
    else:
        print("Solution not found. Run the program again.")


simulated_annealing()
