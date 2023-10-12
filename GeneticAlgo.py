import random
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

N = int(config['BoardConfig']['N8'])
# N = int(config['BoardConfig']['N16'])
# N = int(config['BoardConfig']['N32'])
iterations = int(config['BoardConfig']['iterations'])

import random


def random_chromosome(size):  # making random chromosomes
    return [random.randint(1, N) for _ in range(N)]


def fitness(chromosome, max_fitness):
    horizontal_collisions = sum([chromosome.count(queen) - 1 for queen in chromosome]) / 2
    diagonal_collisions = 0

    n = len(chromosome)
    left_diagonal = [0] * 2 * n
    right_diagonal = [0] * 2 * n
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2 * n - 1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i] - 1
        diagonal_collisions += counter / (n - abs(i - n + 1))

    return int(max_fitness - (horizontal_collisions + diagonal_collisions))  # 28-(2+3)=23


def probability(chromosome, fitness, max_fitness):
    return fitness(chromosome, max_fitness) / max_fitness


def random_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"


def reproduce(x, y):  # doing cross_over between two chromosomes
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]


def mutate(x):  # randomly changing the value of a random index of a chromosome
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x


def genetic_queen(population, fitness, max_fitness):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, fitness, max_fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities)  # best chromosome 1
        y = random_pick(population, probabilities)  # best chromosome 2
        child = reproduce(x, y)  # creating two new chromosomes from the best 2 chromosomes
        if random.random() < mutation_probability:
            child = mutate(child)
        print_chromosome(child, max_fitness)
        new_population.append(child)
        if fitness(child, max_fitness) == max_fitness: break
    return new_population


def print_chromosome(chrom, max_fitness):
    # print("Chromosome = {},  Fitness = {}"
    #       .format(str(chrom), fitness(chrom, max_fitness)))
    a = 0
    

def execute_genetic_algo():
    maxFitness = (N * (N - 1)) / 2  # 8*7/2 = 28
    population = [random_chromosome(N) for _ in range(100)]

    generation = 1

    while not maxFitness in [fitness(chrom, maxFitness) for chrom in population]:
        print("=== Generation {} ===".format(generation))
        population = genetic_queen(population, fitness, maxFitness)
        print("")
        print("Maximum Fitness = {}".format(max([fitness(n, maxFitness) for n in population])))
        generation += 1
    chrom_out = []
    print("Solved in Generation {}!".format(generation - 1))
    for chrom in population:
        if fitness(chrom, maxFitness) == maxFitness:
            print("");
            print("One of the solutions: ")
            chrom_out = chrom
            print_chromosome(chrom, maxFitness)

    board = []

    for x in range(N):
        board.append(['0'] * N)

    for i in range(N):
        board[N - chrom_out[i]][i] = '1'

    def print_board(board):
        for row in board:
            print(" ".join(row))

    print_board(board)
