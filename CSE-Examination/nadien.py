def gps_tracker():
    x, y = 0, 0  # starting position

    print("Welcome to the GPS Tracker!")
    print("Starting at position (0, 0)")
    print("Enter N, S, E, W to move or STOP to end.\n")

    while True:
        move = input("Enter direction: ").strip().lower()

        if move in ["n", "north"]:
            y += 1
        elif move in ["s", "south"]:
            y -= 1
        elif move in ["e", "east"]:
            x += 1
        elif move in ["w", "west"]:
            x -= 1
        elif move == "stop":
            break
        else:
            print("Invalid input! Use N, S, E, W or STOP.")
            continue

        print(f"Current position: ({x}, {y})")

    print("\nSession ended.")
    print(f"Final position: ({x}, {y})")
    if (x, y) == (0, 0):
        print("You returned to the origin (0, 0).")
    else:
        print("You did not return to the origin.")

if __name__ == "__main__":
    gps_tracker()
