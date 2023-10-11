# Hill Climbing Algorithm for the N-Queens Problem

This repository contains a Python implementation of the Hill Climbing algorithm to solve the N-Queens problem. The N-Queens problem is a classic combinatorial optimization problem that involves placing N chess queens on an N×N chessboard so that no two queens threaten each other. Thus, a solution requires that no two queens share the same row, column, or diagonal.

The Hill Climbing algorithm is a local search algorithm that starts with a random initial solution and iteratively makes small changes to the current solution to optimize a given objective function. In this case, the objective is to minimize the number of pairwise attacks between queens.

## Contents

- [Algorithm Overview](#algorithm-overview)
- [Usage](#usage)
- [Algorithm Details](#algorithm-details)
- [License](#license)

## Algorithm Overview

The Hill Climbing algorithm implemented in this repository follows these key steps:

1. **Random Initialization:** It starts with a random initial solution. The chessboard is randomly configured with queens, and the objective function is computed.

2. **Local Search:** The algorithm iteratively explores neighboring solutions. It selects a neighboring state that improves the objective function and moves to that state. This process is repeated until it reaches a local optimum where no better neighbor can be found.

3. **Random Restart:** If the algorithm gets stuck in a local optimum, it can escape by performing a random restart. It generates a new random initial solution and repeats the local search.

4. **Termination:** The algorithm terminates when either it finds a solution with zero attacks (i.e., a valid N-Queens solution) or reaches a predefined number of iterations.

## Usage

To use the Hill Climbing algorithm to solve the N-Queens problem, follow these steps:

1. Ensure you have Python 3.x installed on your system.

2. Clone or download this repository to your local machine.

3. Install the required dependencies if not already installed. You can do this using pip:

   ```bash
   pip install configparser
   ```

4. Run the `hill_climbing_nqueens.py` script using the following command:

   ```bash
   python hill_climbing_nqueens.py
   ```

5. The algorithm will execute and display the final N-Queens solution on the console.

## Algorithm Details

- **`random_board_config(board, state, N_)`:** This function randomly configures the chessboard with queens. It assigns random positions for queens on the board and updates the state.

- **`print_board(board, N_)`:** This function prints the current configuration of the chessboard, showing the positions of the queens.

- **`print_state(state)`:** Prints the current state, which represents the positions of queens.

- **`compare_states(state_1, state_2, N_)`:** Compares two states to check if they are equal, which is useful for determining if a local optimum has been reached.

- **`fill(board, value, N_)`:** Fills the chessboard with a specified value, where 1 represents the presence of a queen, and 0 represents an empty square.

- **`objective(board, state, N_)`:** Computes the number of pairwise attacks in the current state. The objective is to minimize this value.

- **`generate_board(board, state)`:** Generates a chessboard configuration based on the queen positions.

- **`copy_state(state1, state2)`:** Copies the values from one state to another.

- **`get_neighbour(board, state)`:** Finds the optimal neighbor by considering neighboring states and their objectives.

- **`hill_climbing(board, state, N_)`:** The main Hill Climbing algorithm, which iteratively searches for a solution by exploring neighboring states.

- **`execute_hill_climbing()`:** The entry point of the script. It initializes the algorithm and starts the hill climbing process.

## License

This implementation of the Hill Climbing algorithm for the N-Queens problem is provided under the [MIT License](LICENSE). You are free to use and modify the code as needed.