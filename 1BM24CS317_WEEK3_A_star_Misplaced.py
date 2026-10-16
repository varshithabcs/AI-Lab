
from heapq import heappush, heappop


# Misplaced Tiles Heuristic
def heuristic(state, goal):
    return sum(
        1 for i in range(9)
        if state[i] != 0 and state[i] != goal[i]
    )


# Generate neighboring states
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    moves = [-3, 3, -1, 1]

    for move in moves:
        new = zero + move

        if 0 <= new < 9:
            if abs(move) == 3 or new // 3 == zero // 3:
                temp = list(state)
                temp[zero], temp[new] = temp[new], temp[zero]
                neighbors.append(tuple(temp))

    return neighbors


# A* Search Algorithm
def astar(start, goal):
    pq = []
    heappush(pq, (heuristic(start, goal), 0, start, [start]))

    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor, goal)

                heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None


# Read input
print("Enter initial state (use 0 for blank):")
start = tuple(map(int, input().split()))

print("Enter goal state (use 0 for blank):")
goal = tuple(map(int, input().split()))


# Validate input
if (len(start) != 9 or len(goal) != 9 or
        set(start) != set(range(9)) or
        set(goal) != set(range(9))):

    print("Invalid input! Enter numbers 0 to 8 exactly once.")

else:
    path = astar(start, goal)

    if path:
        print("\n========== SOLUTION FOUND ==========\n")

        for step, state in enumerate(path):
            print(f"Step {step}:")

            for i in range(0, 9, 3):
                print(" ".join(
                    "_" if x == 0 else str(x)
                    for x in state[i:i+3]
                ))

            g = step
            h = heuristic(state, goal)
            f = g + h

            print(f"g(n) = {g}, h(n) = {h}, f(n) = {f}")
            print("-" * 35)

        print("Total moves:", len(path) - 1)

    else:
        print("No solution exists.")