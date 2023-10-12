import HillClimbing
import GeneticAlgo


def execute_search(version):
    if version == 1:
        HillClimbing.execute_hill_climbing()
    if version == 2:
        GeneticAlgo.execute_genetic_algo()


if __name__ == '__main__':
    execute_search(2)
