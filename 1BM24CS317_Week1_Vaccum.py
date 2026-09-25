# Vacuum Cleaner Agent
# Simple Reflex Agent + Goal-Based Agent

# Initial state of the environment
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

# Initial position of the vacuum cleaner
position = "A"

print("Initial State:")
print("Room A:", rooms["A"])
print("Room B:", rooms["B"])
print("Vacuum Position:", position)

print("\nVacuum Cleaner Actions:")

# Continue until both rooms are clean
while rooms["A"] == "Dirty" or rooms["B"] == "Dirty":

    # Simple Reflex Agent:
    # If the current room is dirty, suck the dirt
    if rooms[position] == "Dirty":
        print("Room", position, "is Dirty -> Suck")
        rooms[position] = "Clean"

    # If current room is clean, move to the other room
    elif position == "A":
        print("Room A is Clean -> Move Right to Room B")
        position = "B"

    else:
        print("Room B is Clean -> Move Left to Room A")
        position = "A"


# Goal state
print("\nFinal State:")
print("Room A:", rooms["A"])
print("Room B:", rooms["B"])
print("Vacuum Position:", position)

print("\nGoal Achieved: Both rooms are Clean!")