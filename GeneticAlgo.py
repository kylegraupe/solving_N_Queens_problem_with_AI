import random
import configparser
import random


config = configparser.ConfigParser()
config.read('config.ini')

# UNCOMMENT THE LINE ASSOCIATED WITH THE DESIRED BOARD SIZE
N = int(config['BoardConfig']['N8'])  # N = 8
# N = int(config['BoardConfig']['N16'])  # N = 16
# N = int(config['BoardConfig']['N32'])  # N = 32
iterations = int(config['BoardConfig']['iterations'])


def random_chromosome(size):
    """
    Generate a random chromosome representing the placement of queens on the chessboard.

    :param size: The size of the chromosome (number of queens).
    :return: A list representing the chromosome.
    """
    return [random.randint(1, N) for _ in range(N)]


def objective_function(chromosomes, max_obj):
    """
    Compute the objective of a chromosome by calculating the number of attacks between queens.

    :param chromosomes: The chromosome to evaluate.
    :param max_obj: The maximum objective function value (maximum possible attacks to be minimized).
    :return: The objective function value.
    """
    hor_attacks = sum([chromosomes.count(queen) - 1 for queen in chromosomes]) / 2
    diag_attacks = 0

    n = len(chromosomes)
    left_diagonal = [0] * 2 * n
    right_diagonal = [0] * 2 * n
    for i in range(n):
        left_diagonal[i + chromosomes[i] - 1] += 1
        right_diagonal[len(chromosomes) - i + chromosomes[i] - 2] += 1

    diag_attacks = 0
    for i in range(2 * n - 1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i] - 1
        diag_attacks += counter / (n - abs(i - n + 1))

    return int(max_obj - (hor_attacks + diag_attacks))


def probability(chromosome, objective, max_objective):
    """
    Calculate the probability of selecting a chromosome based on its objective function.

    :param chromosome: The chromosome to evaluate.
    :param objective: The objective function.
    :param max_objective: The maximum objective value.
    :return: The probability of selecting the chromosome.
    """
    return objective(chromosome, max_objective) / max_objective


def random_selection(population, probabilities):
    """
    Select a chromosome from the population with a probability based on its objective function.

    :param population: The population of chromosomes.
    :param probabilities: A list of probabilities corresponding to the chromosomes in the population.
    :return: The selected chromosome.
    """
    population_with_probabilty = zip(population, probabilities)
    total = sum(w for c, w in population_with_probabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "USER ERROR: no solution"


def reproduce(x, y):
    """
    Perform crossover (reproduction) between two chromosomes to create two new chromosomes.

    :param x: The first parent chromosome.
    :param y: The second parent chromosome.
    :return: Two new chromosomes resulting from crossover.
    """
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]


def mutate(x):
    """
    Mutate a chromosome by randomly changing the value of a random index.

    :param x: The chromosome to mutate.
    :return: The mutated chromosome.
    """
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x


def genetic_queen(population, objective, max_objective):
    """
    Perform the genetic algorithm to find a solution to the N-Queens problem.

    :param population: The initial population of chromosomes.
    :param objective: The objective function.
    :param max_objective: The maximum objective value.
    :return: The updated population after one generation.
    """
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, objective, max_objective) for n in population]
    for i in range(len(population)):
        x = random_selection(population, probabilities)
        y = random_selection(population, probabilities)
        child = reproduce(x, y)
        if random.random() < mutation_probability:
            child = mutate(child)
        print_chromosome(child, max_objective)
        new_population.append(child)
        if objective(child, max_objective) == max_objective: break
    return new_population


def print_chromosome(chrom, max_obj):
    a = 0


def execute_genetic_algo():
    """
    Executes Genetic Algorithm
    :return:
    """
    for i in range(iterations):
        solution_count = 0
        objective_max = (N * (N - 1)) / 2
        population = [random_chromosome(N) for _ in range(100)]

        generation = 1

        while not objective_max in [objective_function(chrom, objective_max) for chrom in population]:
            print(f"========= Generation {generation} =========")
            population = genetic_queen(population, objective_function, objective_max)

            print(f"Max Objective Value = {max([objective_function(n, objective_max) for n in population])}")
            generation += 1

        chrom_out = []
        print(f"Solved in Generation {generation - 1}!")
        for chrom in population:
            if objective_function(chrom, objective_max) == objective_max:

                print("Solution to N Queens: ")
                solution_count += 1
                chrom_out = chrom
                print_chromosome(chrom, objective_max)

        board = []

        for x in range(N):
            board.append(['0'] * N)

        for i in range(N):
            board[N - chrom_out[i]][i] = '1'

        def print_board(board):
            for row in board:
                print(" ".join(row))

        print_board(board)

    print(f"Total number of solutions of {iterations} iterations: {solution_count}")

