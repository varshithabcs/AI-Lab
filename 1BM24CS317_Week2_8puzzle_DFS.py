# 8-Puzzle using DFS

def display(state):
    for i in range(0, 9, 3):
        print(*state[i:i + 3])
    print()


def get_moves(state):
    moves = []
    zero = state.index(0)
    directions = [-3, 3, -1, 1]

    for d in directions:
        new_pos = zero + d

        if 0 <= new_pos < 9:
            if d == -1 and zero % 3 == 0:
                continue
            if d == 1 and zero % 3 == 2:
                continue

            new_state = list(state)
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )
            moves.append(tuple(new_state))

    return moves


def dfs(initial, goal):
    stack = [(initial, [initial])]
    visited = {initial}
    iterations = 0

    while stack and iterations < 10:
        current, path = stack.pop()
        iterations += 1

        print("Iteration:", iterations)
        display(current)

        if current == goal:
            print("Goal found!")
            print("Number of moves:", len(path) - 1)
            return

        # Prefer states closer to the goal
        moves = get_moves(current)
        moves.sort(key=lambda s: sum(
            s[i] != goal[i] for i in range(9)
        ), reverse=True)

        for next_state in moves:
            if next_state not in visited:
                visited.add(next_state)
                stack.append((next_state, path + [next_state]))

    print("Goal not found within 10 iterations.")


print("Enter 9 numbers (0 represents blank):")
initial = tuple(map(int, input().split()))

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

if len(initial) == 9 and set(initial) == set(range(9)):
    dfs(initial, goal)
else:
    print("Invalid input! Enter numbers 0 to 8 exactly once.")