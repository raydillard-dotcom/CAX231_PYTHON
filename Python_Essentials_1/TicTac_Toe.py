
from random import randrange


def display_board(board):
    """Accepts the board's current status and prints it out to the console."""
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    """Asks the user for their move, checks input validity, and updates the board."""
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Bad move: enter a number from 1 to 9.")
                continue

            # Map 1-9 to 3x3 grid coordinates (row, col)
            row = (move - 1) // 3
            col = (move - 1) % 3

            # Check if the field is free (still an integer)
            if isinstance(board[row][col], int):
                board[row][col] = 'O'
                break
            else:
                print("Field already occupied, choose another one.")
        except ValueError:
            print("Invalid input: please enter an integer between 1 and 9.")


def make_list_of_free_fields(board):
    """Browses the board and builds a list of tuples representing free squares (row, col)."""
    free_fields = []
    for row in range(3):
        for col in range(3):
            if isinstance(board[row][col], int):
                free_fields.append((row, col))
    return free_fields


def victory_for(board, sign):
    """Analyzes the board status to check if the given sign ('X' or 'O') has won."""
    # Check rows and columns
    for r in range(3):
        if board[r][0] == sign and board[r][1] == sign and board[r][2] == sign:
            return True
        if board[0][r] == sign and board[1][r] == sign and board[2][r] == sign:
            return True

    # Check diagonals
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False


def draw_move(board):
    """Selects a random free field for the computer's move and updates the board."""
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        index = randrange(len(free_fields))
        row, col = free_fields[index]
        board[row][col] = 'X'


def main():
    # Initialize the board with numbers 1 through 9
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Computer makes the first move in the center
    board[1][1] = 'X'
    human_turn = True

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O' and the computer is 'X'.")

    while True:
        display_board(board)

        if human_turn:
            enter_move(board)
            if victory_for(board, 'O'):
                display_board(board)
                print("You won!")
                break
            human_turn = False
        else:
            print("\nComputer's turn...")
            draw_move(board)
            if victory_for(board, 'X'):
                display_board(board)
                print("Computer won!")
                break
            human_turn = True

        if not make_list_of_free_fields(board):
            display_board(board)
            print("It's a tie!")
            break


if __name__ == "__main__":
    main()