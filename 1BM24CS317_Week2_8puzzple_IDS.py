# 8-Puzzle using DLS and IDS
# 0 represents the blank space

def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def moves(state):
    result = []
    z = state.index(0)

    for d in [-3, 3, -1, 1]:
        n = z + d

        if 0 <= n < 9:
            if d == -1 and z % 3 == 0:
                continue
            if d == 1 and z % 3 == 2:
                continue

            s = list(state)
            s[z], s[n] = s[n], s[z]
            result.append(tuple(s))

    return result


def dls(state, goal, limit, path):
    if state == goal:
        return path

    if limit == 0:
        return None

    for nxt in moves(state):
        if nxt not in path:
            result = dls(nxt, goal, limit - 1, path + [nxt])
            if result:
                return result

    return None


def ids(initial, goal, max_depth=20):
    for depth in range(max_depth + 1):
        print("Depth limit:", depth)
        result = dls(initial, goal, depth, [initial])

        if result:
            print("Goal found!")
            print("Moves:", len(result) - 1)

            for i, state in enumerate(result):
                print("Step", i)
                display(state)
            return

    print("Goal not found")


initial = tuple(map(int, input("Enter 9 numbers (0 = blank): ").split()))

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

if len(initial) == 9 and set(initial) == set(range(9)):
    ids(initial, goal)
else:
    print("Invalid input! Enter numbers 0 to 8 exactly once.")