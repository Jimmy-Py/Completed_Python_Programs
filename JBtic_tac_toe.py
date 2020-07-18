# 2019 Python3 version of Tic Tac, JB. Started 2-24-19
# Plays Tic Tac Toe with the user.

# Global Constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    """Displays game instructions."""
    print(
        """
Welcome to Tic-Tac
        
You will make your move by entering a number, 0 - 8. The number will correspond to a space on the board as illustrated:
        
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8\n
""")


def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Asks for a number within a range."""
    response = None  # defining variable to be used.
    while response not in range(low, high):
        response = int(input(question))
        if response >= 9:
            print("\nSorry, '8' is the highest numbered square on the board, please choose a square that is 8 or below.")
    return response


def pieces():
    """Determine if human or computer goes first."""
    go_first = ask_yes_no("Would you like to go first? y/n: ")
    if go_first == "y":
        print("You will go first.")
        human = X
        computer = O
    else:
        print("You will go second.")
        human = O
        computer = X
    return computer, human


def new_board():
    """Create a new board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Display board on screen"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Create a list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2),  # Horizontals
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),  # Verticals
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),  # Diagonals
                   (6, 4, 2))
    # Search board for winning entries.
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def human_move(board, human):
    """Get human move."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("That square is already occupied. Make a different selection.\n")
    return move


def computer_move(board, computer, human):
    """Make computer move."""
    # Make a local copy to work with, since the function will be changing the list.
    board = board[:]
    # Best positions to have, in order:
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I shall take square number", end=" ")

    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY

    # if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checkin this move, undo it
        board[move] = EMPTY

    # No move immediately wins, choose best move based off list.
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X


def congrat_the_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner == human:
        print("The human wins wins!\n")
    elif the_winner == computer:
        print("The computer wins!\n")
    else:
        print("It's a tie!\n")


def main():
    computer, human = pieces()  # Asks user to pick X's or O's.
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human  # Makes that square on the board an X or an O (depending on the human piece selection.)
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
            # Display a reference board for users to determine the number of the square they want to play on.
            print(
                """
                (Reference Board)
        
                0 | 1 | 2
                ---------
                3 | 4 | 5
                ---------
                6 | 7 | 8
                """
            )
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_the_winner(the_winner, computer, human)

# Start the program.
display_instruct()
selection = 0
while selection == 0:
    main()
    # selection = int(input("Enter '0' to continue, or enter '1' to exit. "))
