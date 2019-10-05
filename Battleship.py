from random import randint

board = []

for ocean in range(5):
    board.append(["O"] * 5)

def print_board(board_in):
    for row in board_in:
        print("  ".join(row))

print("Welcome to Battleship!")
print()
print_board(board)
print()

def random_row(board_in):
    return randint(0, len(board_in) - 1)

def random_col(board_in):
    return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

for turn in range(10):
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Column: "))
    
    if guess_row == ship_row and guess_col == ship_col:
        print()
        print("Congratulations! You sank the tiniest Battleship ever!")
        print()
        board[guess_row][guess_col] = "B"
        print_board(board)
        break
    else:
        print()
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You already guessed that one!")
        else:
            print("You missed!")
            board[guess_row][guess_col] = "X"
        print("Try Again")
        print()
        print_board(board)
        print()
        if turn == 10:
            print("Game Over")
            print("You'll find them next time!")
