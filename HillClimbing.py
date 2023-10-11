import configparser
from random import randint

config = configparser.ConfigParser()
config.read('config.ini')

N = int(config['BoardConfig']['N'])


def random_board_config(board, state, n_):
    """
    Randomly configure the chessboard with queens.

    :param board: The chessboard.
    :param state: The state representing queen positions.
    :param n_: The size of the board.
    """
    for i in range(n_):
        state[i] = randint(0, 100000) % n_
        board[state[i]][i] = 1


def print_board(board, n_):
    """
    Print the configuration of the chessboard.

    :param board: The chessboard.
    :param n_: The size of the board.
    """
    for i in range(n_):
        print(board[i])


def print_state(state):
    """
    Print the current state of queen positions.

    :param state: The state representing queen positions.
    """
    print(state)


def bool_compare_states(state_1, state_2, n_):
    """
    Compare two states representing queen positions.

    :param state_1: The first state.
    :param state_2: The second state.
    :param n_: The size of the board.
    :return: True if the states are equal, False otherwise.
    """
    for i in range(n_):
        if state_1[i] != state_2[i]:
            return False

    return True


def fill_board(board, value, n_):
    """
    Fill the chessboard with a specified value.

    :param board: The chessboard.
    :param value: The value to fill.
    :param n_: The size of the board.
    """
    for i in range(n_):
        for j in range(n_):
            board[i][j] = value


def objective(board, state, n_):
    """
    Calculate the number of pairwise attacks, aiming to minimize it.

    :param board: The chessboard.
    :param state: The state representing queen positions.
    :param n_: The size of the board.
    :return: The number of attacking queen pairs (to be minimized).
    """
    attacking = 0
    for i in range(n_):
        row = state[i]
        col = i - 1
        while col >= 0 and board[row][col] != 1:
            col -= 1
        if col >= 0 and board[row][col] == 1:
            attacking += 1

        row = state[i]
        col = i + 1
        while col < n_ and board[row][col] != 1:
            col += 1
        if col < n_ and board[row][col] == 1:
            attacking += 1

        row = state[i] - 1
        col = i - 1
        while col >= 0 and row >= 0 and board[row][col] != 1:
            col -= 1
            row -= 1
        if col >= 0 and row >= 0 and board[row][col] == 1:
            attacking += 1

        row = state[i] + 1
        col = i + 1
        while col < n_ and row < n_ and board[row][col] != 1:
            col += 1
            row += 1
        if col < n_ and row < n_ and board[row][col] == 1:
            attacking += 1

        row = state[i] + 1
        col = i - 1
        while col >= 0 and row < n_ and board[row][col] != 1:
            col -= 1
            row += 1
        if col >= 0 and row < n_ and board[row][col] == 1:
            attacking += 1

        row = state[i] - 1
        col = i + 1
        while col < n_ and row >= 0 and board[row][col] != 1:
            col += 1
            row -= 1
        if col < n_ and row >= 0 and board[row][col] == 1:
            attacking += 1

    return int(attacking / 2)


def generate_board(board, state):
    """
    Generate a chessboard configuration based on the queen positions.

    :param board: The chessboard.
    :param state: The state representing queen positions.
    """
    fill_board(board, 0, N)
    for i in range(N):
        board[state[i]][i] = 1


def copy_state(state1, state2):
    """
    Copy the values from one state to another.

    :param state1: The target state.
    :param state2: The source state.
    """
    for i in range(N):
        state1[i] = state2[i]


def get_neighbour(board, state):
    """
    Find an optimal neighbor for the given state.

    :param board: The chessboard.
    :param state: The current state.
    """
    opBoard = [[0 for _ in range(N)] for _ in range(N)]
    opState = [0 for _ in range(N)]

    copy_state(opState, state)
    generate_board(opBoard, opState)

    opObjective = objective(opBoard, opState, N)

    NeighbourBoard = [[0 for _ in range(N)] for _ in range(N)]
    NeighbourState = [0 for _ in range(N)]
    copy_state(NeighbourState, state)
    generate_board(NeighbourBoard, NeighbourState)

    for i in range(N):
        for j in range(N):
            if j != state[i]:
                NeighbourState[i] = j
                NeighbourBoard[NeighbourState[i]][i] = 1
                NeighbourBoard[state[i]][i] = 0
                temp = objective(NeighbourBoard, NeighbourState, N)

                if temp <= opObjective:
                    opObjective = temp
                    copy_state(opState, NeighbourState)
                    generate_board(opBoard, opState)

                NeighbourBoard[NeighbourState[i]][i] = 0
                NeighbourState[i] = state[i]
                NeighbourBoard[state[i]][i] = 1

    copy_state(state, opState)
    fill_board(board, 0, N)
    generate_board(board, state)


def hill_climbing(board, state, n_=N):
    neighbourBoard = [[0 for _ in range(n_)] for _ in range(n_)]
    neighbourState = [0 for _ in range(n_)]

    copy_state(neighbourState, state)
    generate_board(neighbourBoard, neighbourState)

    while True:
        copy_state(state, neighbourState)
        generate_board(board, state)

        get_neighbour(neighbourBoard, neighbourState)

        if bool_compare_states(state, neighbourState, N):
            print_board(board, N)
            break
        elif objective(board, state, N) == objective(neighbourBoard, neighbourState, N):
            neighbourState[randint(0, 100000) % N] = randint(0, 100000) % N
            generate_board(neighbourBoard, neighbourState)


def execute_hill_climbing():
    """
    Execute the hill climbing algorithm to find a solution for the N-Queens problem.
    """
    state = [0] * N
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Generate a random starting point by
    # randomly configuring the board
    random_board_config(board, state, N)

    # Perform hill climbing on the
    # obtained board configuration
    hill_climbing(board, state)

