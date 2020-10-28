import random
import copy


def init_board(n=5, random_chance=20):
    """Initialise a random board with a 1/5 chance of life per index"""
    # TODO: Make it so you can adjust height [complete] AND width, snakify.org for tutorial

    board = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            num = random.randrange(0, 100)
            if num <= random_chance:   # change this value to edit the randomisation
                board[i][j] = 1
            else:
                board[i][j] = 0

    return board


def print_board(board):
    """Print a board array"""
    for line in board:
        for x in line:
            print(x, end=" ")
        print()


def update_board(original_board):
    """Go over the ruleset and original board to update the cloned board"""
    # TODO also value of m so I can have an asymmetrical array
    # the number of rows of a list of lists would be len(A)
    # the number of columns len(A[0]) given that all rows have the same number of columns

    board_to_update = copy.deepcopy(original_board)
    n = len(original_board)
    for i in range(n):
        for j in range(n):
            total = 0

            if i > 0 and original_board[i - 1][j] == 1:
                total += 1
            if j > 0 and original_board[i][j - 1] == 1:
                total += 1
            if i > 0 and j > 0 and original_board[i - 1][j - 1] == 1:
                total += 1
            if i < n - 1 and original_board[i + 1][j] == 1:
                total += 1
            if j < n - 1 and original_board[i][j + 1] == 1:
                total += 1
            if i < n - 1 and j < n - 1 and original_board[i + 1][j + 1] == 1:
                total += 1
            if i < n - 1 and j > 0 and original_board[i + 1][j - 1] == 1:
                total += 1
            if i > 0 and j < n - 1 and original_board[i - 1][j + 1] == 1:
                total += 1

            # print total here for bug-finding

            # death
            if total < 2 or total > 3 and original_board[i][i] == 1:
                board_to_update[i][j] = 0
            # birth
            if total == 3 and original_board[i][j] == 0:
                board_to_update[i][j] = 1

    return board_to_update


my_board = init_board(5, 50)

print("\n ORIGINAL BOARD")
print_board(my_board)

updated_board = update_board(list(my_board))
print("\n UPDATED BOARD")
print_board(updated_board)
