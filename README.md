Certainly, here's a short README.md file for your application:


# N-Queens Solver

This application provides two different algorithms for solving the N-Queens problem with varying board sizes (N = 8, N = 16, or N = 32) and a fixed number of iterations (100). You can choose to use either the Genetic Algorithm or the Hill Climbing Algorithm to find a solution to the N-Queens puzzle.

## Getting Started

To run the N-Queens solver, follow these steps:

1. Clone this repository to your local machine. git clone <repository-link>


2. Ensure you have Python installed on your system.

3. Configure the board size and other parameters by modifying the 'config.ini' file. Uncomment the line associated with the desired board size (N = 8, N = 16, or N = 32).

4. Run the application to choose between the Genetic Algorithm and Hill Climbing Algorithm for solving the N-Queens problem:

```bash
python main.py
```

5. The chosen algorithm will attempt to find a solution for the specified board size and display the result, including the final chessboard configuration with queens placed to avoid attacks.

## Algorithms

### Genetic Algorithm

The Genetic Algorithm uses a population of randomly generated solutions to evolve and find the optimal solution by selecting the fittest individuals, performing crossover (reproduction), and applying mutation.

### Hill Climbing Algorithm

The Hill Climbing Algorithm starts with a random board configuration and iteratively improves the solution by making small changes to minimize the number of queen attacks.

## Contributors

- [Your Name](https://github.com/your-github-username)

Feel free to contribute to this project by improving the algorithms, adding new features, or fixing bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Make sure to replace `<repository-link>` with the actual link to your repository. You can also add contributors and update the license information as needed.